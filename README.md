# project-template
# Automating Data Cleansing for Healthcare Records with NLP

This project aims to streamline and automate the process of cleaning healthcare-related datasets, particularly hospital bed records, using Python and basic NLP (Natural Language Processing) techniques.

## Overview

Healthcare datasets often contain inconsistencies, missing values, and textual noise that must be addressed before performing analysis. This project implements an end-to-end pipeline that:

- Cleans text data using regex and basic stopwords
- Handles missing values in numerical columns
- Visualizes the effects of data cleaning using plots
- Prepares the dataset for downstream use

## Folder Structure

```
healthcare_data_cleaning/
│
├── 1_data_cleaning.py         # Loads, cleans text, imputes missing values
├── 2_visualization.py         # KDE plots, boxplots, time series and categorical visualizations
├── 3_save_and_export.py       # Saves cleaned CSV file
├── README.md                  # Detailed project documentation
```

## Requirements

Ensure the following libraries are installed:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Install with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

## Usage

1. Update the `data_path` in the scripts to point to your CSV file.
2. Run each script in order:
   - `1_data_cleaning.py`
   - `2_visualization.py`
   - `3_save_and_export.py`

The cleaned file will be saved to the specified path.

## Author

Unnathi — 2025
