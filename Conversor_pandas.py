import pandas as pd
chaves = ['Nome', 'Idade', 'Cidade', 'Email', 'CPF',]
df = pd.read_csv('dados.csv')
df.to_json('novos_dados.json', orient='records', force_ascii=False)
