from datasets import load_dataset
dataset_name = "ai4bharat/indic-instruct-data-v0.1"
dataset = load_dataset(dataset_name, 'anudesh')
#dataset['hi']


text = dataset['hi'][0]['messages']
que = text[0]['content']
res = text[1]['content']
#dt = f"<s>[INST] "+{que}+"[/INST] "{res}+" </s>"
dt = f"<s>[INST] {que} [/INST] {res} </s>"
formated_data = {}
formated_data['text']=dt
text_list = []
text_list.append(formated_data)
print(text_list)
