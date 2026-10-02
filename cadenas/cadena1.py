vector = ["j", "u", "a", "n"]
print("TIPO DE CLASE")
print(type(vector))

print("RECORRE EL VECTOR")
for letra in vector:
    print(letra)

nombre = "luis juan"
print("*"*20)
print("RECORRE EL STR")
for letra in nombre:
    print(letra)

print("*"*20)
print("TAMAÑO")
print(len(vector))
print(len(nombre))

def convertirMayus(texto):
    return f"{texto.upper()}"

def convertirMinus(texto):
    return f"{texto.lower()}"

def caps(texto):
    return f"{texto.capitalize()}"

def titulo(texto):
    return f"{texto.title()}"

def generarEmail(texto):
    nombre = texto.split()
    email = ''.join(palabra[:2].lower() for palabra in nombre)
    return f"{email}@uamv.edu.ni"

print("*"*20)
print("CONVERTIR MAYUSCULAS")
print(convertirMayus(nombre))
#print(convertirMayus(nombre))

print("*"*20)
print("CADA LETRA EN MAYUSCULA")
for w in vector:
    print(convertirMayus(w),) 

print("*"*20)
print("CONVERTIR MINUSCULA")
print(convertirMinus(nombre))

print("*"*20)
print("CAPITALIZAR")
print(caps(nombre))

print("*"*20)
print("TITULO")
print(titulo(nombre))

print("*"*20)
print("GENERAR EMAIL")
print(generarEmail(nombre))