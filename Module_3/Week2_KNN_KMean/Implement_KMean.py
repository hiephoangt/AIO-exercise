from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt

iris_dataset = load_iris()
data = iris_dataset.data
data = iris_dataset.data[:, 0:2]

#Plot data
plt.scatter(data[:, 0], data[:, 1],c='blue')
plt.title('Iris Dataset')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

class KMeans:
    def __init__(self, k=3, max_iters=100):
        self.k = k                   # Số cụm
        self.max_iters = max_iters   # Số vòng lặp tối đa
        self.centroids = None        # Tọa độ tâm cụm
        self.clusters = None         # Cụm của từng điểm dữ liệu

    def initialize_centroids(self, data):
        """
        Khởi tạo ngẫu nhiên tâm cụm
        Parameters:
            data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
        Return:
            None
        """
        np.random.seed(42)
        self.centroids = data[np.random.choice(data.shape[0], self.k, replace=False)]

    def euclidean_distance(self, x1, x2):
        """
        Tính khoảng cách Euclid giữa hai điểm dữ liệu
        Parameters:
            x1 (numpy.ndarray): điểm dữ liệu 1
            x2 (numpy.ndarray): điểm dữ liệu 2
        Return:
            float: khoảng cách Euclid
        """
        return np.sqrt(np.sum(np.power(x1 - x2, 2)))

    def assign_clusters(self, data):
        """
        Phân cụm dữ liệu
        Parameters:
            data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
        Return:
            numpy.ndarray: mảng chứa cluster của từng điểm dữ liệu
        """

        # Tính toán khoảng cách giữa mỗi điểm dữ liệu (data point) và tâm (centroids) bằng cách sử dụng hàm euclidean_distance
        distances = np.array([[self.euclidean_distance(x, centroid) for centroid in self.centroids] for x in data])

        # print(np.argmin(distances, axis=1)) # Có thể in ra dòng này để thấy cách biểu diễn mảng chứa allocation
        return np.argmin(distances, axis=1)

    def update_centroids(self, data):
        """
        Cập nhật tâm cụm
        Parameters:
            data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
        Return:
            numpy.ndarray: mảng chứa tâm cụm mới
        """
        return np.array([data[self.clusters == i].mean(axis=0) for i in range(self.k)])

    def fit(self, data):
        """
        Hàm huấn luyện
        Parameters:
            data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
        Return:
            None
        """
        # Gọi tới phương thức khởi tạo ngẫu nhiên tâm cụm
        self.initialize_centroids(data)
        self.plot_clusters(data, 0)

        for i in range(self.max_iters):
            # Gán cụm cho các data point gần nhất
            self.clusters = self.assign_clusters(data)

            # Visualize các cụm và tâm cụm tại iteration này
            self.plot_clusters(data, i)

            # Dựa vào các data point của từng cụm, dịch chuyển tâm cụm tới vị trí trung tâm (tính mean) của cụm
            new_centroids = self.update_centroids(data)

            # Nếu tâm cụm không di chuyển, dừng lại
            if np.all(self.centroids == new_centroids):
                break

            # Nếu tâm cụm có di chuyển, thực hiện lại vòng lặp với các giá trị tâm cụm mới
            self.centroids = new_centroids
            self.plot_clusters(data, i)

        # Plot kết quả cuối cùng của các cụm, tâm cụm
        self.plot_final_clusters(data)


    def plot_clusters(self, data, iteration):
        """
        Vẽ các cụm và tâm cụm tại mỗi iteration
        Parameters:
            data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
            iteration (int): iteration hiện tại
        Return:
            None
        """
        plt.scatter(data[:, 0], data[:, 1], c=self.clusters, cmap='viridis', marker='o', alpha=0.6)
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], s=300, c='red', marker='x')
        plt.title(f"Iteration {iteration + 1}")
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.show()

    def plot_final_clusters(self, data):
        """
        Vẽ các cụm và tâm cụm cuối cùng
        Parameters:
            data (numpy.ndarray): dữ liệu đầu vào cần phân cụm
        Return:
            None
        """
        plt.scatter(data[:, 0], data[:, 1], c=self.clusters, cmap='viridis', marker='o', alpha=0.6)
        plt.scatter(self.centroids[:, 0], self.centroids[:, 1], s=300, c='red', marker='x')
        plt.title("Final Clusters and Centroids")
        plt.xlabel('Sepal length')
        plt.ylabel('Sepal width')
        plt.show()

kmeans = KMeans(k=2)
kmeans.fit(data)