# Step 1: Install Required Libraries (uncomment if needed)
# !pip install pandas numpy matplotlib seaborn scikit-learn --quiet

# Step 2: Import Libraries
import pandas as pd
import numpy as np
import re
from sklearn.impute import SimpleImputer

# Step 3: Load Dataset
data_path = "C:/Users/unnat/Downloads/sample_hospital_beds.csv"  # Update if needed
df = pd.read_csv(data_path)

# Step 4: Original Data Copy
original_df = df.copy()

# Step 5: Dataset Summary
print("\nOriginal Data Preview:")
print(df.head())
print("\nMissing Values:")
print(df.isnull().sum())

# Step 6: Basic Stopwords
basic_stopwords = set([
    'a', 'an', 'the', 'and', 'or', 'if', 'in', 'on', 'at', 'to', 'for', 'of', 'by', 
    'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',
    'above', 'below', 'from', 'up', 'down', 'out', 'off', 'over', 'under', 'again', 'further',
    'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
    'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only',
    'own', 'same', 'so', 'than', 'too', 'very', 'can', 'will', 'just', 'don', 'should', 'now'
])

# Step 7: Basic Text Cleaning
def clean_text_basic(text):
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r'[^a-z ]', ' ', text)
        tokens = text.split()
        filtered_tokens = [word for word in tokens if word not in basic_stopwords]
        return ' '.join(filtered_tokens)
    return text

# Step 8: Apply Text Cleaning
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].apply(clean_text_basic)

# Step 9: Impute Missing Numeric Values
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
imputer = SimpleImputer(strategy='mean')
df[num_cols] = imputer.fit_transform(df[num_cols])

# Step 9.1: Show Cleaned Dataset Preview
print("\nCleaned Dataset Preview (First 5 rows):")
print(df.head())