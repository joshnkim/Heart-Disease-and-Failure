import pandas as pd

# read in csv file
data = pd.read_csv('/Users/jush/Desktop/Heart Disease/heart.csv')
df = pd.DataFrame(data)
print("Original Dataset State: \n", df, "\n")

# clean cholesterol field 
df = df.loc[df['Cholesterol'] != 0]
print("Cleaned cholesterol field: \n", df, "\n")

# clean resting bp
df = df.loc[df['RestingBP'] != 0]
print("Cleaned resting bp field: \n", df) # no change in row number, cleaning cholesterol field took care of this field as well. 

# clean negative old peak values 

# print out to csv
df.to_csv('/Users/jush/Desktop/Heart Disease/heart_cleaned.csv')
print("DataFrame successfully exported to csv...")

