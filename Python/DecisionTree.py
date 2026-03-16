from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

from sklearn.model_selection import train_test_split
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans

# read in data
data = pd.read_csv('/Users/jush/Desktop/Heart Disease/heart_cleaned.csv')
df = pd.DataFrame(data)

df['Sex'] = df['Sex'].replace({'M': 0, 'F': 1})
df['ExerciseAngina'] = df['ExerciseAngina'].replace({'N':0, 'Y':1})

df = df.drop(columns=['Unnamed: 0', 'RestingECG', 'ST_Slope', 'ChestPainType'], axis=1)

print(df)

# splitting
training, testing = train_test_split(df, test_size=0.2, random_state=42)
print('\nThe training Data is: ', training, '\n')
print('The testing data is: \n', testing, '\n')

# balance training set
counts = training['HeartDisease'].value_counts()
print('Label counts: \n', counts, '\n')
minority = counts.min()

# create sep df's for each class
c0 = training[training['HeartDisease'] == 0]
c1 = training[training['HeartDisease'] == 1]

c0under = c0.sample(minority, random_state=42)
c1under = c1.sample(minority, random_state=42)
balanced_train = pd.concat([c0under, c1under])
balanced_train = balanced_train.sample(frac=1, random_state=42)

print('Balanced data counts: \n', balanced_train['HeartDisease'].value_counts())

# remove but retain labels
train_label = balanced_train['HeartDisease']
balanced_train = balanced_train.drop(['HeartDisease'], axis=1)

test_label = testing['HeartDisease']
testing = testing.drop(['HeartDisease'], axis=1)

print('Training Labels: \n', train_label, '\n')
print('Training set: \n', training, '\n')
print('Testing labels: \n', test_label, '\n')
print('Testing set: \n', testing, '\n')

# visualization for data
train_label_count = train_label.value_counts()
print("Train Label Counts: \n", train_label_count, "\n")
sns.barplot(x = train_label_count.index, y = train_label_count.values, palette=["#8fbec0", "#c48a8f", "#b6a9b8"])
plt.title('Training Labels')
plt.xlabel('Performance')
plt.ylabel('Count')
plt.show()

test_label_count = test_label.value_counts()
print("Train Label Counts: \n", test_label_count, "\n")
sns.barplot(x = test_label_count.index, y = test_label_count.values, palette=["#8fbec0", "#c48a8f", "#b6a9b8"])
plt.title('Testing Labels')
plt.xlabel('Performance')
plt.ylabel('Count')
plt.show()



# start tree creation
custom_weights = {0: 1, 1: 3}

myDT_Classifier = DecisionTreeClassifier(
    max_depth = 5,
    min_samples_split=4,
    min_samples_leaf=5,
    # class_weight='balanced',
    class_weight=custom_weights,
    random_state=42
)

# fit model
myDT_Classifier = myDT_Classifier.fit(balanced_train, train_label)
class_names_str = [str(c) for c in myDT_Classifier.classes_]

# plot
# plot figure
plt.figure(figsize=(8,6), dpi=300)

myPlot = tree.plot_tree(myDT_Classifier,
                        feature_names=balanced_train.columns,
                        class_names=class_names_str,
                        filled=True)
plt.show()


# make predictions
prediction = myDT_Classifier.predict(testing)
print("Prediction for testing set: \n", prediction, "\n")

# prep for confusion matrix
label_names = ['0', '1']
actual_labels = test_label
predicted_labels = prediction

# create confusion matrix
cm = confusion_matrix(actual_labels, predicted_labels)
print("Confusion matrix: \n", cm, "\n")

# visualization via heatmap
sns.heatmap(cm, annot=True,
            cmap = 'Reds',
            xticklabels=label_names, yticklabels=label_names,
            cbar=False)
plt.title("Confusion Matrix for Heart Attack Data", fontsize=20)
plt.xlabel("Predicted", fontsize=15)
plt.ylabel("Actual", fontsize=15)
plt.show()

importances = pd.Series(myDT_Classifier.feature_importances_, index=balanced_train.columns)
print("Order of importance: \n", importances.sort_values(ascending=False), "\n")

# Integrating the confusion matrix elements with the dataset clusters. 
# Kmeans with k = 3
x = df[['Age', 'Sex', 
        'RestingBP', 'Cholesterol', 'FastingBS', 
        'MaxHR', 'ExerciseAngina', 
        'Oldpeak']]

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

df['Cluster ID'] = kmeans.fit_predict(df[features])

# new dataframe 
results_df = testing.copy()
results_df['Actual'] = test_label
results_df['Predicted'] = prediction

results_df['Cluster ID'] = df['Cluster ID']

# helper function for classification
def get_matrix_section(row):
    if row['Actual'] == 1 and row['Predicted'] == 1: return 'True Positive'
    if row['Actual'] == 0 and row['Predicted'] == 0: return 'True Negative'
    if row['Actual'] == 0 and row['Predicted'] == 1: return 'False Positive'
    if row['Actual'] == 1 and row['Predicted'] == 0: return 'False Negative'

# integration
results_df['Matrix_Section'] = results_df.apply(get_matrix_section, axis=1)
cluster_analysis = pd.crosstab(results_df['Cluster ID'], results_df['Matrix_Section'])

# viewing and printing 
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print("Cluster vs. Confusion Matrix Analysis: \n", cluster_analysis, "\n")