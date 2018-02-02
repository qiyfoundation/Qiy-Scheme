import re

definitions="""
"""

lines=definitions.split("\n")

defs=[]
for line in lines:
    definition=line.split("\t")
    if len(definition)>1:
        defs.append(definition)

def complete_references(text):
    text=re.sub(r'\[([A-Za-z ]*)ies\]([^(])',r'[\1ies](#\1y)\2',text)
    text=re.sub(r'\[([A-Za-z ]*)s\]([^(])',r'[\1s](#\1)\2',text)
    text=re.sub(r'\[([A-Za-z ]*)\]([^(])',r'[\1](#\1)\2',text)
    return text
    
def add_anchor(match_object):
    term=match_object.group(1)
    anchor_id=term.lower().replace(" ","-")
    anchor='<a id="{1}">{0}</a>'.format(term,anchor_id)
    return anchor

def create_anchors(text):
    text=re.sub(r'\[\[([A-Za-z ]*)\]\]',add_anchor,text)
    return text

def create_toc(text):
    body=text.split("${toc}")[1]
    lines=body.split("\n")
    toc=""
    for line in lines:
        if len(line)>1:
            if line[0]=="#":
                toc_entry=create_toc_entry(line)
                toc="{0}\n{1}".format(toc,toc_entry)
    text=text.replace("${toc}",toc)
    return text


def create_toc_entry(s):
    entry=""
    split=s.split(" ")
    level=len(split[0])
    heading_number=split[1]
    offset=level+len(heading_number)+2
    heading_text=s[offset:]
    while level>1:
        entry=entry+"\t"
        level=level-1
    entry="{0}1. [{2}](#{1} {2})".format(entry,heading_number,heading_text)
    return entry


def generate_anchors():
    for d in defs:
        term=d[0]
        description=d[1]

        a_id=term.lower().replace(" ","-")
        dm_link="[{0}](#{1})".format(term,a_id)
        anchor='<a id="{1}">{0}</a>'.format(term,a_id)
        print("{0}{1}".format(anchor,description))

def read_text(filename):
    with open(filename,'r') as f:
        s=f.read()
    return s


def write_text(filename,txt):
    with open(filename,'w') as f:
        f.write(txt)

def renumber(s,van,naar):
    s=s.replace("# {0}".format(van),"# {0}".format(naar))
    s=s.replace("#{0}".format(van),"#{0}".format(naar))
    s=s.replace("[{0}".format(van),"[{0}".format(naar))
    return s

def move_chapters():
    text=renumber(text,"10","11")
    text=renumber(text,"9","10")
    text=renumber(text,"8","9")
    text=renumber(text,"7","8")
    text=renumber(text,"6","7")
    text=renumber(text,"5","6")
    text=renumber(text,"4","5")
    text=renumber(text,"3","4")
    #text=renumber(text,"2","3")
    write_text('renumbered.out',text)

def source2gitbucket():
    text=read_text('FuncQiy-source.md')
    text=create_anchors(text)
    text=complete_references(text)
    text=create_toc(text)
    write_text('FuncQiy-gitbucket.md',text)

source2gitbucket()
