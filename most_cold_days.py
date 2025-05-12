import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo = r'CURITIBA.csv'

archive = pd.read_csv(caminho_arquivo,sep=';', decimal=',')

# elimina dados NaN da coluna Data
archive = archive.dropna(subset=['Data'])

# converte para data a coluna Data
archive['Data'] = pd.to_datetime(archive['Data'])

# converte a coluna Data para o formato DD/MM/AAAA
archive['Data'] = archive['Data'].dt.strftime('%d/%m/%Y')

# converte a coluna TEMPERATURA_MEDIA para number
archive['TEMPERATURA_MEDIA'] = pd.to_numeric(archive['TEMPERATURA_MEDIA'], errors='coerce') 
# coerce converte erros em NaN

# elimina dados NaN da coluna TEMPERATURA_MEDIA
archive = archive.dropna(subset=['TEMPERATURA_MEDIA'])

# agrupando as temperaturas por dia
average = archive.groupby(by='Data')['TEMPERATURA_MEDIA'].mean()

# encontrando os 5 dias mais frios
dias_mais_frios = average.nsmallest(5)

# Tamanho da janela a ser exibida o gráfico
plt.figure(figsize=(10, 6))

# estilo do gráfico
plt.style.use('bmh')

plt.barh(dias_mais_frios.index, dias_mais_frios.values) # barras horizontais

for index, value in enumerate(dias_mais_frios.values):
    plt.text(value, index, f'{value:.2f}', va='center', ha='right', color='white', fontsize=10, fontweight='bold')

plt.xlabel('Temperatura média (ºC)')
plt.ylabel('Data')
plt.title('5 dias mais frios em Curitiba')

# inverter para os dias mais frios aparecerem no topo
plt.gca().invert_yaxis()

plt.show()
