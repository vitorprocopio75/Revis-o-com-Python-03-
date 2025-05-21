nome_da_pessoa = input("qual é o seu nome ?")


    
nota = float(input(f"{nome_da_pessoa}, digite a nota final de (0 a 10): "))

if 9.0 <= nota <= 10.0:
    classificacao = "Exelente"
elif 7.0 <= nota <= 8.9:
    classificacao = "Bom"
elif 5.0 <= nota <= 6.9:
    classificacao = "Regular"
elif 3.0 <= nota <= 4.9:
    classificacao = "Ruim"
elif 0.0 <= nota <= 2.9:
    classificacao = "Crítico"
else: 
    "Nota inválida "

print(f"Agente {nome_da_pessoa}, sua classificação é: {classificacao} (nota: {nota})")


