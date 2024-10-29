import pandas as pd

caminhoDoc = 'viagens/2024_Viagem.csv'

df_viagens = pd.read_csv(caminhoDoc, encoding="Windows-1252", sep=";" )    

pd.set_option('display.max_columns', None)



colunas = df_viagens["Valor díarias","Nome"]

print(df_viagens[colunas])