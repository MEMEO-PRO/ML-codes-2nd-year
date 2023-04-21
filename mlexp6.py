import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv('car_data.csv')

X = data[['AnnualSalary', 'Age']].values

k = 3
kmeans = KMeans(n_clusters=k)

kmeans.fit(X)


new_data = np.array([[1.0, 2.0], [3.0, 4.0]])
new_labels = kmeans.predict(new_data)

centers = kmeans.cluster_centers_

plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='red', marker='x', s=200, label='Cluster Centers')
plt.scatter(new_data[:, 0], new_data[:, 1], c=new_labels, cmap='viridis', marker='s', label='New Data')
plt.title('K-Means Clustering with Predicted Cluster Centers')
plt.xlabel('Age')
plt.ylabel('AnnualSalary')
plt.legend()
plt.show()
