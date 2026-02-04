states = ['A','B','C','D']
neighbors = {'A':['B','C'],'B':['A','C','D'],'C':['A','B','D'],'D':['B','C']}
colors = ['Red','Green','Blue']

def safe(s,c,a):
    return all(a.get(n)!=c for n in neighbors[s])

def solve(a={}):
    if len(a)==4: return a
    s = [x for x in states if x not in a][0]
    for c in colors:
        if safe(s,c,a):
            a[s]=c
            r = solve(a)
            if r: return r
            del a[s]

ans = solve()
print(ans)
