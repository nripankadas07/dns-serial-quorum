"""Evaluate supplied authoritative SOA observations with RFC 1982 arithmetic."""
import argparse,json,sys
from pathlib import Path

def serial(v):
    if type(v) is not int or not 0<=v<2**32: raise ValueError('serial must be an unsigned 32-bit integer')
    return v

def relation(observed,expected):
    delta=(serial(observed)-serial(expected))%(2**32)
    return 'equal' if delta==0 else 'ambiguous' if delta==2**31 else 'ahead' if delta<2**31 else 'behind'

def evaluate(data):
    if not isinstance(data,dict) or set(data)!={'expected','required','observations'}: raise ValueError('expected, required, observations required')
    expected=serial(data['expected']);obs=data['observations'];required=data['required']
    if not isinstance(obs,list) or not 1<=len(obs)<=1000: raise ValueError('1..1000 observations required')
    if type(required) is not int or not 1<=required<=len(obs): raise ValueError('required must be 1..observation count')
    names=set();rows=[]
    for o in obs:
        if not isinstance(o,dict) or set(o)!={'server','serial'}: raise ValueError('invalid observation')
        name=o['server']
        if not isinstance(name,str) or not name or len(name)>253 or name in names: raise ValueError('unique server label required')
        names.add(name)
        state='unavailable' if o['serial'] is None else relation(o['serial'],expected)
        rows.append({'server':name,'serial':o['serial'],'relation':state})
    counts={k:sum(r['relation']==k for r in rows) for k in ('equal','behind','ahead','ambiguous','unavailable')}
    return {'expected':expected,'required':required,'counts':counts,'quorum_met':counts['equal']>=required,'all_equal':counts['equal']==len(rows),'observations':rows,'warning':'snapshot only; ahead is not equality and half-range order is undefined'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('snapshot');a=p.parse_args()
    try:
        with Path(a.snapshot).open('rb') as f: raw=f.read(262145)
        if len(raw)>262144: raise ValueError('snapshot exceeds 256 KiB')
        print(json.dumps(evaluate(json.loads(raw)),sort_keys=True));return 0
    except (ValueError,OSError,TypeError,KeyError,UnicodeError) as e: print(json.dumps({'error':str(e)}));return 2
if __name__=='__main__':sys.exit(main())
