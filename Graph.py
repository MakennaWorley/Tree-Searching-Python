
'''
Demonstration of some simple graph algorithms.
    
@author: Jingsai Liang
'''

import sys

class GraphAlgorithms:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
    
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        for line in graphFile:
            '''
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (firstVertex, secondVertex) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = [ ]

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex].append(secondVertex)
        
        # creates and sort a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        # sort adjacency list for each vertex
        for vertex in self.adjacencyList:
            self.adjacencyList[vertex].sort()

    '''
    Begins the DFS algorithm.
    '''
    def DFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""

    '''
    depth-first traversal of specified graph
    '''
    def DFS(self, method):
        self.DFSInit()
        if method == 'recursive':
            # Your code goes here:
            for vertex in self.vertices:
                if vertex not in self.path:
                    self.DFS_recur(vertex)

            return self.path
        elif method == 'stack':
            # Your code goes here:
            for vertex in self.vertices:
                if vertex not in self.path:
                    self.DFS_stack(vertex)

            return self.path


    def DFS_recur(self,vertex):
        # Your code goes here:
        self.path = self.path + vertex

        for v in self.adjacencyList[vertex]:
            if v not in self.path:
                self.DFS_recur(v)


    def DFS_stack(self, vertex):
        stack=[]
        # Your code goes here:
        stack.append(vertex)

        while stack:
            v = stack.pop()
            if v not in self.path:
                self.path = self.path + v
                for w in self.adjacencyList[v]:
                    if w not in self.path:
                        stack.append(w)


    def BFSInit(self):
        # initially all vertices are considered unknown
        self.unVisitedVertices = list(set(self.vertices))
        # initialize path as an empty string
        self.path = ""
        

    def BFS(self):
        self.BFSInit()
        #queue = []
        # Your code goes here:
        for vertex in self.vertices:
            if vertex not in self.path:
                self.BFS_queue(vertex)

        return self.path


    def BFS_queue(self, vertex):
        queue = []
        self.path = self.path + vertex
        queue.append(vertex)

        while queue:
            vertex = queue.pop(0)
            for v in self.adjacencyList[vertex]:
                if v not in self.path:
                    self.path = self.path + v
                    queue.append(v)


    def hasCycle(self):
        # Your code goes here:
        visited = set()

        for vertex in self.vertices: #check all vertexes
            if vertex not in visited:
                if self.cycle_helper(vertex, None, visited):
                    return True
        return False


    def cycle_helper(self, vertex, parent, visited):
        visited.add(vertex) #add to visited

        for v in self.adjacencyList[vertex]: #for all children of vertex
            if v not in visited: #haven't visited this child
                if self.cycle_helper(v, vertex, visited): #check for the next parent-child relationship
                    return True
            elif v != parent: #cycle is found directly
                return True

                    
    # Work on this function for at most 10 extra points
    def shortestpath(self, p, q):
        # Your code goes here:
        queue = [p]
        visited = set(p)
        pairs = {p: None} #child - parent
        count = 0

        while queue:
            vertex = queue.pop(0)

            if vertex == q: #found the destination
                while vertex is not None: #we can backtrack through the dictionary
                    vertex = pairs[vertex] #find the parent of the vertex
                    count = count + 1
                return count - 1 #path is found to be of length count

            for v in self.adjacencyList[vertex]: #children of vertex
                if v not in visited:
                    visited.add(v)
                    pairs[v] = vertex #add the parent child to the pairs
                    queue.append(v)

        return False #no path found