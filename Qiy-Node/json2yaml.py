from json import load
from yaml import dump

def j2y(filename):
    src=filename
    dst=src.replace(".json",".yaml")
    with open(src,'r') as f:
        t=load(f)

    with open(dst,'w') as f:
        f.write(dump(t))


j2y('openapi.json')
j2y('Server/openapi.json')
j2y('Client/openapi.json')

