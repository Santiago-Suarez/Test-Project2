
#!/usr/bin/env python
# -*- coding: utf-8 -*-

millas = 0.62137

print str("Este programa te permite convertir km en millas")

kilometros = int(raw_input("Inserta el numero de km que quieres convertir: "))

print kilometros * millas


while True:
    repeticion = raw_input("Quieres convertir otra cantidad?: ")
    if repeticion == "si":
        kilometros = int(raw_input("Inserta el nuevo numero de km que quieres convertir: "))
        print kilometros * millas

else:
    print "Hasta luego, Lucas"
