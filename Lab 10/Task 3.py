import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import seaborn as sns
import matplotlib.pyplot as plt

random_state = 727

np.random.seed(random_state)

cap = np.vectorize(lambda v: min(4, max(0, v)))

S, M, L = np.floor([N * 0.2, N * 0.3, N * 0.5]).astype(int)

data = {
  'student_id': range(1, S + M + L + 1),
  'GPA': cap(np.round(np.concatenate([
    np.random.normal(3.7, 0.2, M),
    np.random.normal(2.8, 0.3, L),
    np.random.normal(1.9, 0.2, S)
  ]), 2)),
  'study_hours': np.concatenate([
    np.random.randint(12, 20, M),
    np.random.randint(6, 12, L),
    np.random.randint(1, 6, S)
  ]),
  'attendance_rate': np.concatenate([
    np.random.randint(90, 100, M),
    np.random.randint(70, 90, L),
    np.random.randint(40, 70, S)
  ])
}

df = pd.DataFrame(data)

df.info()
df.head()

df.describe()
df_original = df.copy()
df.drop('student_id', axis=1, inplace=True)
sns.heatmap(df.corr())
plt.show()

ss = StandardScaler()
df_scaled = ss.fit_transform(df)
wcss = []
for i in range(2, 7):
  model = KMeans(i, init='k-means++', random_state=random_state)
  model.fit(df_scaled)
  wcss.append(model.inertia_)

sns.lineplot(x=range(2,7), y=wcss)
plt.show()

model = KMeans(3, init='k-means++', random_state=random_state)
predictions = model.fit_predict(df_scaled)

df['clusters'] = predictions
plt.scatter(x=df['GPA'], y=df['study_hours'], c=df['clusters'], cmap='viridis', label=df['clusters'].unique())
plt.xlabel('GPA')
plt.ylabel('Study Hours')
plt.show()

# Scatter plot presented

df_original['clusters'] = df['clusters']

values = df_original.values
np.random.shuffle(values)
pd.DataFrame(data=values, columns=df_original.columns).head(10
