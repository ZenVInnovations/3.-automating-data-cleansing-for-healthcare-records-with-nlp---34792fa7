import pandas as pd

# Assuming `df` already contains cleaned data
data_path = "C:/Users/unnat/Downloads/sample_hospital_beds.csv"
df = pd.read_csv(data_path)

# Save the cleaned data
cleaned_path = "C:/Users/unnat/Downloads/cleaned_sample_hospital_beds.csv"
df.to_csv(cleaned_path, index=False)
print(f"\n✅ Cleaned data saved to: {cleaned_path}")