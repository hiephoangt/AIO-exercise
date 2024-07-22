import numpy as np


def compute_vector_length(vector):
    return np.linalg.norm(vector)


def compute_dot_product(vector1, vector2):
    return vector1.dot(vector2)


def matrix_multi_vector(matrix, vector):
    return matrix.dot(vector)


def matrix_multi_matrix(matrix1, matrix2):
    return matrix1.dot(matrix2)


def inverse_matrix(matrix):
    return np.linalg.inv(matrix)


def compute_eigne(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


def compute_cosine(vector1, vector2):
    cos_sim = compute_dot_product(
        vector1, vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2))
    return cos_sim


if __name__ == '__main__':
    # Question 1:
    vector = np.array([-2, 4, 9, 21])
    result = compute_vector_length([vector])
    print(round(result, 2))

    # Question 2:
    v1 = np. array([0, 1, -1, 2])
    v2 = np. array([2, 5, 1, 0])
    result = compute_dot_product(v1, v2)
    print(round(result, 2))

    # Question 3:
    x = np. array([[1, 2],
                   [3, 4]])
    k = np. array([1, 2])
    print('result \n', x.dot(k))

    # Question 4:
    x = np. array([[-1, 2],
                   [3, -4]])
    k = np. array([1, 2])
    print('result \n', x@k)

    # Question 5:
    m = np. array([[-1, 1, 1], [0, -4, 9]])
    v = np. array([0, 2, 1])
    result = matrix_multi_vector(m, v)
    print(result)

    # Question 6:
    m1 = np. array([[0, 1, 2], [2, -3, 1]])
    m2 = np. array([[1, -3], [6, 1], [0, -1]])
    result = matrix_multi_matrix(m1, m2)
    print(result)

    # Question 7:
    m1 = np.eye(3)
    m2 = np. array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    result = m1@m2
    print(result)

    # Question 8:
    m1 = np.eye(2)
    m1 = np. reshape(m1, (-1, 4))[0]
    m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
    result = m1@m2
    print(result)

    # Question 9:
    m1 = np. array([[1, 2], [3, 4]])
    m1 = np. reshape(m1, (-1, 4), "F")[0]
    m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
    result = m1@m2
    print(result)

    # Question 10:
    m1 = np. array([[-2, 6], [8, -4]])
    result = inverse_matrix(m1)
    print(result)

    # Question 11:
    matrix = np. array([[0.9, 0.2], [0.1, 0.8]])
    eigenvalues, eigenvectors = compute_eigne(matrix)
    print(eigenvectors)

    # Question 12:
    x = np. array([1, 2, 3, 4])
    y = np. array([1, 0, 3, 0])
    result = compute_cosine(x, y)
    print(round(result, 3))
