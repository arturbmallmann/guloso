#Matriz de Incidência

def montarMatriz():
    matriz=list()
    while True:
        resp = input()
        if not resp:
            return matriz
        matriz.append([int(x) for x in resp.split(' ')])

class GraphMatrix():
    def __init__(self,first,matrix):
        self.first=first
        self.matrix=matrix
    def get_neighbors(self,vert):
        (x,y) = vert
        self.matrix[x][y]
    def __str__(self):
        return 'teste'

class IncMatrix(GraphMatrix):
    def __init__(self,*args):
        super(IncMatrix,self).__init__(*args)
    def get_destino(self,arresta):
        destino=[(i,ar[arresta]) for i,ar in enumerate(self.matrix) if ar[arresta] > 0]
        return destino[0]
#        i=0
#        vizinhos=list()
#        for ar in self.matrix:
#            if ar[vert] > 0:
#                vizinhos.append((i,ar[vert]))
#            i+=1

    def get_arrestas(self,vert):
        arrestas=[(i,ar) for i,ar in enumerate(self.matrix[vert]) if ar<0 ]
#        print ("Arrestas conectadas a %d:",vert)
#        print (arrestas)
        return arrestas
#        arrestas=list()
#        for ar in self.matrix[vert]:
#            if ar < 0:
#                arrestas.append
    def show_vizinhos(self,vert):
        vizinhos=[]
        for arresta in self.get_arrestas(vert):
            (a,valor)=arresta
            vizinhos.append(self.get_destino(a))
        print (vizinhos)
class AdjMatrix(GraphMatrix):
    def __init__(self,*args):
        super(AdjMatrix,self).__init__(*args)
    def show_vizinhos(self,vert):
        vizinhos=[(i,ar) for i,ar in enumerate(self.matrix[vert]) if ar>0 ]
        return vizinhos
    
