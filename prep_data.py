from datasets import load_dataset
dataset_name = "ai4bharat/indic-instruct-data-v0.1"
dataset = load_dataset(dataset_name, 'anudesh')
#dataset['hi']


"""text = dataset['hi'][0]['messages']
que = text[0]['content']
res = text[1]['content']
#dt = f"<s>[INST] "+{que}+"[/INST] "{res}+" </s>"
dt = f"<s>[INST] {que} [/INST] {res} </s>"
formated_data = {}
formated_data['text']=dt
text_list = []
text_list.append(formated_data)
print(text_list)"""


text_list = []
for m in dataset['hi']:
  #que = m[i]['messages'][0]['content']
  que = m['messages'][0]['content']
  res = m['messages'][1]['content']
  dt = f"<s>[INST] {que} [/INST] {res} </s>"
  formated_data = {}
  formated_data['text']=dt
  text_list.append(formated_data)


import csv
# Define the filename for the CSV file
csv_filename = 'formatted_data.csv'

# Define the field names for the CSV file
field_names = ['text']

# Write the data to the CSV file
with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    
    # Write the header
    writer.writeheader()
    
    # Write the data
    for item in text_list:
        writer.writerow(item)
