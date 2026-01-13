print("Hola mundo")
print('Hola "mundo"')

ingles = "Hi i'm javier"
print(ingles)
multiple = """ Como
estan?  """

print (multiple)

palabra = "murcielago"
print(len(palabra))
palabra = "ejercicios de Python"
incluida = "Python" in  palabra
print(incluida)

noincluida = "javascript" not in palabra

print(noincluida)

mayuscula = palabra.upper()
print(mayuscula)

minuscula = palabra.lower()
print(minuscula)

espacios = "   este es el texto    "
limpieza = espacios.strip()
print(limpieza)


texto = "Este es un texto"
print(texto[0]) #posicion de indice desde 0 en string

print(texto[0:4])

print(texto[0:len(texto)])


print(texto[:len(texto)])

texto2 = "este curso es de python"
print(texto2.replace("python","javascript"))
textoDividido = texto.split(" ")
print(textoDividido)


texto3 = "Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras"

print("mayusculas".lower() in texto3.lower())