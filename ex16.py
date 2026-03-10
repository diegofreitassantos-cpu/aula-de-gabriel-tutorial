# ex16 - condiçao com and

idade = int(input("idade: "))
carteira = input(" tem carteira? (sim/nao): ")

if idade >= 18 and carteira == "sim":
    print("pode dirigir")

else:
    print ("nao pode dirigir")
    