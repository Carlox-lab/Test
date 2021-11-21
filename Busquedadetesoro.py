from random import randrange

def crearBombsT(s):
    c = 0
    d = 0
    e = 0
    B1x=randrange(s)
    B1y=randrange(s)
    B2x=randrange(s)
    B2y=randrange(s)
    while c==0:
        if ((B1x*10)+B1y)==((B2x*10)+B2y):
            B2x = randrange(s)
            B2y = randrange(s)
        else:
            c+=1
    B3x=randrange(s)
    B3y=randrange(s)
    while d == 0:
        if ((B1x*10) + B1y) == ((B3x*10)+ B3y):
            B3x = randrange(s)
            B3y = randrange(s)
        else:
            if ((B2x*10) + B2y) == ((B3x*10) + B3y):
                B3x = randrange(s)
                B3y = randrange(s)
            else:
                d+=1
    Tx=randrange(s)
    Ty=randrange(s)
    while e == 0:
        if ((B1x*10) + B1y) == ((Tx*10) + Ty):
            Tx = randrange(s)
            Ty = randrange(s)
        else:
            if ((B2x*10) + B2y) == ((Tx*10) + Ty):
                Tx = randrange(s)
                Ty = randrange(s)
            else:
                if ((B3x*10)+B3y) == ((Tx*10) + Ty):
                    Tx = randrange(s)
                    Ty = randrange(s)
                else:
                    e += 1
    if s>=5 and s<10:
        f = 0 
        B4x=randrange(s)
        B4y=randrange(s)
        while f==0:
            if ((B1x * 10) + B1y) == ((B4x * 10) + B4y):
                B4x = randrange(s)
                B4y = randrange(s)
            else:
                if ((B2x * 10) + B2y) == ((B4x * 10) + B4y):
                    B4x = randrange(s)
                    B4y = randrange(s)
                else:
                    if ((B3x * 10) + B3y) == ((B4x * 10) + B4y):
                        B4x = randrange(s)
                        B4y = randrange(s)
                    else:
                        f += 1
        return [B1x,B1y,B2x,B2y,B3x,B3y,Tx,Ty,B4x,B4y]
    if s>=10:
        f = 0
        g = 0 
        B4x=randrange(s)
        B4y=randrange(s)
        while f==0:
            if ((B1x * 10) + B1y) == ((B4x * 10) + B4y):
                B4x = randrange(s)
                B4y = randrange(s)
            else:
                if ((B2x * 10) + B2y) == ((B4x * 10) + B4y):
                    B4x = randrange(s)
                    B4y = randrange(s)
                else:
                    if ((B3x * 10) + B3y) == ((B4x * 10) + B4y):
                        B4x = randrange(s)
                        B4y = randrange(s)
                    else:
                        f += 1
        B5x=randrange(s)
        B5y=randrange(s)
        while g == 0:
            if ((B1x * 10) + B1y) == ((B5x * 10) + B5y):
                B5x = randrange(s)
                B5y = randrange(s)
            else:
                if ((B2x * 10) + B2y) == ((B5x * 10) + B5y):
                    B5x = randrange(s)
                    B5y = randrange(s)
                else:
                    if ((B3x * 10) + B3y) == ((B5x * 10) + B5y):
                        B4x = randrange(s)
                        B4y = randrange(s)
                    else:
                        if ((B4x * 10) + B4y) == ((B5x * 10) + B5y):
                            B4x = randrange(s)
                            B4y = randrange(s)
                        else:
                             g += 1
        return [B1x,B1y,B2x,B2y,B3x,B3y,Tx,Ty,B4x,B4y,B5x,B5y]
    return [B1x,B1y,B2x,B2y,B3x,B3y,Tx,Ty]


def crearTablero(s):
    coord = crearBombsT(s)
    matriz=[]
    for i in range(s):
        matriz.append([i*0]*s)
    matriz[coord[1]][coord[0]]=1
    matriz[coord[3]][coord[2]]=1
    matriz[coord[5]][coord[4]]=1
    matriz[coord[7]][coord[6]]=2
    if s>=5 and s<10:
        matriz[coord[9]][coord[8]]=1
    if s>=10:
        matriz[coord[9]][coord[8]]=1
        matriz[coord[11]][coord[10]]=1
    return matriz 

