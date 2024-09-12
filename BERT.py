from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-cased")


# now you can encode
text = 'A quick brown fox jumps over' # Just a dummy text
model_inputs = tokenizer.encode_plus(text)
