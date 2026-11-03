import numpy as np
import pandas as pd

np.random.seed(42)

n_samples = 600
n_class = n_samples // 2

ph_0 = np.random.uniform(3.0, 5.0, n_class)
moisture_0 = np.random.uniform(18.0, 32.0, n_class)
temp_0 = np.random.uniform(25.0, 45.0, n_class)
microbial_0 = np.random.uniform(2000, 5500, n_class)
pkg_0 = np.random.uniform(50.0, 75.0, n_class)
label_0 = np.zeros(n_class)

ph_1 = np.random.uniform(6.0, 7.5, n_class)
moisture_1 = np.random.uniform(8.0, 15.0, n_class)
temp_1 = np.random.uniform(2.0, 15.0, n_class)
microbial_1 = np.random.uniform(10, 800, n_class)
pkg_1 = np.random.uniform(80.0, 100.0, n_class)
label_1 = np.ones(n_class)

df = pd.DataFrame(
    {
        "ph_level": np.concatenate([ph_0, ph_1]),
        "moisture_content_pct": np.concatenate([moisture_0, moisture_1]),
        "temperature_celsius": np.concatenate([temp_0, temp_1]),
        "microbial_count_cfu": np.concatenate([microbial_0, microbial_1]),
        "packaging_integrity_score": np.concatenate([pkg_0, pkg_1]),
        "compliance_status": np.concatenate([label_0, label_1]),
    }
)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

file_name = "food_quality_dataset.csv"
df.to_csv(file_name, index=False)

print(f"Dataset successfully generated and saved as '{file_name}'!")
print(f"Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}")
print("\nFirst 5 rows:")
display(df.head())