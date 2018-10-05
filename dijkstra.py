import mtx
import sys
from math import inf
class Dijkstra(mtx.BuscaMatriz):
    show=lambda self:print("Custo: %s\nPai: %s\nFila %s\nAtual: %d" % (self.custo,self.pai,self.fila,self.matrix.get_actual()))
    def __init__(self,matrix):
#        self.matrix=matrix
#        self.custo=[inf]*matrix.size()
#        self.pai=[-1]*matrix.size()
        super(Dijkstra,self).__init__(matrix)
        self.fila=list(range(0,matrix.size()))
        self.fila.remove(self.matrix.get_actual())

#        self.custo[self.matrix.get_actual()]=0
    def explora(self):
        index=self.matrix.get_actual()
        if(self.custo[index]==inf):#caso seja desconexo
            self.custo[index]=0
        for vizinho in self.matrix.get_vizinhos(index):
            (vert,value)=vizinho
            self.show()
            nvalue=value+self.custo[index]
            if nvalue < self.custo[vert]:
                print("Novo valor para %d: %d"%(vert,nvalue))
                self.atualiza(vert,nvalue)
    def gen_fila(self):
        for x in self.fila:
            custo=self.custo[x]
            yield (custo,x)
    def end(self):
        return self.fila==[]
    def atualiza(self,filho,valor):
        self.custo[filho]=valor
        self.pai[filho]=self.matrix.get_actual()
    def choose(self):
        fila=list()
        for a in self.gen_fila():
            fila.append(a)
        fila.sort()
        print("\nFila em ordem de peso: %s"%(fila))
        (peso,actual)=fila.pop(0)
        
        self.matrix.set_actual(actual)
        self.fila.remove(actual)

def main():
    args=[x for x in sys.argv if x.startswith('--')]
    matrix=mtx.carregaMatriz(args)
    
    di=Dijkstra(matrix)
    di.explora()
    while(di.end()==False):
        print("==================================")
        di.explora()
        di.choose()
    di.backtrack(int(input("backtrack:")))
if __name__=='__main__':
    main()
