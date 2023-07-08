import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize = (15,8))
grafico = sns.lineplot(x = "dia", y = "venda", data=df_gasolina)
grafico.set(title= "Preço do Combustivel durante os dias", xlabel="Dia", ylabel="Valor da venda")