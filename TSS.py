import snap
import pandas
import numpy as np
import statistics as stats
import random

# Ausiliary functions

def copy_graph(graph):
    tmpfile = 'copies/.copy.bin'

    # Saving to tmp file
    FOut = snap.TFOut(tmpfile)
    graph.Save(FOut)
    FOut.Flush()

    # Loading to new graph
    FIn = snap.TFIn(tmpfile)
    graphtype = type(graph)
    new_graph = graphtype.New()
    new_graph = new_graph.Load(FIn)

    return new_graph

def activation_pruning(p2p, probs):

    for edge, prob in probs.items():
        rand = random.random()
        if rand < prob:
            p2p.DelEdge(edge[0], edge[1])

def ths_constant(p2p, degrees):
    ths = {}
    nodeI = p2p.BegNI()
    th = random.randint(0, stats.mean(degrees))

    ths.update({nodeI.GetId() : th})
    while nodeI.Next() < p2p.EndNI():
        ths.update({nodeI.GetId() : th})
    
    return ths

def ths_majority(p2p, degrees):
    ths = {}
    nodeI = p2p.BegNI()
    deg = degrees[nodeI.GetId()]

    ths.update({nodeI.GetId() : deg/2})
    while nodeI.Next() < p2p.EndNI():
        deg = degrees[nodeI.GetId()]
        ths.update({nodeI.GetId() : deg/2})
    
    return ths

def ths_deg(p2p, degrees):
    ths = {}
    nodeI = p2p.BegNI()
    deg = degrees[nodeI.GetId()]

    ths.update({nodeI.GetId() : deg/3})
    while nodeI.Next() < p2p.EndNI():
        deg = degrees[nodeI.GetId()]
        ths.update({nodeI.GetId() : deg/3})
    
    return ths

# Create Graph, computes degrees, sets probs and ths, loading data from file
def createGraphFromFile(file, prob_value, ths_fun):

    # Create P2P undirected graph
    p2p = snap.TUNGraph.New()

    # Variables
    degrees = []
    probs = {}
    ths = {}

    # Open dataset file
    fIN = open(file, 'r')

    for line in fIN.readlines():
        if line[0] == '#':
            continue
        nodes = line.split()
        for node in nodes:
            node = int(node)
            if p2p.IsNode(node):
                continue
            else:
                p2p.AddNode(node)
        p2p.AddEdge(int(nodes[0]), int(nodes[1]))
        probs.update({(int(nodes[0]), int(nodes[1])) : prob_value})
    
    # Activation pruning
    activation_pruning(p2p, probs)

    # Compute degrees
    snap.GetDegSeqV(p2p, degrees)

    # Create thresholds
    ths = ths_fun(p2p, degrees)

    print("P2P Graph created correctly.")
    print("Nodes:", p2p.GetNodes(), "Edges:", p2p.GetEdges())

    # Close file
    fIN.close()

    return (p2p, probs, ths)

# TODO
def TSS(p2p, probs, ths):
    V = [node for node in ths.keys]
    S = []
    neighbors = []

    while len(V) > 0:
        for node in V:
            if ths.get(node) == 0:
                GetNodesAtHop(p2p, node, 1, neighbors, False)
                for neighbor in neighbors:
                    






    return len(S)


def exec(file, exec_number, prob_value, ths_fun):
    results = []
    avg = 0
    
    returns = createGraphFromFile(file, prob_value, ths_fun)
    p2p = returns[0]
    probs = returns[1]
    ths = returns[2]

    temp_p2p = copy_graph(p2p)

    for i in range(exec_number):
        results.append(TSS(temp_p2p, probs, ths))
        temp_p2p = copy_graph(p2p)

    avg = stats.mean(results)

    print("Media:", avg)

if __name__ == '__main__':

    exec('./dataset/p2p-Gnutella08.txt', 10, 0.01, ths_constant)
    