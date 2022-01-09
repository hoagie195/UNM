from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from matplotlib import colors as mcolors
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
class KMEAN:
    def __init__(self):
        self.data = [
       [50, 50, 50, 40],
       [50, 50, 30, 60],
       [50, 20, 50, 60],
       [50, 50, 10, 50],
       [40, 30, 30, 30],
       [40, 20, 30, 40],
       [40, 30, 20, 20],
       [40, 25, 30, 40],
    ]
        self.clusters = 3
        super().__init__()
    
    def predict(self):
        km =  KMeans(n_clusters=self.clusters, init='random',
            n_init=10, max_iter=300, tol=1e-04, random_state=0)
        y_km = km.fit_predict(self.data)
        print(km.labels_)
        print(km.inertia_)
        pca = PCA(2)
        pca.fit(self.data)
        pca_data = pca.transform(self.data)
        print(pca_data)
        pca_km = km.fit_predict(pca_data)

        plt.scatter(
        pca_data[y_km == 0, 0], pca_data[y_km == 0, 1],
            s=50, c='lightgreen',
            marker='s', edgecolor='black',
            label='cluster 1'
        )

        plt.scatter(
            pca_data[y_km == 1, 0], pca_data[y_km == 1, 1],
            s=50, c='orange',
            marker='o', edgecolor='black',
            label='cluster 2'
        )

        plt.scatter(
            pca_data[y_km == 2, 0], pca_data[y_km == 2, 1],
            s=50, c='lightblue',
            marker='v', edgecolor='black',
            label='cluster 3'
        )

        # plot the centroids
        plt.scatter(
            km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
            s=250, marker='*',
            c='red', edgecolor='black',
            label='centroids'
        )
        plt.legend(scatterpoints=1)
        plt.grid()
        plt.show()


def main():
    KMEAN().predict()

if __name__ == '__main__':
    main()
