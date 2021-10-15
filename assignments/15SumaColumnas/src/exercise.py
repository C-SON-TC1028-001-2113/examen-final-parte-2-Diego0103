def main():
    matriz = []
    listadesumas=[]
    r = int(input())
    c = int(input())
    if c<=0:
        print('Error')
    else:
        for i in range(r):
            lista = []
            matriz.append(lista)
            for j in range(c):
                valor = int(input())
                matriz[i].append(valor)
    
        for i in range(c):
            suma=0
            for j in range(r):
                suma=matriz[j][i]+suma
            listadesumas.append(suma)
        print(listadesumas)


if __name__=='__main__':
    main()
