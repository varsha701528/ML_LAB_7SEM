

import csv
def more_general(h1, h2): 
    more_general_parts = [] 
    for x, y in zip(h1, h2):
        mg = x == "?" or (x != "0" and (x == y or y == "0"))
        more_general_parts.append(mg)
    return all(more_general_parts)
l1 = [1, 2, 3] 
l2 = [3, 4, 5] 
list(zip(l1, l2))


#min_generalizations
def fulfills(example, hypothesis):
# the implementation is the same as for hypotheses:
    return more_general(hypothesis, example)

def min_generalizations(h, x):#find S
    h_new = list(h)
    for i in range(len(h)):
        if not fulfills(x[i:i+1], h[i:i+1]):
            h_new[i] = '?' if h[i] != '0' else x[i]
    return [tuple(h_new)]



min_generalizations(h=('0', '0'  , 'sunny'), x=('rainy', 'windy', 'cloudy'))



def min_specializations(h, domains, x):#g,domains,-ve instance
    results = []
    for i in range(len(h)):
        if h[i] == "?":
            for val in domains[i]:
                if x[i] != val:
                    h_new = h[:i] + (val,) + h[i+1:]
                    results.append(h_new) 
        elif h[i] != "0":
            h_new = h[:i] + ('0',) + h[i+1:]
            results.append(h_new)
    return results
        




min_specializations(h=('?', 'x',),
domains=[['a', 'b', 'e'], ['x', 'y']],
x=('b', 'x')) 


# In[27]:


with open('enjoy.csv')  as csvFile:
    examples = [tuple(line) for line in csv.reader(csvFile)]
print(examples)



def get_domains(examples):
    d = [set() for i in examples[0]]
    for x in examples:
        for i, xi in enumerate(x):
            d[i].add(xi)
    return [list(sorted(x)) for x in d]
get_domains(examples)



def generalize_S(x, G, S): 
    S_prev = list(S)
    for s in S_prev:
        if s not in S:
            continue
        if not fulfills(x, s):#not(s must be true for x)
            S.remove(s)
            Splus = min_generalizations(s, x)
            #keep only generalizations that have a counterpart in G
            S.update([h for h in Splus if any([more_general(g,h)for g in G])])
            #remove hypotheses less specific than any other in S
            S.difference_update([h for h in S if any([more_general(h, h1)for h1 in S if h != h1])])
    return S


def specialize_G(x, domains, G, S): 
    G_prev = list(G)
    for g in G_prev:
        if g not in G:
            continue
        if fulfills(x, g):
            G.remove(g)
            Gminus = min_specializations(g, domains, x)
            #keep only specializations that have a conuterpart in S
            G.update([h for h in Gminus if any([more_general(h, s)
            for s in S])])
            #remove hypotheses less general than any other in G
            G.difference_update([h for h in G if any([more_general(g1, h)
            for g1 in G if h != g1])])
    return G




def candidate_elimination(examples):
    domains = get_domains(examples)[:-1]

    G = set([("?",)*len(domains)])#initial general hypothesis
    S = set([("0",)*len(domains)])#initial specific hypothesis
    i=0
    print("\n G[{0}]:".format(i),G) 
    print("\n S[{0}]:".format(i),S) 
    for xcx in examples:
        i=i+1
        x, cx = xcx[:-1], xcx[-1]
         # Splitting data into attributes and decisions 
        if cx=='Y': # x is positive example
            G = {g for g in G if fulfills(x, g)}
            #remove any general hyp inconsistent with x
            S = generalize_S(x, G, S)
        else: # x is negative example
            S = {s for s in S if not fulfills(x, s)}
            #remove any specific hyp inconsistent with x
            G = specialize_G(x, domains, G, S) 
            print("\n G[{0}]:".format(i),G) 
            print("\n S[{0}]:".format(i),S)

    return S,G




def enumerateHypothesesBetween_s_g(s, g):
    hypotheses = []
    for i, constraint in enumerate(g):
        if constraint != s[i]: 
            hypothesis = g[:] 
            hypothesis[i]=s[i] 
            hypotheses.append(hypothesis)
    return hypotheses

def enumerateVersionSpace(S, G):
    hypotheses = [] 
    hypotheses += S 
    hypotheses += G
    print("Initial Hypothesis",hypotheses)
    s=hypotheses[0]#specific hypothesis for i in range(1,len(hypotheses)):
    inBetweenHypotheses =enumerateHypothesesBetween_s_g(list(s),list(hypotheses[i]))
    hypotheses.extend(inBetweenHypotheses)
    print("Hypothesis with duplicates",hypotheses)
    #Remove duplicates   from hypotheses
    setH = set()
    for h in hypotheses:
        setH.add(tuple(h))
        ans=[list(x) for x in setH]
        print("Version Space:",ans)

S,G=candidate_elimination(examples) 

print(S)
print(G)
