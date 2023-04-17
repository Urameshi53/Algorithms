# states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])

# stations = {}
# stations["kone"] = set(["id", "nv", "ut"])
# stations["ktwo"] = set(["wa", "id", "mt"])
# stations["kthree"] = set(["or", "nv", "ca"])
# stations["kfour"] = set(["nv", "ut"])
# stations["kfive"] = set(["ca", "az"])
# final_stations = set()
# while states_needed:
# 	best_station = None
# 	states_covered = set()
# 	for station, states_for_station in stations.items():
# 		covered = states_needed & states_for_station
# 		if len(covered) > len(states_covered):
# 			best_station = station
# 			states_covered = covered
# 	states_needed -= states_covered
# 	final_stations.add(best_station)

# print(final_stations)
# print(stations.items())

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

graph = {}
# graph["you"] = ["alice","bob","claire"]
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None 

path = []

processed = []
# print(graph.items())

def dijkstra():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node 
        processed.append(node)
        node = find_lowest_cost_node(costs)
    print(parents)
    return cost
# print(dijkstra())


l = [1,10,3,12,5]
def resum(l):
    s = 0
    if len(l) == 0:
        return 0
    else:
        s = l[0]+resum(l[1:])
        return s 
# print(resum(l))

def relen(l):
    c = 0
    if len(l) == 1:
        return 1
    else:
        c = 1 + relen(l[1:])
        return c
    
# print(relen(l))
def remax(l):
    m = 0
    if len(l) == 1 and l[0] > m:
        m = l[0]
        return m
    else:
        m = remax(l)
        return m
# print(remax(l))

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort(l))


# Dynamic Programming Top-Down Approach
# l = {0:1,1:1}
# def fib(n):
#     if n not in l:
#         l[n] = fib(n-1)+fib(n-2)
#     return l[n]

# Bottom-Up Approach
# def fib(n):
#     if n == 0:
#         return 1
#     else:
#         p,c = 0,1
#         for i in range(n):
#             new = p+c
#             p = c
#             c = new
#         return c
    
# # for i in range(10000):
# #     print(fib(i))
# print(fib(100000))

# Top-Down Method using factorial
# d = {0:1,1:1}
# def fact(n):
#     if n not in d:
#         d[n] = n*fact(n-1)
#     return d[n]

# print(fact(1000))

# Bottom-Up Method using factorial
def fact(n):
    a = 1
    for i in range(2,n+1):
        a = a*i
    return a

# for i in range(5):
#     print(fact(i))
print(fact(10000))


    
    