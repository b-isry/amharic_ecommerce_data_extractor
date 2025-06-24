# Amharic E-commerce Data Extractor

This project is designed to extract, preprocess, and prepare Amharic e-commerce data for manual annotation, particularly for Named Entity Recognition (NER) tasks using the CoNLL format.

## Project Structure

- `scripts/extract_sample_for_labeling.py`: Script to sample messages and prepare them for manual CoNLL labeling.
- `data/`: Contains raw and preprocessed CSV data files.
  - `preprocessed_telegram_data.csv`: The main input file for the script (must contain a column with cleaned Amharic messages).
  - `telegram_data.csv`: Raw data (not directly used by the script).
- `conll_labeling.txt`: Output file containing sampled messages in CoNLL format for manual labeling.
- `photos/`: Contains image files, possibly related to the e-commerce data.
- `requirements.txt`: Python dependencies.

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

To generate a sample for manual CoNLL labeling:

```bash
python scripts/extract_sample_for_labeling.py
```

This will:

- Read messages from `data/preprocessed_telegram_data.csv` (expects a column named `Cleaned Message`).

- Randomly sample 40 messages.
- Tokenize each message and write tokens (one per line) to `conll_labeling.txt`, with a default label `O`.
- Separate messages with a blank line.

Example output in `conll_labeling.txt`:

```
አዲስ	O
ምርት	O
...

ቤት	O
ዋጋ	O

...
```

## Notes

- The script expects the input CSV to be UTF-8 encoded and to contain a column named `Cleaned Message`.
- You can adjust the number of samples by changing the `NUM_SAMPLES` variable in the script.
- The output file is overwritten each time the script is run.

