import snap
import pandas
import numpy as np
import statistics as stats

# snap.back.to.reality::watch.your.profanity::this.is.insanity::our.center.of.gravity::out.the.humanity::bisexuality::so.this.is.what.it.does.and.it.feels.like.the.male.fantasy?::screw.gravity::call.up.sean.annity::for.both.strategies::inside.our.galaxy::oh.we.re.snapping.back.to.reality.oh.there.goes.gravity.MOMS.SPAGHETTIIIIIII



#def degree_ths(p2p, degrees):
#
#   TODO
#

def costant_ths(p2p, degrees):

    thresholds = []


def get_tresholds(p2p, degrees, th_func):

    thresholds = th_func(p2p, degrees)
    
    return thresholds

def get_degrees(p2p):
    nodeI = p2p.BegNI()
    degrees = {}

    degrees.update({nodeI.GetId(): nodeI.GetDeg()})
    while nodeI.Next() < p2p.EndNI():
        degrees.update({nodeI.GetId(): nodeI.GetDeg()})
    
    return degrees

def loadFromFile(p2p, file):

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
    
    print("P2P Graph created correctly.")
    print("Nodes:", p2p.GetNodes(), "Edges:", p2p.GetEdges())

    # Close file
    fIN.close() 

def createP2P():
    # Create P2P undirected graph
    p2p = snap.TUNGraph.New()

    # Load dataset and popolate graph from .txt
    loadFromFile(p2p, './dataset/p2p-Gnutella08.txt')

    # Generate pseudo-random thresholds


    return p2p

# TODO
def TSS(p2p):

    # Variables
    degrees = get_degrees(p2p)
    thresholds = get_tresholds(p2p, degrees, costant_ths)
    print(thresholds)
    S = []







if __name__ == '__main__':

    p2p = createP2P()
    #TSS(p2p)
    