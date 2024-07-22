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

def compute_cosine(vector1,vector2):
    cos_sim = compute_dot_product(vector1,vector2)/np.linalg.norm(vector1)*np.linalg.norm(vector2)
    return cos_sim
