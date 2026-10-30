"""Check the structure of a human review, never infer judgments from model metrics."""
import argparse
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def check_review(record, criteria):
    expected={c['id'] for c in criteria}
    if record.get('rubric_version')!='2.0' or set(record.get('criteria',{}))!=expected:
        raise ValueError('Use the exact v2.0 criterion inventory')
    rows=record['criteria']
    reviewed=False
    for key,row in rows.items():
        judgment=row.get('judgment')
        if judgment not in {None,'Met','Not Yet'}:raise ValueError(f'{key}: invalid judgment')
        if judgment is not None:
            reviewed=True
            if any(not isinstance(row.get(field),str) or not row[field].strip() for field in ['evidence','feedback']):
                raise ValueError(f'{key}: reviewed criteria need evidence location and feedback')
            if judgment=='Not Yet' and (not isinstance(row.get('required_revision'),str) or not row['required_revision'].strip()):
                raise ValueError(f'{key}: state the required revision')
    if reviewed and any(not isinstance(record.get(k),str) or not record[k].strip() for k in ['reviewer','submission_version']):
        raise ValueError('Identify reviewer and submission version')
    summary={}
    for module in range(1,6):
        members=[c for c in criteria if c['module']==module]
        gate=next(c['id'] for c in members if c['must_pass'])
        if rows[gate]['judgment']!='Met' and any(rows[c['id']]['judgment'] is not None for c in members if c['id']!=gate):
            raise ValueError(f'Module {module}: review must-pass {gate} first; retain later criteria as not reviewed')
        values=[rows[c['id']]['judgment'] for c in members]
        summary[str(module)]='Mastered' if all(v=='Met' for v in values) else 'Not Yet' if 'Not Yet' in values else 'Not fully reviewed'
    return {'competencies':summary,'project':'Mastered' if all(x=='Mastered' for x in summary.values()) else 'Not fully mastered',
        'scope':'Summary of supplied human judgments only; evidence truth is not machine-verified'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path',type=Path)
    args=parser.parse_args()
    criteria=json.loads((ROOT/'assessment/criteria.json').read_text())['criteria']
    print(json.dumps(check_review(json.loads(args.path.read_text()),criteria),indent=2))
