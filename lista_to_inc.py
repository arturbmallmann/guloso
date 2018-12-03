#from numpy import matrix

letra = lambda x:chr(ord('a')+x)
num = lambda x:ord(x)-ord('a')
testa= lambda x,y:x if (x > y) else y
def montarLista():
    arestas=list()
    maior=0
    while(True):
        resp = input()
        if not resp:
            return (arestas, maior)
        entrada=[num(x) for x in resp.split(' ') if (x>='a' and x<='~')]
        for x in entrada:
            maior=testa(x,maior)
        print (maior)
        arestas.append(entrada)
def main ():
    (arestas,tamanho)=montarLista()
#    print(arestas)
#    print("tamanho %d" % (tamanho))
    matris=list()
    for a in arestas:
#        print(a)
        linha=[0]*(tamanho+1)
        linha[a[0]]=1
        linha[a[1]]=1
        matris.append(linha)

    for x in range(0,len(matris[0])):
        linha=''
        for y in range(0,len(matris)):
            linha+=chr(ord('0')+matris[y][x])
            linha+=' '
        print (linha)
if __name__ == "__main__":
    main()
