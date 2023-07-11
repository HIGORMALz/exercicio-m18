plt.figure(figsize = (15,8))
sns.set_palette("husl")
grafico = sns.lineplot(x = "dia", y = "venda", data=gasolina_df) 
grafico.set(title= "Preço medio gasolina na cidade de São Paulo", xlabel="Dia", ylabel="Valor da venda")