import random

bins = range(10)
items = range(500)
values = items*2
iterations = 10000
e = 0.6

class Node(object):
    def __init__(self, id, bin):
        self.id = id
        self.bin = bin
        self.edges = []

class Edge(object):
    def __init__(self, fromNode, toNode):
        self.id = id
        self.fromNode = fromNode
        self.toNode = toNode
        self.pheromone = random.random()

class Graph(object):
    def __init__(self, bins):
        self.startNode = Node(0, -1)
        self.endNode = Node(bins*value+1, -1)
        self.bins = bins
        self.values = random.random()
        self.nodes = []
        self.edges = []
        self.nodes[0] = self.startNode
        self.nodes[bins*value+2] = self.endNode
        self.nodes[b] = [Node(id, bin) for id, bin in bins]
        self.startNode.edges.append(Edge(self.startNode, self.nodes[b]))
        for v in range(bins+1, value*bins+1):
            for n in bins:
                self.nodes[n+v] = Node(n+v, n+1)
                for x in bins:
                    self.nodes[v-bins+n].edges.append(Edge(nodes[v-bins+n], nodes[v+x]))
            v+=bins
        for e in range(value-bins+1, value+1):
            self.endNode.edges.append(Edge(nodes[e], endNode))

class Ant(object):
    def __init__(self):
        self.antPath = []
    def nextStep():
        # for path in paths:
        #     antPath.append(edge.toNode.id)
        thisNode = this.node #PRETYY sure this won't work
        for edge in thisNode.edges:
            den = sum(thisNode.edges.pheromone) #denominator
            rand = random.random() * den #random number between 0 and sum of edges
            num = edge.pheromone #numerator
            nextEdges = []
            nextEdges.append(edge.pheromone)
            for i in len(nextEdges):
                if 0<rand<nextEdges[0]:
                    nextEdge = nextEdges[0]
                    break
                if nextEdges[i]<rand<nextEdges[i+1]:
                    nextEdge = nextEdges[i+1]
                    break

def generatePaths():
    paths = []
    fits = []
    for i in range(p): #number of paths
        ant = Ant()
        while not ant.antPath and not ant.antPath[-1]==graph.endNode: #up to the last node generate nextStep
            i.append(ant.nextStep())
        fitness = max(ant.antPath) - min(ant.antPath)
        fits.append(fitness)
        paths.append(i)
    return paths

def evaporatePheromone(e, edges):
    for edge in edges:
        edge.pheromone = edge.pheromone * e
    return edges

def main():
    graph = Graph(bins)
    for edge in graph.edges:
        edge.pheromone = random.random()
    while k<iterations:
        paths = generatePaths()
        evaporatePheromone(e, graph.edges)
        for edge in graph.edges:
            for pathNo in range(len(paths)):
                if edge in paths[pathNo]:
                    edge.pheromone = edge.pheromone * 100/fits[pathNo]
        k++



if __name__ == "__main__":
    main()
