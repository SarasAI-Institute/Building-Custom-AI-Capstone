from pathlib import Path
import ast, hashlib, json
ROOT=Path(__file__).resolve().parents[1]
def test_exact_criterion_inventory():
    data=json.loads((ROOT/"assessment/criteria.json").read_text())
    criteria=data["criteria"] if isinstance(data,dict) else data
    assert len(criteria)==24
    assert {c["id"] for c in criteria}=={f"C{m}.{i}" for m,n in [(1,5),(2,5),(3,5),(4,5),(5,4)] for i in range(1,n+1)}
    assert {c["id"] for c in criteria if c["must_pass"]}=={"C1.1","C2.3","C3.2","C4.2","C5.1"}
    rubric=(ROOT/"RUBRICS.md").read_text()
    for c in criteria:assert c["id"] in rubric

def test_embedded_helper_matches_source():
    nb=json.loads((ROOT/"capstone_starter.ipynb").read_text())
    embedded="".join(nb["cells"][6]["source"])
    assert ast.dump(ast.parse(embedded))==ast.dump(ast.parse((ROOT/"risklens_support.py").read_text()))

def test_reference_pdfs_are_unchanged():
    folder=ROOT/'assessment/reference'
    manifest=json.loads((folder/'SOURCE_MANIFEST.json').read_text())
    assert len(manifest)==7
    for row in manifest:
        assert hashlib.sha256((folder/row['name']).read_bytes()).hexdigest()==row['sha256']

def test_review_gate_does_not_fail_unreviewed_criteria():
    import sys
    import pytest
    sys.path.insert(0,str(ROOT/'scripts'))
    from check_review import check_review
    template=json.loads((ROOT/'assessment/feedback_template.json').read_text())
    criteria=json.loads((ROOT/'assessment/criteria.json').read_text())['criteria']
    result=check_review(template,criteria)
    assert result['competencies']['1']=='Not fully reviewed'
    template.update(reviewer='Reviewer',submission_version='snapshot-1')
    template['criteria']['C1.1'].update(judgment='Not Yet',evidence='D1.1',feedback='No frozen split',required_revision='Freeze and document an independent split')
    assert check_review(template,criteria)['competencies']['1']=='Not Yet'
    assert template['criteria']['C1.2']['judgment'] is None
    template['criteria']['C1.2'].update(judgment='Met',evidence='D1.2',feedback='Seen')
    with pytest.raises(ValueError):check_review(template,criteria)
