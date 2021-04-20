def duplicate(l):
    m=[]
    for i in l:
        if(i not in m):
            m.append(i)
    print(m)
def unique(l):
    m=[]
    for i in l:
        if(l.count(i)==1):
            m.append(i)
    print(m)