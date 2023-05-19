class node:
    def __init__(self, name, hn):
        self.name = name
        self.hn=hn
        self.neighbours={}
        
    def add_neighbour(self,neighbour_node,weight):
        self.neighbours[neighbour_node.name] = weight
    
    def weight(self,name):        
        return self.neighbours[name]

node_map = {
"Arad" : node('Arad',366),
"Bucharest" : node('Bucharest',0),
"Craiova" : node('Craiova',160),
"Dobreta" : node('Dobreta',242),
"Eforie" : node('Eforie',161),
"Fagaras" : node('Fagaras',178),
"Giurgiu" : node('Giurgiu',77),
"Hirsova" : node('Hirsova',151),
"Lasi" : node('Lasi',226),
"Lugoj" : node('Lugoj',244),
"Mehadia" : node('Mehadia',241),
"Neamt" : node('Neamt',234),
"Oradea" : node('Oradea',380),
"Pitesti" :  node('Pitesti',98),
"Rimnicu" : node('Rimnicu',193),
"Sibiu" : node('Sibiu',253),
"Timisoara" : node('Timisoara',329),
"Urziceni" : node('Urziceni',80),
"Vaslui" : node('Vaslui',199),
"Zerind" : node('Zerind',374)
}

node_map["Arad"].add_neighbour(node_map["Zerind"],75)
node_map["Arad"].add_neighbour(node_map["Timisoara"],118)
node_map["Arad"].add_neighbour(node_map["Sibiu"],140)

node_map["Bucharest"].add_neighbour(node_map["Giurgiu"], 90)
node_map["Bucharest"].add_neighbour(node_map["Urziceni"], 85)
node_map["Bucharest"].add_neighbour(node_map["Pitesti"], 101)
node_map["Bucharest"].add_neighbour(node_map["Fagaras"], 211)

node_map["Craiova"].add_neighbour(node_map["Dobreta"], 120)
node_map["Craiova"].add_neighbour(node_map["Pitesti"], 138)
node_map["Craiova"].add_neighbour(node_map["Rimnicu"], 146)

node_map["Dobreta"].add_neighbour(node_map["Mehadia"], 75)
node_map["Dobreta"].add_neighbour(node_map["Craiova"], 120)

node_map["Eforie"].add_neighbour(node_map["Hirsova"], 86)

node_map["Fagaras"].add_neighbour(node_map["Sibiu"], 99)
node_map["Fagaras"].add_neighbour(node_map["Bucharest"], 211)

node_map["Giurgiu"].add_neighbour(node_map["Bucharest"], 90)

node_map["Hirsova"].add_neighbour(node_map["Urziceni"], 98)
node_map["Hirsova"].add_neighbour(node_map["Eforie"], 86)

node_map["Lasi"].add_neighbour(node_map["Neamt"], 87)
node_map["Lasi"].add_neighbour(node_map["Vaslui"],92)

node_map["Lugoj"].add_neighbour(node_map["Timisoara"], 111)
node_map["Lugoj"].add_neighbour(node_map["Mehadia"], 70)

node_map["Mehadia"].add_neighbour(node_map["Lugoj"], 70)
node_map["Mehadia"].add_neighbour(node_map["Dobreta"], 75)

node_map["Neamt"].add_neighbour(node_map["Lasi"], 87)

node_map["Oradea"].add_neighbour(node_map["Zerind"], 71)
node_map["Oradea"].add_neighbour(node_map["Sibiu"], 151)

node_map["Pitesti"].add_neighbour(node_map["Rimnicu"], 97)
node_map["Pitesti"].add_neighbour(node_map["Bucharest"], 101)
node_map["Pitesti"].add_neighbour(node_map["Craiova"], 138)

node_map["Rimnicu"].add_neighbour(node_map["Sibiu"], 80)
node_map["Rimnicu"].add_neighbour(node_map["Pitesti"], 97)
node_map["Rimnicu"].add_neighbour(node_map["Craiova"], 146)

node_map["Sibiu"].add_neighbour(node_map["Oradea"], 151)
node_map["Sibiu"].add_neighbour(node_map["Fagaras"], 99)
node_map["Sibiu"].add_neighbour(node_map["Rimnicu"], 80)
node_map["Sibiu"].add_neighbour(node_map["Arad"], 140)

node_map["Timisoara"].add_neighbour(node_map["Arad"], 118)
node_map["Timisoara"].add_neighbour(node_map["Lugoj"], 111)

node_map["Urziceni"].add_neighbour(node_map["Vaslui"], 142)
node_map["Urziceni"].add_neighbour(node_map["Hirsova"], 98)
node_map["Urziceni"].add_neighbour(node_map["Bucharest"], 85)

node_map["Vaslui"].add_neighbour(node_map["Lasi"], 92)
node_map["Vaslui"].add_neighbour(node_map["Urziceni"], 142)

node_map["Zerind"].add_neighbour(node_map["Oradea"], 71)
node_map["Zerind"].add_neighbour(node_map["Arad"], 75)

intial = 'Arad'
destination = 'Bucharest'

# intial_keys = (node_map["Arad"].neighbours)
# print(intial_keys)

# for index,(key,value) in enumerate(intial_keys.items()):
#     print(key,value)

fn = 0
gn = 0
print()

def astar(city,gn):
    connecting_cities = node_map[city].neighbours
    print(city,"-->",end=" ")
    fn_list = []
    # print("N = ",connecting_cities.items())
    
    for i,(key,value) in enumerate(connecting_cities.items()):
        fn_list.append(value+node_map[key].hn)
    
    min = 1000000
    index = 0
    for i,items in enumerate(fn_list):
        if(items < min):
            min = items
            index = i
    
    min_city_name = ""
    min_city_gn = 0
    
    for i,(key,value) in enumerate(connecting_cities.items()):
        if i==index:
            min_city_name = key
            min_city_gn = value
            break
    
    gn = gn + min_city_gn
    
    if(min_city_name == "Bucharest"):
        print("Bucharest")
        print()
        exit()
    else:
        astar(min_city_name,min_city_gn)
    
print("Route : ",end="")
astar(intial,gn)