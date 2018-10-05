import mtx
import sys
def main():
    args=[x for x in sys.argv if x.startswith('--')]
    if not args or args[0] == '--help':
        print("[--adj/--inc] file name")
        return
    matrix=mtx.carregaMatriz(args)
    while matrix.run():
        print ("\n") 
if __name__=='__main__':
    main()
