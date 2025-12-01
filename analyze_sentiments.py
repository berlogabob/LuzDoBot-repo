import pandas as pd
# Load the CSV (adjust path if needed)
df = pd.read_csv("data/dataset-balanced.csv")  # , header=None)

# Label column
label_col = "Tipo de Sentimento"

# Counts and percentages
counts = df[label_col].value_counts()
percentages = (counts / len(df) * 100).round(2)

# Create table
result = pd.DataFrame({"Quantity": counts, "Percentage (%)": percentages})
result.loc["Total"] = [len(df), 100.00]

# Display
print(result)
