import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load credit scores
df = pd.read_csv("outputs/scores.csv")

# Plot distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["credit_score"], bins=20, kde=True, color="#3B82F6")

plt.title("Credit Score Distribution", fontsize=16)
plt.xlabel("Credit Score", fontsize=12)
plt.ylabel("Number of Wallets", fontsize=12)
plt.grid(True)

# Create outputs folder if not exists
os.makedirs("outputs", exist_ok=True)

# Save plot
plot_path = "outputs/score_distribution.png"
plt.savefig(plot_path)
print(f"[INFO] Plot saved to {plot_path}")
