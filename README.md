# BERT Tokenizer Example

This repository contains a simple example of how to use the **BERT tokenizer** from Hugging Face's transformers library.

## Code Overview
```python
from transformers import BertTokenizer

# Load the BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-cased")

# Example text for tokenization
text = 'A quick brown fox jumps over'

# Encode the text
model_inputs = tokenizer.encode_plus(text)
