import mtx
import sys
def main():
   args=[x for x in sys.argv if x.startswith('--')]
   matrix=carregaMatriz(args)
def carregaMatriz(args):
    first=int(input('Qual o vertice inicial?'))
    matrix=mtx.montarMatriz()
    if [args[0]=='--adj']:
        print("Matriz de Adjascência")
        return mtx.AdjMatrix(first,matrix)
    else:
        print("Matriz de Incidência")
        return mtx.IncMatrix(first,matrix)
        
if __name__=='__main__':
    main()
