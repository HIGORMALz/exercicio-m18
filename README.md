# **Visualização preço médio de venda da gasolina na cidade de São Paulo nos 10 primeiros dias de Julho de 2021**

**Introduçao**

Esse projeto mostra um gráfico de linha com o preço médio de vendas de gasolina na cidade de São Paulo e junto a ele seu código de geraçao.

**Código de geração**

> 'import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize = (15,8))
grafico = sns.lineplot(x = "dia", y = "venda", data=df_gasolina)
grafico.set(title= "Preço do Combustivel durante os dias", xlabel="Dia", ylabel="Valor da venda")'

**Gráfico gerado**
![]()![image](https://github.com/HIGORMALz/exercicio-m18/assets/138539839/dc8e99bc-658c-4b82-8996-fdedd9ba1528)
**Insight**

 * 1: maior preço da gasolina durante o périodo analisado foi de **5.20**;
 * 2: menor preço foi igual a **4.95**;
 * 3: dia com maior alta da gasolina foi o **Dia 4;**
 * 4: dia com o menor valor da gasolina foi o **Dia 9;**

Durante o curto périodo analisado o preço da gasolina na cidade de São Paulo se mostrou bastante volatil.
