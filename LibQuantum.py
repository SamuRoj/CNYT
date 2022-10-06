import Matrix_Lib as Ml
import Complex_Lib as Cl
import matplotlib.pyplot as plt


def RoundDecimal(matrix):
    result = list(Ml.To_List(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(2):
                result[i][j][k] = round(result[i][j][k], 5)
    return result


# Múltiples rendijas cuántico
def DoubleSlits(matrix, vector, slits, target, clicks):
    result = [[0 for _ in range(slits + target + 1)] for _ in range(slits + target + 1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][j]
    for _ in range(clicks - 1):
        result = Ml.Matrix_Product(result, matrix)
    result = list(Ml.To_List(result))
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j][0], result[i][j][1] = (Cl.Module(result[i][j]))**2, 0
    result = Ml.Matrix_Action(result, vector)
    result = list(map(list, result))
    for i in range(len(result)):
        result[i][0], result[i][1] = round(result[i][0], 5), round(result[i][1], 5)
    return tuple(map(tuple, result))

def BarGraph(vector):
    vector = list(map(list, vector))
    for i in range(len(vector)):
        vector[i] = vector[i][0]
    fig, axis = plt.subplots()
    axis.bar(range(len(vector)), vector, 0.5)
    axis.set_title("Simulación del experimento de la doble rendija")
    axis.set_ylabel("Probabilidad")
    axis.set_xlabel("Posición del vector")
    plt.show()


# Variables a usar para las pruebas
v1 = ((1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
m1 = (((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
        ((1/(2**(1/2)), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
        ((1/(2**(1/2)), 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
        ((0, 0), (-1/(6**(1/2)), 1/(6**(1/2))), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0)),\
        ((0, 0), (-1/(6**(1/2)), -1/(6**(1/2))), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 0)),\
        ((0, 0), (1/(6**(1/2)), -1/(6**(1/2))), (-1/(6**(1/2)), 1/(6**(1/2))), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0)),\
        ((0, 0), (0, 0), (-1/(6**(1/2)), -1/(6**(1/2))), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0)),\
        ((0, 0), (0, 0), (1/(6**(1/2)), -1/(6**(1/2))), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0)))
        
    
print("Simulación del experimento de la doble rendija")
Ml.print_matrix(RoundDecimal(m1))
print()
print("Vector de probabilidades luego de la acción de la matriz")
Ml.print_vector(DoubleSlits(m1, v1, 2, 5, 3))
print()
print("En la posición 5 del vector se logra observar el fenómeno de interferencia.")
BarGraph(DoubleSlits(m1, v1, 2, 5, 3))
