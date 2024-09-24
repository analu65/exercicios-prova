classificacao = 'Botafogo','Fortaleza','Flamengo','Palmeiras','São Paulo','Cruzeiro','Bahia','Athletico','Vasco','Bragantino','Juventude','Grêmio','Criciúma','Internacional','Vitória','Corinthians','Fluminense','Cuiabá','Atlético'	

for indice in enumerate(classificacao):
    corinthians = classificacao.index("Corinthians")+1
print("Cinco primeiros colocados: ",classificacao[0:5])
print("Cinco últimos colocados: ",classificacao[-4:])
print("Times em ordem alfabética: ", sorted(classificacao, reverse = False))
print("Posição do corinthians: ",corinthians)