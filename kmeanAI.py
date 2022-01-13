from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from matplotlib import colors as mcolors
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
class KMEAN:
    def __init__(self):
        self.data = pd.read_csv("kddcup99_csvnew.csv", encoding='utf-8')
        self.clusters = 7
        super().__init__()
    
    def predict(self):
        km =  KMeans(n_clusters=self.clusters, init='random',
            n_init=10, max_iter=300, tol=1e-04, random_state=0)
        y_km = km.fit_predict(self.data)
        print(km.labels_)
        print(km.inertia_)
        pca = PCA(3)
        pca.fit(self.data)
        pca_data = pd.DataFrame(pca.transform(self.data))
        print(pca_data.head())
        pca_km = km.fit_predict(pca_data)

def main():
    KMEAN().predict()

if __name__ == '__main__':
    main()
