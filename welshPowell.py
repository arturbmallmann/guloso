import mtx
import sys
add=lambda x,y: x+y

def main():
    #int(input("vert inicial\n"))
    matrix=mtx.IncMatrix(0,mtx.montarMatriz())
    #somente funciona com incidencia
    print("Size %d" % matrix.size() )
    ord_vertex=[(x, len(matrix.get_arestas(x))) for x in range(0,matrix.size())]
    ord_vertex.sort(key=lambda tupla:tupla[1])
    cores=[0]*matrix.size()
    cor=0
    pintados=[]
    print([(mtx.letra(x),y) for x,y in ord_vertex])
    print(len(pintados))
    while(len(pintados)!=matrix.size()):
        cor+=1
        print("cor %d" % (cor))
        pintados=set([x for x,cores in enumerate(cores) if cores!=0])
        print("pintados %s" % (pintados))
#        ord_vertex=list(set(ord_vertex)-pintados)
        for ll in reversed(ord_vertex):
            (atual,y)=ll
            if(cores[atual]==0):
                matrix.set_actual(atual)
                print("atual %s" % mtx.letra(atual))

                vizinhos=[x for x,y in matrix.get_vizinhos(atual)]
                print("vizinhos: %s" % ([mtx.letra(i) for i in vizinhos]))
                mesmacor=[x for x in vizinhos if cores[x] == cor]
      #          mesmacor=set([x for x in pintados if cores[x] != cor])
                
                #disponiveis, ou seja, se houver um ou mais da cor atual o atual não poderá ser pintado
                print("iguais %s" % (mesmacor))
                if (len(mesmacor)==0):
                   cores[atual]=cor
                   
    #            print("pintados %s" % (pintados))
    #            pintar=pintar - pintados
    #            print("pintar: %s" % ([mtx.letra(i) for i in pintar]))
    #            cor+=1
    #            for i in pintar:
    #                cores[i]=cor
                print("cores:")
                for i in range(0,matrix.size()):
                    print(("%s,%d") % (mtx.letra(i),cores[i]))
#    while matrix.run():
#        print ("\n") 
if __name__=='__main__':
    main()
