import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
  'vehicle_serial_no': [5, 3, 8, 2, 4, 7, 6, 10, 1, 9],
  'mileage': [150000, 120000, 250000, 80000, 100000, 220000, 180000, 300000, 75000, 280000],
  'fuel_efficiency': [15, 18, 10, 22, 20, 12, 16, 8, 24, 9],
  'maintenance_cost': [5000, 4000, 7000, 2000, 3000, 6500, 5500, 8000, 1500, 7500],
  'vehicle_type': ['SUV', 'Sedan', 'Truck', 'Hatchback', 'Sedan', 'Truck', 'SUV', 'Truck', 'Hatchback', 'SUV']
})
df_ohne_vt = df.drop('vehicle_type', axis=1)

ss = StandardScaler()
df_scaled = ss.fit_transform(df_ohne_vt.copy())
wcss = []
random_state = 727

for i in range(1, 11):
  model = KMeans(i, init='k-means++', random_state=random_state)
  model.fit(df_ohne_vt)
  wcss.append(model.inertia_)

sns.lineplot(x=range(1, 11), y=wcss)
plt.show()

predictions_normal = kmeans(df_ohne_vt, k=4, rs=random_state)
predictions_scaled = kmeans(df_scaled, k=4, rs=random_state)
print(silhouette_score(df_ohne_vt, predictions_normal))
print(silhouette_score(df_scaled, predictions_scaled))
