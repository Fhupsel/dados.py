import random
resp= str(input("Deseja rodar o dado? SIM ou NÃO? "))
if resp.upper()== "NÃO":
    print("Ok, o programa será fechado! ")
while resp.upper()=='SIM':
    print("Olá, vamos começar")
    poss=[1,2,3,4,5,6]
    dado=random.choice(poss)
    print("O resultado do dado foi: ",dado)
    resp= str(input("Deseja rodar o dado? Sim ou não?"))
