import random
import json

def generate_nodes(email):
    #set random seed based on email ID
    random.seed(email)
    
    #generate number of nodes (between 5 and 10)
    num_nodes = random.randint(5, 10)
    
    #generate nodes with unique names
    nodes = [chr(65 + i) + chr(65 + j) for i in range(num_nodes) for j in range(num_nodes)]
    nodes = nodes[:num_nodes] 
    
    return nodes

def generate_edges(nodes):
    #set random seed based on nodes
    random.seed("".join(nodes))
    
    #Generate random number of edges (between 5 and 15)
    num_edges = random.randint(5, 15)
    
    # generate unique pairs of nodes as edges
    edges = []
    used_pairs = set()
    while len(edges) < num_edges:
        from_node = random.choice(nodes)
        to_node = random.choice(nodes)
        pair = (from_node, to_node)
        if pair not in used_pairs and from_node != to_node:
            cost = round(random.uniform(1, 5), 2)  # Generate random cost/distance
            edges.append({"from": from_node, "to": to_node, "cost": cost})
            used_pairs.add(pair)
    
    return edges

def main(email):
    nodes = generate_nodes(email)
    edges = generate_edges(nodes)
    
    output = {
        "Nodes": nodes,
        "Edges": edges
    }
    
    print(json.dumps(output, indent=4))

if __name__ == "__main__":
    email = input("Enter email ID: ")
    main(email)
