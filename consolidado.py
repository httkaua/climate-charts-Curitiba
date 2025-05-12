import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import squarify


####################### GRÁFICO 1
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






####################### GRÁFICO 2

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







####################### GRÁFICO 3

caminho_arquivo = r'CURITIBA.csv'

archive = pd.read_csv(caminho_arquivo,sep=';', decimal=',')

# converte a coluna TEMPERATURA_MEDIA para number
archive['TEMPERATURA_MEDIA'] = pd.to_numeric(archive['TEMPERATURA_MEDIA'], errors='coerce')
# coerce converte erros em NaN

# elimina dados NaN da coluna TEMPERATURA_MEDIA
archive = archive.dropna(subset=['TEMPERATURA_MEDIA'])

#filtrar os dados apenas de 2023
dados_2023 = archive[archive['date_year'] == 2023]

# agrupando as temperaturas por dia
average = dados_2023.groupby(by='Data')['TEMPERATURA_MEDIA'].mean()

# classificando os dias em frio, calor, etc.
muito_frio = (average < 10).sum()
frio = ((average >= 10) & (average < 16)).sum()
mediano = ((average >= 16) & (average < 22)).sum()
calor = ((average >= 22) & (average < 26)).sum()
muito_calor = (average >= 26).sum()

# criando uma array com cada classificação de dia
dias = [muito_frio, frio, mediano, calor, muito_calor]

print(dias)

# Tamanho da janela a ser exibido o gráfico
plt.figure(figsize=(18, 9))

# estilo do gráfico
plt.style.use('bmh')

#estilização
plt.title('Dias frios e quentes em Curitiba - Ano 2023')

# Criando um array de cores manualmente para evitar o uso de get_cmap (que deu erro)
colors = ['#A8D8EA','#6CB2E2','#F5F5F5','#FFB347', '#FF6961']

# Classificações (a exibir no gráfico)
labels = [f'Muito Frio\n({muito_frio} dias)', f'Frio\n({frio} dias)', f'Mediano\n({mediano} dias)', f'Calor\n({calor} dias)', f'Muito Calor\n({muito_calor} dias)']

# Plotar o gráfico
squarify.plot(sizes=dias, label=labels, color=colors, alpha=.7, text_kwargs={'fontsize': 10, 'wrap': True})
plt.axis('off')

legenda = ['Muito frio: abaixo de 10º', 'Frio: entre 10º e 16º', 'Mediano: entre 16º e 22º', 'Calor: entre 22º e 26º', 'Muito calor: acima de 26º']

# Adicionando a legenda
plt.figlegend(legenda, loc='upper left')

plt.show()
