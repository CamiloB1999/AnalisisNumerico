import numpy as np

def diagonal_dominante(matriz): 
    diagonales = np.diag(abs(matriz))
    suma_filas = np.sum(abs(matriz), axis=1) - diagonales
    if np.all(diagonales>suma_filas):
        return True
    return False

if __name__ == "__main__":
    #Matriz de coeficientes 
    matriz =np.array([[40., 7., 5.], [20., 7., 50.], [ 5., 90., 7.]])
    dominante = False

    for i in range(len(matriz)):
        for k in range (len(matriz) - 1):
            if(diagonal_dominante(matriz)):
                dominante = True
                print(f'Es dominante')
                break
            else:
                auxiliar = matriz[k]
                matriz[k] = matriz[k+1]
                matriz[k+1] = auxiliar
                print(k)
        if(dominante):
            break

    if(not dominante):
        print('No es dominante')
    
    

        