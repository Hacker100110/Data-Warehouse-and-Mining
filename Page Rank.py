def page_rank(links, damping=0.85, max_iter=100, tol=1e-6):
    nodes = list(links.keys())
    N = len(nodes)
    page_rank = {node: 1.0 / N for node in nodes}
    
    # Power iteration: Apply the PageRank formula iteratively
    for iteration in range(max_iter):
        old_page_rank = page_rank.copy()
        for node in nodes:
            rank_sum = 0
            for other_node in nodes:
                if node in links[other_node]:  # Check if other_node links to this node
                    out_links = len(links[other_node])
                    if out_links > 0:
                        rank_sum += old_page_rank[other_node] / out_links
            
            # Update PageRank value
            page_rank[node] = (1 - damping) / N + damping * rank_sum
        
        # Check convergence
        if sum(abs(page_rank[node] - old_page_rank[node]) for node in nodes) < tol:
            print(f"Converged in {iteration + 1} iterations.")
            break
    
    return page_rank

def get_graph_from_user():
    links = {}
    
    # Input all nodes in one line
    nodes_input = input("Enter all nodes separated by spaces: ").strip().split()
    
    for node in nodes_input:
        links[node] = []
        links_input = input(f"Enter the nodes that {node} links to (separated by spaces): ").strip()
        links[node] = links_input.split() if links_input else []  # Allow for no links
    
    return links

# Example usage
if __name__ == "__main__":
    links = get_graph_from_user()
    ranks = page_rank(links)
    print("\nPageRank values:")
    for node, rank in ranks.items():
        print(f"{node}: {rank:.6f}")
