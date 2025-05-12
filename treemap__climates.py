import pandas as pd
import matplotlib.pyplot as plt
import squarify

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
