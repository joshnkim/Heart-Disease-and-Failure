import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv('/Users/jush/Desktop/Heart Disease/heart_cleaned.csv')
df = pd.DataFrame(data)
print(df)

df['Sex'] = df['Sex'].replace({'M': 0, 'F': 1})
df['ExerciseAngina'] = df['ExerciseAngina'].replace({'N':0, 'Y':1})

df = df.drop(columns=['Unnamed: 0', 'RestingECG', 'ST_Slope', 'ChestPainType'], axis=1)

print("Find Columns for K Assignment: \n", df.columns.tolist(), ",\n")

# get columns for Kmeans
x = df[['Age', 'Sex', 
        'RestingBP', 'Cholesterol', 'FastingBS', 
        'MaxHR', 'ExerciseAngina', 
        'Oldpeak']]

# visualize in 3D
chart = plt.figure()
ax = chart.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])
ax.view_init(elev=10, azim=0)
print(ax.get_zlim())
ax.scatter(
    x['Cholesterol'],
    x['FastingBS'],
    x['RestingBP']
)
ax.set_xlabel('Cholesterol')
ax.set_ylabel('FastingBS')
ax.set_zlabel('RestingBP')
plt.title('3D Visualization')
plt.show()
    

# Kmeans with k = 3
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(x)

# labels
labels = kmeans.labels_
print('Cluster Labels K=3: \n', labels, '\n')
print('Centroids K=3: \n', kmeans.cluster_centers_, '\n')

# readable centroids
features = ['Age', 'Sex', 
            'RestingBP', 'Cholesterol', 'FastingBS', 
            'MaxHR', 'ExerciseAngina', 
            'Oldpeak']
cdf = pd.DataFrame(kmeans.cluster_centers_, columns = features)
cdf.index.name = 'Cluster ID'
pd.set_option('display.max_columns', None)
print('Labeled Cluster Centers: \n', cdf, '\n')
cdf.to_csv('/Users/jush/Desktop/Heart Disease/clustertable.csv')



# cluster visualization
chart = plt.figure()
ax = chart.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])
ax.view_init(elev=10, azim=0)
print(ax.get_zlim())
ax.scatter(
    x['Cholesterol'],
    x['FastingBS'],
    x['RestingBP'],
        c=labels,
        cmap='coolwarm'
)
ax.set_xlabel('Cholesterol')
ax.set_ylabel('FastingBS')
ax.set_zlabel('RestingBP')
plt.title('3D Visualization')
plt.show()

