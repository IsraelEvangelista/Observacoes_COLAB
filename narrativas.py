f'''

Existem várias maneiras de aperfeiçoar a narrativa gerada por este código. Algumas sugestões incluem:

Adicionar informações sobre os usuários com maior faturamento: você pode usar o método groupby do Pandas para agrupar os dados por usuário e, em seguida, usar o método sort_values para ordenar os usuários por faturamento. Em seguida, você pode incluir informações sobre os usuários com maior faturamento na narrativa.

Adicionar uma análise de tendência: você pode usar o método rolling do Pandas para calcular a média móvel dos dados e incluir informações sobre a tendência do faturamento e da inadimplência na narrativa.

Criar gráficos para ilustrar os dados: você pode usar a biblioteca Matplotlib para criar gráficos que ilustrem os dados, como um gráfico de linhas que mostre a evolução do faturamento e da inadimplência ao longo do tempo.

Usar valores para usuários "A", "B", "C" e assim por diante: você pode usar o método groupby do Pandas para agrupar os dados por usuário e, em seguida, usar o método sum para calcular o faturamento e a inadimplência para cada usuário. Em seguida, você pode incluir esses valores na narrativa.

'''

# Exemplo de um dataset de faturamento e inadimplencia

import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados em um dataframe
df = pd.read_csv("faturamento.csv")

# Filtrando os dados para o ano de 2022
df = df[df["data"].dt.year == 2022]

# Calculando o valor total faturado e inadimplência
total_faturado = df["faturamento"].sum()
total_inadimplencia = df["inadimplencia"].sum()

# Agrupando os dados por usuário e ordenando por faturamento
usuarios_por_faturamento = df.groupby("usuario")["faturamento"].sum().sort_values(ascending=False)

# Calculando a média móvel dos dados
media_movel_faturamento = df["faturamento"].rolling(3).mean()
media_movel_inadimplencia = df["inadimplencia"].rolling(3).mean()

# Criando a narrativa
narrativa = "Em 2022, o valor total faturado foi de R$ {:.2f} e o valor de inadimplência foi de R$ {:.2f}. O usuário com maior faturamento foi {} com R$ {:.2f}".format(total_faturado, total_inadimplencia, usuarios_por_faturamento.index[0], usuarios_por_faturamento[0])

print(narrativa)

# Criando o gráfico de linhas
plt.plot(df["data"], media_movel_faturamento, label
         

         
# Mais um exemplo
         
import pandas as pd

# Carregando os dados em um dataframe
df = pd.read_csv("faturamento.csv")

# Filtrando os dados para o ano de 2022
df = df[df["data"].dt.year == 2022]

# Calculando o valor total faturado e inadimplência
total_faturado = df["faturamento"].sum()
total_inadimplencia = df["inadimplencia"].sum()

# Criando a narrativa
narrativa = "Em 2022, o valor total faturado foi de R$ {} e o valor de inadimplência foi de R$ {}.".format(total_faturado, total_inadimplencia)

print(narrativa)

