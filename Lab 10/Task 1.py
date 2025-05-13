import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Mall_Customers.csv')

df.info()
df.head()
df.describe()
df.drop('CustomerID', axis=1, inplace=True)
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
sns.heatmap(df.select_dtypes(include="number").corr())
plt.show()

wcss = []
for i in range(1, 11):
  model = KMeans(i, init='k-means++', random_state=727)
  model.fit(df)
  wcss.append(model.inertia_)

sns.lineplot(wcss)
plt.show()

def kmeans(data: np.ndarray | pd.DataFrame, k: int = 5, rs: int = 727):
  model = KMeans(k, init='k-means++', random_state=rs)
  return model.fit_predict(data)

df_ohne_age = df.drop('Age', axis=1)

ss = StandardScaler()
df_scaled = ss.fit_transform(df_ohne_age)

predictions_normal = kmeans(df_ohne_age)
predictions_scaled = kmeans(df_scaled)
def plot_pca(data: np.ndarray | pd.DataFrame, predictions: np.ndarray):
  pca = PCA(n_components=2)
  data_2d = pca.fit_transform(data)

  plt.figure(figsize=(8, 6))
  plt.scatter(data_2d[:, 0], data_2d[:, 1], c=predictions, cmap='viridis', alpha=0.7)
  plt.xlabel("PCA Component 1")
  plt.ylabel("PCA Component 2")
  plt.grid(True)
  plt.show()

plot_pca(df_ohne_age, predictions_normal)
plot_pca(df_scaled, predictions_scaled)

print(silhouette_score(df_ohne_age, predictions_normal))
print(silhouette_score(df_scaled, predictions_scaled))
