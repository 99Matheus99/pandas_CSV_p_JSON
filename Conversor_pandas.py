import pandas as pd
from time import sleep
try:
    df = pd.read_csv('dados.csv') # abre o arquivo
    print('Arquivo dados.csv encontrado...')
    sleep(1) # espera 1 segundo
    print(f'Processando {len(df)} registros...')
    sleep(1)
    df.to_json('novos_dados.json', orient='records', force_ascii=False, indent=2) # converte de csv para json
    sleep(1)
    print('Arquivo novos_dados.json gerado!')
except FileNotFoundError:
    print('Erro... Arquivo não encontrado!')