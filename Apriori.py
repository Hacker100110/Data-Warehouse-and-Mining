from itertools import combinations

def get_input_data():
    transactions = [set(input(f"Enter items in transaction {i + 1} (separated by space): ").split()) 
                    for i in range(int(input("Enter number of transactions: ")))]
    return transactions

def calculate_support(itemset, transactions):
    return sum(1 for transaction in transactions if itemset.issubset(transaction)) / len(transactions)

def apriori(transactions, min_support):
    # Generate 1-itemsets with min_support
    items = {item for transaction in transactions for item in transaction}
    freq_itemsets = [{item} for item in items if calculate_support({item}, transactions) >= min_support]
    all_freq_itemsets, supports = [], {}
    
    # Store supports for single itemsets
    for itemset in freq_itemsets:
        supports[frozenset(itemset)] = calculate_support(itemset, transactions)
        all_freq_itemsets.append(itemset)
        
    k = 2
    while freq_itemsets:
        candidates = [a | b for i, a in enumerate(freq_itemsets) for b in freq_itemsets[i+1:] if len(a | b) == k]
        freq_itemsets = [itemset for itemset in candidates if calculate_support(itemset, transactions) >= min_support]
        
        for itemset in freq_itemsets:
            supports[frozenset(itemset)] = calculate_support(itemset, transactions)
        
        all_freq_itemsets.extend(freq_itemsets)
        k += 1

    return all_freq_itemsets, supports

def generate_association_rules(freq_itemsets, supports, min_confidence):
    rules = []
    for itemset in freq_itemsets:
        for i in range(1, len(itemset)):
            for antecedent in map(set, combinations(itemset, i)):
                consequent = itemset - antecedent
                confidence = supports[frozenset(itemset)] / supports[frozenset(antecedent)]
                if confidence >= min_confidence:
                    rules.append((tuple(antecedent), tuple(consequent), confidence))
    return rules

if __name__ == "__main__":
    transactions = get_input_data()
    min_support = float(input("Enter minimum support (as a decimal): "))
    min_confidence = float(input("Enter minimum confidence (as a decimal): "))
    
    # Generate frequent itemsets and supports
    freq_itemsets, supports = apriori(transactions, min_support)
    
    print("\nFrequent Itemsets:")
    for itemset in freq_itemsets:
        print(tuple(itemset))
    
    # Generate association rules
    rules = generate_association_rules(freq_itemsets, supports, min_confidence)
    
    print("\nAssociation Rules:")
    for antecedent, consequent, confidence in rules:
        print(f"Rule: {antecedent} -> {consequent} [Confidence: {confidence:.2f}]")
