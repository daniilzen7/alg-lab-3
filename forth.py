import sys
 
class Graph(object): # создание и конутсрукция графа
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        Этот метод обеспечивает симметричность графика. Другими словами, 
        если существует путь от узла A к B со значением V, должен быть путь от 
        узла B к узлу A со значением V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Возвращает узлы графа"
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Возвращает соседей узла"
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Возвращает значение ребра между двумя узлами."
        if node1 == node2:
            return 10**10
        else:
            if node2 in graph.get_outgoing_edges(node1):
                return self.graph[node1][node2]
            else:
                return 10**10


def dijkstra_algorithm(graph, value, node):
    '''
        Алгоритм Дейкстры, возвращающий пункт и путь к нему по формуле
        из презы
    '''
    global nodes
    global d
    nodes.remove(node)

    dmin = 10000
    for i in nodes:
        d[i] = min(d[i], value + graph.value(node, i))
        if d[i] < dmin:
            ans_node = i
            ans_value = d[i]
            dmin = d[i]

    return ans_node, ans_value

nodes = ["Москва", "Санкт-Петербург", "Архангельск", "Тольятти", "Калининград", "Чита"]
 
init_graph = {}
for node in nodes:
    init_graph[node] = {}
    
init_graph["Калининград"]["Санкт-Петербург"] = 1
init_graph["Калининград"]["Москва"] = 4
init_graph["Санкт-Петербург"]["Архангельск"] = 2
init_graph["Санкт-Петербург"]["Москва"] = 3
init_graph["Москва"]["Тольятти"] = 4
init_graph["Архангельск"]["Тольятти"] = 4
init_graph["Тольятти"]["Чита"] = 8
init_graph["Чита"]["Москва"] = 6
# создали граф с городами
print('Граф:', init_graph, '\n')

graph = Graph(nodes, init_graph)

node = "Калининград"
ans_value = 0
d = {"Москва": 10**10, "Санкт-Петербург": 10**10, "Архангельск": 10**10,
     "Тольятти": 10**10, "Калининград": 10**10, "Чита": 10**10}
d.pop(node)
for i in range(5): # пробегаем циклом по всем городам
    node, ans_value = dijkstra_algorithm(graph, ans_value, node)

print('Кратчайшее расстояние от выбранного города до:', d)