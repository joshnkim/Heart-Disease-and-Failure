import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.read_csv('/Users/jush/Desktop/Heart Disease/heart.csv')
df = pd.DataFrame(data)
print(df.columns.to_list())


sns.set_palette(["#5a4fcf"])
sns.boxplot(df['Age'])
plt.title("Age")
plt.show()

sns.set_palette(["#408080"])
sns.histplot(df['Sex'])
plt.title("Sex")
plt.show()

sns.set_palette(["#9d2933"])
sns.histplot(df['ChestPainType'])
plt.title("Chest Pain Type")
plt.show()

sns.set_palette(["#00a86b"])
sns.scatterplot(df['RestingBP'])
plt.title("Resting Blood Pressure")
plt.show()

sns.set_palette(["#191d92"])
sns.boxplot(df['Cholesterol'])
plt.title("Cholesterol")
plt.show()
sns.set_palette(["#191d92"])
sns.scatterplot(df['Cholesterol'])
plt.title("Cholesterol")
plt.show()

sns.set_palette(["#a2c4c9"])
sns.histplot(df['FastingBS'])
plt.title("Fasting Blood Sugar")
plt.show()

sns.set_palette(["#df73ff"])
sns.histplot(df['RestingECG'])
plt.title("Resting ECG Readings")
plt.show()

sns.set_palette(["#5a4fcf"])
sns.boxplot(df['MaxHR'])
plt.title("Max Heart Rate")
plt.show()
sns.set_palette(["#5a4fcf"])
sns.scatterplot(df['MaxHR'])
plt.title("Max Heart Rate")
plt.show()

sns.set_palette(["#408080"])
sns.histplot(df['ExerciseAngina'])
plt.title("Presence of Exercise Angina")
plt.show()

sns.set_palette(["#9d2933"])
sns.boxplot(df['Oldpeak'])
plt.title("Old Peak Readings")
plt.show()
sns.set_palette(["#9d2933"])
sns.scatterplot(df['Oldpeak'])
plt.title("Old Peak Readings")
plt.show()

sns.set_palette(["#00a86b"])
sns.histplot(df['ST_Slope'])
plt.title("ST Slope")
plt.show()

sns.set_palette(["#191d92"])
sns.histplot(df['HeartDisease'])
plt.title("Heart Disease")
plt.show()