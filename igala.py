import pandas as pd
import json

# Load your CSV
df = pd.read_csv('clean_2_augmented.csv')

# Create JSONL for fine-tuning
jsonl_data = []
for index, row in df.iterrows():
    jsonl_data.append({
        "prompt": f"Translate the following Igala phrase to English: {row['Igala']}",
        "completion": row['English']
    })
    jsonl_data.append({
        "prompt": f"Translate the following English phrase to Igala: {row['English']}",
        "completion": row['Igala']
    })

# Save as JSONL file
with open('igala_english_fine_tuning_data.jsonl', 'w') as f:
    for entry in jsonl_data:
        f.write(json.dumps(entry) + '\n')
