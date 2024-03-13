from datasets import load_dataset
dataset_name = "ai4bharat/indic-instruct-data-v0.1"
dataset = load_dataset(dataset_name, 'anudesh')
dataset['hi']
