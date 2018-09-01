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
        self.actual=first
        self.matrix=matrix
        self.custo=0
        self.visited=[0]*len(matrix)
        self.visited[first]=1
        for i,linha in enumerate(matrix):
            print ("linha %d: %s"%(i,linha))
    def __str__(self):
        return 'teste'
    def visit(self,aresta,custo):
        if (self.visited[aresta]==1):
            return False
        self.visited[aresta]=1
        self.actual=aresta
        self.custo+=custo
        return True
    def get_actual(self):
        return self.actual
    def run(self,*reverse):
        print("Atualmente em %d com custo %d" % (self.actual,self.custo))
        vizinhos=self.get_vizinhos(self.actual)
        print ("vizinhos:")
        for vizinho in vizinhos:
            print("numero %d custo %d" % vizinho)
        while len(vizinhos)>0:
            if reverse:
                v=vizinhos.pop()
            else:
                v=vizinhos.pop(0)
            if self.visit(*v) == True:
                return True
        return False
class IncMatrix(GraphMatrix):
    def __init__(self,*args):
        super(IncMatrix,self).__init__(*args)
    def get_destino(self,aresta):
#        destino=[(i,valor) for i,valor in enumerate(self.matrix)]
#
#        print (self.matrix)
#        vet=[]
#        print("tam %d aresta %d" % (len(self.matrix),aresta))
        for i in range(0,len(self.matrix)):
            linha=self.matrix[i]
            if linha[aresta] != 0 and i!=self.actual:
                return i
#                return (i,linha[aresta])
#            vet+=self.matrix[aresta][i]
            
#        print (vet)
#        result=[(i,valor) for i,valor in enumerate(self.matrix[aresta]) if valor > 0]
#        print(result)
#        return result[0]
    def get_arestas(self,vert):
        arestas=[(i,ar) for i,ar in enumerate(self.matrix[vert]) if ar>0 ]
        return arestas
    def get_vizinhos(self,vert):
        vizinhos=[]
        for aresta in self.get_arestas(vert):
            (a,valor)=aresta
            print("aresta saídas de %d: %d custo %d" %(vert,*aresta))
            vizinhos.append((self.get_destino(a),valor))
        vizinhos.sort(key=lambda tupla:tupla[1])
        return vizinhos 


# get arestas
#        print ("Arestas conectadas a %d:",vert)
#        print (arestas)
#        arestas=list()
#        for ar in self.matrix[vert]:
#            if ar < 0:
#                arestas.append
#        return arestas
#get destino
#        i=0
#        vizinhos=list()
#        for ar in self.matrix:
#            if ar[vert] > 0:
#                vizinhos.append((i,ar[vert]))
#            i+=1

class AdjMatrix(GraphMatrix):
    def __init__(self,*args):
        super(AdjMatrix,self).__init__(*args)
    def get_vizinhos(self,vert):
        vizinhos=[(i,ar) for i,ar in enumerate(self.matrix[vert]) if ar>0 ]
        vizinhos.sort(key=lambda tupla:tupla[1])
        return vizinhos
    
