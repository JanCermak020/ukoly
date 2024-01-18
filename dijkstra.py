
class graf():
 
    def __init__(self, Body):
        self.B = Body
        self.graf = [[0 for slopec in range(Body)]
                      for radek in range(Body)]
 
    def printSolution(self, vzdalenost):
        print("Body \t vzdalenost od zacatku")
        for node in range(self.B):
            print(node, "\t\t", vzdalenost[node])
 
    def minvzdalenost(self, vzdalenost, sptSet):
 
        min = 1e9
 
        for v in range(self.B):
            if vzdalenost[v] < min and sptSet[v] == False:
                min = vzdalenost[v]
                min_index = v
 
        return min_index
    def dijkstra(self, start_bod):
 
        vzdalenost = [1e7] * self.B
        vzdalenost[start_bod] = 0
        sptSet = [False] * self.B
 
        for count in range(self.B):
            u = self.minvzdalenost(vzdalenost, sptSet)
 
            sptSet[u] = True
 
            for v in range(self.B):
                if (self.graf[u][v] > 0 and
                   sptSet[v] == False and
                   vzdalenost[v] > vzdalenost[u] + self.graf[u][v]):
                    vzdalenost[v] = vzdalenost[u] + self.graf[u][v]
 
        self.printSolution(vzdalenost)
 
# Driver program
g = graf(9)
g.graf = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
 
g.dijkstra(5)