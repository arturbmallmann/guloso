import mtx
import sys
def main():
    #int(input("vert inicial\n"))
    matrix=mtx.IncMatrix(0,mtx.montarMatriz())
    #somente funciona com incidencia
    print("Size %d" % matrix.size() )
    ord_vertex=[(x, len(matrix.get_arestas(x))) for x in range(0,matrix.size())]
    ord_vertex.sort(key=lambda tupla:tupla[1])
    print([(chr(ord('a')+x),y) for x,y in ord_vertex])
#    while matrix.run():
#        print ("\n") 
if __name__=='__main__':
    main()
