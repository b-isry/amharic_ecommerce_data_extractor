import csv
import random

NUM_SAMPLES = 40
INPUT_CSV = './data/preprocessed_telegram_data.csv'
OUTPUT_TXT = 'conll_labeling.txt'

messages = []
with open(INPUT_CSV, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['Cleaned Message'] and row['Cleaned Message'].strip():
            messages.append(row['Cleaned Message'])

sampled = random.sample(messages, min(NUM_SAMPLES, len(messages)))

total_tokens = 0
with open(OUTPUT_TXT, 'w', encoding='utf-8') as f:
    for msg in sampled:
        tokens = msg.split()
        total_tokens += len(tokens)
        for token in tokens:
            f.write(f"{token}\tO\n")
        f.write("\n")

print(f"Sampled {len(sampled)} messages for manual CoNLL labeling.")
print(f"Total tokens in sampled messages: {total_tokens}")
print(f"Output saved to: {OUTPUT_TXT}")
