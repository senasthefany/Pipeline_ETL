#extract, transform and load
import pandas as pd
# import requests
# import json
import openai

# def get_user(id):
#     name_user = df['Name']

openai_api_key = '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'
openai.api_key = openai_api_key

def generate_ai_messages(id):
    semester = dict_df[id]['Semester']
    if semester < 8:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um coordenador de curso de graduação de química."
                },
                {
                    "role": "user",
                    "content": f"Crie uma mensagem personalizada para {dict_df[id]['Name']} com seu nome sobre a época de matrícula e o lembrando de se rematricular (máximo de 200 caracteres)"
                }
            ]
        )
    else:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um coordenador de curso de graduação de química."
                },
                {
                    "role": "user",
                    "content": f"Crie uma mensagem personalizada para {dict_df[id]['Name']} com seu nome o lembrando de marcar a data de formatura parabenizando-o. (máximo de 200 caracteres)"
                }
            ]
        )
    return completion.choices[0].message.content.strip('\"')

def update_user(id):
    if "Message" in dict_df[id]:
        print(f"Update of {dict_df[id]['Name']} was done!")
    else:
        print(f"Update of {dict_df[id]['Name']} was not done!")



df = pd.read_csv('list2.csv', delim_whitespace=True)
user_ids = df['UserId'].tolist()
users = df['Name'].tolist()
dict_df = df.to_dict('index')
# users = [user for id in user_ids if (user := df['Name']) is not None]

for id in user_ids:
    dict_df[id]['Message'] = generate_ai_messages(id)
    update_user(id)
