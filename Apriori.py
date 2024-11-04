from itertools import combinations

def get_data():
    trans = [set(input(f"Enter items in transaction {i + 1} (separated by space): ").lower().split()) 
             for i in range(int(input("Enter number of transactions: ")))]
    return trans

def calc_supp(item, trans):
    return sum(1 for tr in trans if item.issubset(tr)) / len(trans)

def apriori(trans, min_supp):
    # Generate initial 1-itemsets with min_supp
    items = {itm for tr in trans for itm in tr}
    freq_sets = [{itm} for itm in items if calc_supp({itm}, trans) >= min_supp]
    all_freq, supps = [], {}
    
    # Store supports for 1-itemsets
    for itm in freq_sets:
        supps[frozenset(itm)] = calc_supp(itm, trans)
        all_freq.append(itm)
        
    k = 2
    while freq_sets:
        # Generate candidates only from combinations of the current frequent itemsets
        cand = [a | b for i, a in enumerate(freq_sets) for b in freq_sets[i + 1:] if len(a | b) == k]
        
        # Filter candidates based on support
        freq_sets = []
        for itm in cand:
            if itm not in supps:  # Avoid recalculating support for the same itemset
                supp = calc_supp(itm, trans)
                if supp >= min_supp:
                    freq_sets.append(itm)
                    supps[frozenset(itm)] = supp
        
        all_freq.extend(freq_sets)
        k += 1

    return all_freq, supps

def gen_rules(freq_sets, supps, min_conf):
    rules = []
    for itm in freq_sets:
        for i in range(1, len(itm)):
            for ant in map(set, combinations(itm, i)):
                cons = itm - ant
                conf = supps[frozenset(itm)] / supps[frozenset(ant)]
                if conf >= min_conf:
                    rules.append((tuple(ant), tuple(cons), conf))
    return rules

if __name__ == "__main__":
    trans = get_data()
    min_supp = float(input("Enter minimum support (as a decimal): "))
    min_conf = float(input("Enter minimum confidence (as a decimal): "))
    
    # Generate frequent itemsets and supports
    freq_sets, supps = apriori(trans, min_supp)
    
    print("\nFrequent Itemsets:")
    for itm in freq_sets:
        print(tuple(itm))
    
    # Generate association rules
    rules = gen_rules(freq_sets, supps, min_conf)
    
    print("\nAssociation Rules:")
    for ant, cons, conf in rules:
        print(f"Rule: {ant} -> {cons} [Confidence: {conf:.2f}]")
