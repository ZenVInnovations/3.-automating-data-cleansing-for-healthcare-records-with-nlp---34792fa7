import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load original and cleaned datasets
data_path = "C:/Users/unnat/Downloads/sample_hospital_beds.csv"
cleaned_path = "C:/Users/unnat/Downloads/cleaned_sample_hospital_beds.csv"

original_df = pd.read_csv(data_path)
df = pd.read_csv(cleaned_path)

num_cols = df.select_dtypes(include=['float64', 'int64']).columns

# Step 10: KDE Plots (Before vs After)
for col in num_cols:
    plt.figure(figsize=(8, 4))
    sns.kdeplot(data=original_df[col].dropna(), label="Before", color='blue', linestyle="--")
    sns.kdeplot(data=df[col], label="After", color='green')
    plt.title(f'Density Plot for {col}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Step 11: Boxplot Comparison (Before vs After)
for col in num_cols:
    plt.figure(figsize=(6, 4))
    data_combined = pd.DataFrame({
        'Before': original_df[col],
        'After': df[col]
    })
    sns.boxplot(data=data_combined, palette=['skyblue', 'lightgreen'])
    plt.title(f'Boxplot Comparison for {col}')
    plt.grid(True)
    plt.show()

# Step 12: Time Series Line Plot (if TIME column is valid)
if 'TIME' in df.columns and 'Value' in df.columns:
    try:
        plt.figure(figsize=(10, 5))
        plt.plot(original_df['TIME'], original_df['Value'], label='Before', linestyle='--', marker='o', color='blue')
        plt.plot(df['TIME'], df['Value'], label='After', linestyle='-', marker='x', color='green')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Hospital Beds Over Time')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"[Error] Time series plot failed: {e}")

# Step 13: Bar Chart Comparison of First Categorical Column
cat_cols = df.select_dtypes(include='object').columns
if len(cat_cols) > 0:
    col = cat_cols[0]
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    original_counts = original_df[col].value_counts()
    sns.barplot(x=original_counts.index, y=original_counts.values, palette='Blues_r')
    plt.title(f'Original {col}')
    plt.xticks(rotation=45)

    plt.subplot(1, 2, 2)
    cleaned_counts = df[col].value_counts()
    sns.barplot(x=cleaned_counts.index, y=cleaned_counts.values, palette='Greens_r')
    plt.title(f'Cleaned {col}')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()