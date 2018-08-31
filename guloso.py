import mtx
import sys
def main():
    args=[x for x in sys.argv if x.startswith('--')]
    if not args or args[0] == '--help':
        print("[--adj/--inc] file name")
        return
    matrix=carregaMatriz(args)
    while matrix.run():
        print ("\n") 
def carregaMatriz(args):
    print(args)
    first=int(input('Qual o vertice inicial?'))
    matrix=mtx.montarMatriz()
    if args[0]=='--adj':
        print("Matriz de Adjascência")
        return mtx.AdjMatrix(first,matrix)
    elif args[0]=='--inc':
        print("Matriz de Incidência")
        return mtx.IncMatrix(first,matrix)
if __name__=='__main__':
    main()
