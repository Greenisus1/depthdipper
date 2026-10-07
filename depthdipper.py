#!/usr/bin/env python3
"""Depthdipper: JSON value types and depth counts, source values/keys hidden."""
import argparse,collections,json,sys
from pathlib import Path
MAX=1048576
class Number(str):pass
def reject(_):raise ValueError('Nonstandard constant')
def unique(pairs):
    out={}
    for k,v in pairs:
        if k in out:raise ValueError('Duplicate key')
        out[k]=v
    return out
def analyze(data):
    if len(data)>MAX:raise ValueError('Size cap')
    value=json.loads(data.decode('utf-8'),object_pairs_hook=unique,parse_constant=reject,parse_int=Number,parse_float=Number)
    stack=[(value,0)];types=collections.Counter();maximum=0
    while stack:
        v,depth=stack.pop();maximum=max(maximum,depth)
        if isinstance(v,Number):kind='number'
        elif v is None:kind='null'
        elif type(v) is bool:kind='boolean'
        elif isinstance(v,str):kind='string'
        elif isinstance(v,list):kind='array';stack.extend((x,depth+1) for x in v)
        else:kind='object';stack.extend((x,depth+1) for x in v.values())
        types[kind]+=1
    return {'values':sum(types.values()),'types':dict(sorted(types.items())),'max_value_depth':maximum,'note':'Root depth 0; each child value adds 1. Object keys not counted as values. Values/keys hidden, structure sensitive. No schema/security checks. Empty containers are values; parser depth limits apply.'}
def inspect(path):
    p=Path(path)
    if not p.is_file() or p.stat().st_size>MAX:raise ValueError('Regular file <=1 MiB')
    with p.open('rb') as f:data=f.read(MAX+1)
    return analyze(data)
def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('file',nargs='?');a=p.parse_args(argv)
    try:
        path=a.file if a.file is not None else input('JSON file (0 exits): ')
        if a.file is None and path=='0':return 0
        print(json.dumps(inspect(path),indent=2))
    except (ValueError,OSError,RecursionError):print('Cannot inspect regular strict UTF-8 JSON <=1 MiB; source not echoed.',file=sys.stderr);return 2
    except (EOFError,KeyboardInterrupt):print('\nCancelled.')
    return 0
if __name__=='__main__':raise SystemExit(main())
