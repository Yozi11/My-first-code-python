import os
os.system("cls")


nota1=float(input("escreva uma nota1:"))
nota2=float(input("escreva uma nota 2 "))
media = (nota1 + nota2)/2


if media >= 7:
    resultado="aprovado"
else:
    resultado = "reprovado"
 
 
print(f"media:{media}")
print(f"resultado:{resultado}")        