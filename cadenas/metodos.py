text = "me mundo llamo ricky"

text = text.upper()  # convertir a mayusculas
print(text)

text = text.lower() # convertir a minusculas
print(text)

contar = text.count("o") # contar subcadenas en nuestro texto
print(contar)

capitalize = text.capitalize() #Convierte la primera letra en mayusculas
print(capitalize)

indices = text.index("m") #retorna el indice
print(indices)

find = text.find("ric") #Retorna el indice principal de la cadena
print(find)

replace = text.replace("m", "z") #Reemplazar por el valor el que deseas
print(replace)

lista = text.split(" ") #convertimos a una lista
print(lista)

raton = ["Brennis", "Es", "Una", "Rata"]
resultado = "-".join(raton)
print(resultado)

print("mundo" in text)