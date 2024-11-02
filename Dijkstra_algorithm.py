#Занесли простейший граф 
graph ={}
graph['start']= {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['fin'] = 5
graph['b']['a'] = 3
graph['fin'] = {}

# Cтоимости каждого узла
infinity = float('inf')
costs ={}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# Информация о родителях 
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# Массив, храняший уже проверенные узлы
processed =[]

# Ищем узел с наименьшей стоимостью
def find_lowest_cost_node(costs):  
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost <= lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def Dijkstra_algorithm(graph, costs, parents, item):
    node = find_lowest_cost_node(costs)
    while node!=  None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node 
        processed.append(node)
        node = find_lowest_cost_node(costs)
    return costs[item]
        
print(Dijkstra_algorithm(graph, costs, parents, 'fin'))
