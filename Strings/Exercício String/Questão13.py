import random

print("Bem vindo ao Jogo da palavra embaralhada!")

jogar = str(input("jogar? Sim/Não/Adicionar palavra."))

a = 'Otorrinolaringologista'

b = 'Paralelepipedo'

c = 'Caminhão'
    
d = 'Filtro'

e = 'Facebook'

f = 'Banheiro'

g = 'Torta'

h = 'Chocolate'

i = 'Júpiter'

j = 'Segredo'

k = 'Guardanapo'

lista = [a,b,c,d,e,f,g,h,i,j,k]

while jogar == 'Adicionar palavra' or jogar == 'adicionar palavra':
	
        digitar = input("digite a palavra aqui:")
	
        lista.append(digitar)
	
        print("\nObrigado pela colaboração.:D\n")
	
        jogar = str(input("jogar? Sim/Não/Adicionar palavra:\n"))

while jogar == 'Sim' or jogar == 'sim':

	lista2 = []

	palavra = random.choice(lista)

	for i in palavra:

		lista2.append(i)

    	random.shuffle(lista2)

	print()

	for j in range(len(palavra)):

        	print(lista2[j],end=' ')

    	print()

    	resposta = input("\nQual é a palavra?\n")

    	if resposta == palavra:

        	print("\nParabéns, você acertou!!:)")

        	jogar = str(input("\njogar novamente? Sim/Não/Adicionar palavra.\n"))

    	else:

        	print("\nQue pena, você errou.:(\n")

       		print("A resposta certa era",palavra)

        	jogar = str(input("\njogar novamente? Sim/Não/Adicionar palavra.\n"))
		
    	while jogar == 'Adicionar palavra' or jogar == 'adicionar palavra':
		
        	digitar = input("digite a palavra aqui:")
		
        	lista.append(digitar)
		
        	print("\nObrigado pela colaboração.:D\n")
		
        	jogar = str(input("jogar? Sim/Não/Adicionar palavra:"))
		
if jogar == 'não' or jogar == 'Não':
	
    	print("obrigado por jogar")
	
print("Programa encerrado.")
