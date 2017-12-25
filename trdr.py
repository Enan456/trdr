# http://docs.python-requests.org/en/master/
# https://github.com/ericsomdahl/python-bittrex/blob/master/bittrex/bittrex.py
from bittrex import Bittrex
import time, math, urllib2, json, re,os

TIME = 20
CHECKER = 10

MARGIN_UP = 55
MARGIN_DOWN = 25
API_KEY =  0
SELF = 1
API_SECRET = 0
PATH_COUNTER= 0
#init bitterex download @enan
cwd = os.getcwd()
def initbase():
	Bitterex._init_(SELF,API_KEY,API_SECRET)
	phist= open('phist.txt','w')
	rhist = open('route.txt','w')


def initbitterexdown():
	placeholder = Bitterex.get_currencies()
	for 
	datastore = json.loads(

#from abritarge by ericsomdahl
# Step 1: For each node prepare the destination and predecessor
def initializealgo(graph, source):
    d = {} # Stands for destination
    p = {} # Stands for predecessor
    for node in graph:
        d[node] = float('Inf') # We start admiting that the rest of nodes are very very far
        p[node] = None
    d[source] = 0 # For the source we know how to reach
    return d, p

def relax(node, neighbour, graph, d, p):
    # If the distance between the node and the neighbour is lower than the one I have now
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # Record this lower distance
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node
 
def retrace_negative_loop(p, start):
	arbitrageLoop = [start]
	next_node = start
	while True:
		next_node = p[next_node]
		if next_node not in arbitrageLoop:
			arbitrageLoop.append(next_node)
		else:
			arbitrageLoop.append(next_node)
			arbitrageLoop = arbitrageLoop[arbitrageLoop.index(next_node):]
			return arbitrageLoop


def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1): #Run this until is converges
        for u in graph:
            for v in graph[u]: #For each neighbour of u
                relax(u, v, graph, d, p) #Lets relax it


    # Step 3: check for negative-weight cycles
    for u in graph:
        for v in graph[u]:
        	if d[v] < d[u] + graph[u][v]:
        		return(retrace_negative_loop(p, source))
    return None
#@enan core function
def writer_price(text):
	phist.write(text)

def writer_routes(text):
        rhist.write(text)

def repeater(iterator, i):
	for i in iterator:
		paths = []

		graph = download()

		for key in graph:
	            path = bellman_ford(graph, key)
	            if path not in paths and not None:
		                paths.append(path)

	for path in paths:
		if path == None:
			print("No opportunity here :(")
		else:
	 		money = 100
			pathsToGet[PATH_COUNTER] = "Starting with %(money)i in %(currency)s" % {"money":money,"currency":path[0]}
			PATH_COUNTER += 1
			for i,value in enumerate(path):
				if i+1 < len(path):
					start = path[i]
					end = path[i+1]
					rate = math.exp(-graph[start][end])
					money *= rate
					print "%(start)s to %(end)s at %(rate)f = %(money)f" % {"start":start,"end":end,"rate":rate,"money":money}
					
		print "\n"
def timeExec(interval, duration):
	
