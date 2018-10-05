import mtx
import sys
from math import inf
class largura():
    show=lambda self:print("Custo: %s\nPai: %s\nCor: %s\nAtual: %d" % (self.custo,self.pai,self.cor,self.matrix.get_actual()))
    def __init__(self,matrix):
        self.matrix=matrix
        self.custo=[inf]*matrix.size()
        self.pai=[-1]*matrix.size()
        self.cor=['w']*matrix.size()
    def explora(self,index):
        self.matrix.set_actual(index)#só para contagem
        self.show()
        explorar=list()
        if(self.custo[index]==inf):
            self.custo[index]=0
        for vizinho in self.matrix.get_vizinhos(index):
            (vert,value)=vizinho
            nvalue=self.custo[index]+1
            if self.cor[vert]=='w':
                print("Novo valor para %d: %d"%(vert,nvalue))
                self.atualiza(vert,nvalue)
                explorar+=[vert]
                self.cor[vert]='g'
        self.cor[index]='b'
        print(explorar)
        return explorar
    def atualiza(self,filho,valor):
        self.custo[filho]=valor
        self.pai[filho]=self.matrix.get_actual()
def main():
    args=[x for x in sys.argv if x.startswith('--')]
    matrix=mtx.carregaMatriz(args)
    
    lar=largura(matrix)
    explorar=[matrix.get_actual()]
    while(explorar!=[]):
        print("==================================")
        aux=list()
        for i in explorar:
            aux+=lar.explora(i)
        print("explorar: %s"%(aux))
        explorar=aux
    lar.show()
if __name__=='__main__':
    main()