def jugar1Vez(tablero,s):
    str(input("Para salir del juego no teclee ni Si ni No."))
    test = str(input("Es una prueba? (Si/No):"))
    if test == 'Si':
        print("El siguiente es el tablero con bombas(1) y tesoro(2)")
        for i in tablero:
            print(i)
    else: 
        if test == 'No':
            print('Tablero')
            a = []
            for i in range(s):
                a.append([0] * s)
            for i in a:
                print(i)
        else:
            exit()

    print("El juego ha comenzado")
    jy = int(input("Ingresa la columna en que deseas buscar el tesoro (las columnas empiezan en 0 por lo que tu ranngo es [0,(n-1)], conforme aumenta su valor te mueves hacia abajo):"))
    jx = int(input("Ahora ingresa la fila donde deseas buscar el tesoro (las filas empiezan en 0 por lo que tu ranngo es [0,(n-1)], conforme aumenta su valor te mueves hacia la derecha): "))    
    re = 0
    z = 0
    while re == 0:
        if jy < len(tablero) and jx < len(tablero):
            while z == 0:
                if jy < len(tablero) and jx < len(tablero):
                    if (tablero[jx][jy] == 2):
                        print(f"Has encontrado el tesoro y ganado el juego")
                        z += 1
                        re += 1
                        for i in tablero:
                            print(i)
                    else:
                        if (tablero[jx][jy] == 1):
                            print("Has encontrado una bomba y perdido el juego")
                            z += 1
                            re += 1
                            for i in tablero:
                                print(i)
                        else:
                            print('Genial, no te topaste con nada, si ingresas los mismos valores otra vez el resultado se repetirá.')
                            actualizaTablero(tablero,jx,jy,tamaño_deMatriz)   
                            jy = int(input("Ingresa una columna para buscar:"))
                            jx = int(input("Ahora ingresa una fila para buscar:"))
                else:
                    print("Uno o ambos valores no estan dentro del rango del tablero,lee los parametros con atención e ingresa nuevos valores para poder jugar")
                    jy = int(input(
                        "Ingresa una columna para buscar (las columnas empiezan en 0 por lo que tu ranngo es [0,(n-1)], conforme aumenta su valor te mueves hacia abajo):"))
                    jx = int(input(
                        "Ingresa una fila para buscar (las filas empiezan en 0 por lo que tu ranngo es [0,(n-1)], conforme aumenta su valor te mueves hacia la derecha):"))
        else:
            print("Uno o ambos valores no estan dentro del rango del tablero,lee los parametros con atención e ingresa nuevos valores para poder jugar")

def actualizaTablero(tablero,jx,jy,tamaño_deMatriz):
    a = []
    for i in range(len(tablero)):
        a.append([0]*len(tablero))
    if jx==0:
        if jy==tamaño_deMatriz-1:
            a[jx+1][jy] = tablero[jx+1][jy]
            a[jx][jy-1] = tablero[jx][jy-1]
        else:
            if jy==0:
                a[jx][jy+1] = tablero[jx][jy+1]
                a[jx+1][jy] = tablero[jx+1][jy]
            else:
                a[jx][jy-1] = tablero[jx][jy-1]
                a[jx][jy+1] = tablero[jx][jy+1]
                a[jx+1][jy] = tablero[jx+1][jy]
    else:
        if jx == tamaño_deMatriz-1:
            if jy == 0:
                a[jx][jy+1] = tablero[jx][jy+1]
                a[jx-1][jy] = tablero[jx-1][jy]
            else:
                if jy == tamaño_deMatriz-1:
                    a[jx][jy-1] = tablero[jx][jy-1]
                    a[jx-1][jy] = tablero[jx-1][jy]
                else:
                    a[jx][jy-1] = tablero[jx][jy-1]
                    a[jx][jy+1] = tablero[jx][jy+1]
                    a[jx-1][jy] = tablero[jx-1][jy]    
        else:
            a[jx][jy-1] = tablero[jx][jy-1]
            a[jx-1][jy] = tablero[jx-1][jy]
            a[jx][jy+1] = tablero[jx][jy+1]
            a[jx+1][jy] = tablero[jx+1][jy] 
    for i in a:
        print(i)

tamaño_deMatriz=int(input("ingresa el tamaño del tablero,a partir de 2 (si es 2 es modo DIOS), que deseas (ej. n= tablero de n x n)  :"))
#print(list(range(s)))
if tamaño_deMatriz <2: 
    exit()
else:
    tablero = crearTablero(tamaño_deMatriz)
    jugar1Vez(tablero,tamaño_deMatriz)