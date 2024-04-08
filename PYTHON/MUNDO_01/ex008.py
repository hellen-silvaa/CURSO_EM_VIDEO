#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Uma distância em mmetros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
m = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medidade de {medida}m corresponde a {km}km, {hm}hm, {dam}dam, {m}m,, {cm}cm, {mm}mm')