import itertools

korzina = [{'K', 'A', 'D', 'B'}, {'D', 'A', 'C', 'E', 'B'},
           {'C', 'A', 'B', 'E'}, {'B', 'A', 'D'}]

min_supp = 0.6
min_conf = 0.8

def supp(korz, seek):
    if isinstance(seek, str):
        seek = {seek}
    elif isinstance(seek, tuple):
        seek = set(seek)

    r = 0
    for array in korz:
        if seek.issubset(array):
            r+=1
    return r / len(korz)

def conf(korz, L, R):
    LR = merge(L, R)
    if supp(korz, L) != 0:
        return supp(korz, LR)/supp(korz, L)
    else:
        return 0

def merge(set1, set2):
    if isinstance(set1, tuple):
        set1 = set(set1)
    if isinstance(set2, tuple):
        set2 = set(set2)

    if isinstance(set1, str):
        set1 = {set1}
    if isinstance(set2, str):
        set2 = {set2}


    set1_without_set2 = set1-set2
    return set(list(set2 - set1_without_set2) + list(set1))

def apriori(korz, items, n):
    out = []
    for item in items:
        if supp(korz, item)>=min_supp:
            out.append(item)

    print(out)
    if len(out) == 0:
        return []

    all = set()
    for item in out:
        all = merge(all, item)

    print(set(itertools.combinations(all, n+1)))
    out += apriori(korz, set(itertools.combinations(all, n+1)), n+1)

    return out

def get_me_results(korz, ap):
    results = []
    for it in ap:
        if isinstance(it, tuple):
            for item in set(itertools.permutations(it)):
                item = list(item)
                # print(conf(korz, item[0], set(item[1:])))
                conff = conf(korz, item[0], set(item[1:]))
                if conff>min_conf:
                    results.append((item, conff))

    return results


print(supp(korzina, {'B','D'}))
print(conf(korzina, {'B'}, {'D'}))

all = set()
for items in korzina:
    all = merge(all, items)

print(get_me_results(korzina, apriori(korzina, all,1)))


