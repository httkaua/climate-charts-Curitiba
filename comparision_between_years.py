import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

caminho_arquivo = r'CURITIBA.csv'

archive = pd.read_csv(caminho_arquivo,sep=';', decimal=',')

# converte a coluna UMIDADE_MEDIA para number
archive['UMIDADE_MEDIA'] = pd.to_numeric(archive['UMIDADE_MEDIA'], errors='coerce')
# coerce converte erros em NaN

# elimina dados NaN da coluna UMIDADE_MEDIA
archive = archive.dropna(subset=['UMIDADE_MEDIA'])

# cada ano presente no arquivo
date_year = archive['date_year'].unique()

#filtrar os dados apenas do mês de julho
dados_julho = archive[(archive['date_month'] == 7) & (archive['date_year'] >= 2014) & (archive['date_year'] <=2024)]

# encontrar a cada ano a umidade média de julho
for date_year in archive:
    moisture_july = dados_julho.groupby(by='date_year')['UMIDADE_MEDIA'].mean()

plt.figure(figsize=(10, 6))

# estilo do gráfico
plt.style.use('bmh')

#plt.plot(temp_july)
plt.plot(moisture_july, linestyle='--', marker='o')

#estilização
plt.ylabel('Umidade relativa do ar')
plt.xlabel('Ano')
plt.title('Umidade do ar em Curitiba no mês de julho - Últimos 10 anos')

# definindo os marcadores do eixo X ano a ano
plt.xticks(np.arange(min(moisture_july.index), max(moisture_july.index)+1, 1))

#definindo os marcadores do eixo Y de 0 a 100
plt.ylim(0, 100)

# formatando os marcadores do eixo Y como porcentagem
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())

plt.show()
