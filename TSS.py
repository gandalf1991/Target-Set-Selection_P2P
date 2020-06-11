import snap
import pandas
import numpy as np
import matplotlib as mpl

# snap.back.to.reality::watch.your.profanity::this.is.insanity::our.center.of.gravity::out.the.humanity::bisexuality::so.this.is.what.it.does.and.it.feels.like.the.male.fantasy?::screw.gravity::call.up.sean.annity::for.both.strategies::inside.our.galaxy::oh.we.re.snapping.back.to.reality.oh.there.goes.gravity.MOMS.SPAGHETTIIIIIII

def loadFromFile(p2p, file):
    # Stats
    nodes_num = 0
    edges_num = 0

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
                nodes_num += 1
        p2p.AddEdge(int(nodes[0]), int(nodes[1]))
        edges_num+=1   
    
    print("P2P Graph created correctly.")
    print("Nodes:", nodes_num, "Edges:", edges_num)

    # Close file
    fIN.close() 

def createP2P():
    # Create P2P undirected graph
    p2p = snap.TUNGraph.New()

    # Load from .txt
    loadFromFile(p2p, './dataset/p2p-Gnutella08.txt')

    return p2p


def TSS(p2p):

    # Variables
    thresholds = [n ]
    degrees = []
    S = []






    return true






if __name__ == '__main__':

    p2p = createP2P()
    TSS(p2p)