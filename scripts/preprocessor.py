import os
import pandas as pd
import re

RAW_PATH = "data/telegram_data.csv"
OUTPUT_PATH = "data/preprocessed_telegram_data.csv"

def clean_text(text):
    if pd.isna(text) or text.strip() == "":
        return None
    # Remove Telegram links, phone numbers, emojis, unwanted characters
    text = re.sub(r"http\S+|www\S+|t.me\S+", "", text)  # remove links
    text = re.sub(r"[^\w\s፣።፤፥፦፡፠መሃል]+", "", text)  # remove emojis & Latin punctuations
    text = re.sub(r"\s+", " ", text)  # collapse whitespace
    return text.strip()

def preprocess_telegram_data():
    df = pd.read_csv(RAW_PATH)
    print("Columns in CSV:", df.columns)  # debug line

    # Use the correct column name for messages
    message_col = "Original Message"  # adjust if needed

    df.drop_duplicates(subset=[message_col], inplace=True)
    df[message_col] = df[message_col].apply(clean_text)
    df.dropna(subset=[message_col], inplace=True)
    df = df[df[message_col].str.len() > 10]  

    df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
    print(f"Preprocessed data saved to {OUTPUT_PATH}")

    
if __name__ == "__main__":
    if not os.path.exists(RAW_PATH):
        print(f"Input file {RAW_PATH} does not exist.")
    else:
        preprocess_telegram_data()
        print("Preprocessing complete.")