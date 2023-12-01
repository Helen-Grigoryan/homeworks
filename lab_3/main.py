import random

def generate_matrix(rows, cols):
    matrix_2d = [[random.randint(1,20) for _ in range(cols)] for _ in range(rows)]
    return matrix_2d

def generate_vector(elems):
    vector = [random.randint(1,20) for _ in range(elems)]
    return vector

def multiply_matrix_and_vector(matrix, vector):
    if len(matrix[0]) != len(vector):
        raise Exception("The number of columns of matrix should be equal to the number of elements of vector")
    result = []
    for i in range(len(matrix)):
        sum = 0
        for k in range(len(matrix[0])):
            sum += matrix[i][k] * vector[k]
        result.append(sum)
    return result


matrix = generate_matrix(4,7)
vector1 = generate_vector(10)
vector2 = generate_vector(7)

print("The matrix:")
for row in matrix:
    print(row)

print(f"Vector 1:\n{vector1}")
print(f"Vector2:\n{vector2}")

res = multiply_matrix_and_vector(matrix, vector2)
try:
    txt_file = open("somefile.txt", 'w')
    txt_file.write(f"{res}")
except FileNotFoundError:
    print("Error: The new file could not be created.")


