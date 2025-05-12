print ("Este programa calcula la altura de una caja")

largo=int(input("Ingrese el largo:"))
ancho=int(input("Ingrese el ancho:"))

h=1 #altura
volumen=0 #volumen
volumen2=0
volumen2 = volumen
#vol = h*(largo - h -h) * (ancho -2*h)

while volumen >= volumen2:
 volumen2 = volumen
 volumen=h*(ancho-2*h)*(largo-h*2)
 h += 1
 print(volumen)

print(f"El volumen maximo es:")