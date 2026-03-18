# Heart Disease and Failure Data Analysis Project 

This Heart Disease repository contains a data science and analysis project using Decision Trees and Confusion Matrices, K-Means Clustering, and Exploratory Data Analysis
in order to analyze the correlations between certain health markers and heart disease. This project was implemented using Python and SQL.


# Overview
## 1. Heart Dataset
For this project, I used a dataset that was provided by my professor at Oregon State University. The raw dataset was cleaned using Python before analysis.  

Dataset: [heart.csv](CSVs/heart.csv)


## 2. Data Cleaning 
### Process 
- Visualized each variable to identify anomalies and distribution patterns.
- Detected and removed outliers to reduce distortion in the analysis.
- Handled missing values by removing records.

Cleaned Dataset: [heart_cleaned.csv](CSVs/heart_cleaned.csv)

Normalized Dataset: [Mental_Health_Cleaned_Normalized.csv](CSV/Mental_Health_Cleaned_Normalized.csv)

## 3. Decision Tree and Confusion Matrix
### Process
- Split the dataset into training and testing subsets.
- Balanced the training data to improve model performance and reduce class imbalance.
- Separated feature variables and target labels for both training and testing datasets.
- Visualized the distribution of labels in the training and testing sets.
- Tuned model parameters (tree depth, minimum samples per split, and minimum samples per leaf) to optimize predictive performance.
- Trained and visualized the final decision tree model.
- Evaluated model performance using a confusion matrix.

## 4. K-Mmeans Clustering Analysis 
### Process 
- Selected relevant variables from the dataset for clustering analysis
- Visualized the data distribution prior to clustering.
- Experimented with different cluster configurations to determine the most appropriate separation between groups.
- Applied the K-Means clustering algorithm to segment observations into distinct clusters.
- Visualized the final clustered dataset to interpret group patterns.
- Identified and analyzed the centroids representing each cluster.

## 5. Exploratory Data Analysis
### Process
- Wrote SQL queries to analyze single variables in the dataset.
- Wrote SQL queries to analyze multiple variables at once.
- Visualized all query results using Tableau
- Pasted charts from Tableau into a report.

## 6. Technologies and Libraries
### Data Processing
- Python
- Pandas - Data manipulation and preprocessing

### Visualizations
- Seaborn
- Matplotlib
- Tableau
- Visualizations included:
  - Boxplots
  - Heat maps
  - Histograms
  - Scatter Plots
  - Line Graphs
  
### Machine Learning
- Scikit-Learn
  - K-Means Clustering
  - Decision Tree Classifier
  - Confusion Matrix
 
## 6. Project Structure

````markdown
Heart-Disease-and-Failure/
│
├── CSVs/
│   ├── clustertable.csv
│   ├── heart.csv
│   ├── heart_cleaned.csv
│   └── labeltable.csv
│    
├── Python/
│   ├── DataClean.py
│   ├── Decision Tree.py
│   ├── Kmeans.py
│   └── visualizations.py
│
├── Heart Disease Analysis.pdf
└── README.md
````

## 7. Set up
Install required libraries: 
- pip install pandas seaborn matplotlib scikit-learn
- can run sql script for query results locally
  
 
# Results 
- Main driver for Heart Disease prediction is presence of Exercise Angina
- Metabolic markers such as serum cholesterol and fasting blood sugar increases risks in asymptomatic patients. 
