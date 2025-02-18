import pandas as pd
import json

# Caminho do arquivo CSV de entrada
input_csv = 'microdados_ed_basica_2023.csv'

# Caminho do arquivo JSON de saída
output_json = 'dados_pb.json'

# Lê o arquivo CSV com o pandas usando codificação ISO-8859-1
print("Lendo o arquivo CSV...")
df = pd.read_csv(input_csv, delimiter=';', encoding='ISO-8859-1')

# Filtra as linhas onde SG_UF é igual a 'PB'
print("Filtrando dados para SG_UF = 'PB'...")
df_pb = df[df['SG_UF'] == 'PB']

# Seleciona apenas as colunas desejadas
colunas_desejadas = ['NO_REGIAO', 'SG_UF', 'NO_MUNICIPIO', 'NO_MESORREGIAO', 'NO_MICRORREGIAO', 'NO_ENTIDADE']
df_pb = df_pb[colunas_desejadas]

# Converte o DataFrame filtrado para uma lista de dicionários
dados_pb = df_pb.to_dict(orient='records')

# Salva os dados filtrados em um arquivo JSON
print("Salvando dados em JSON...")
with open(output_json, mode='w', encoding='ISO-8859-1') as json_file:
    json.dump(dados_pb, json_file, ensure_ascii=False, indent=4)

print(f"Dados filtrados para PB salvos em {output_json}")