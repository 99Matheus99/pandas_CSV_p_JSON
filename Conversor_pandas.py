import pandas as pd
df = pd.read_csv('dados.csv')
df.to_json('novos_dados.json', orient='records', force_ascii=False, indent=2)
