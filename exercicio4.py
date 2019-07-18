meninos = ["Luiz", "João", "Alex", "Guilherme"]
meninas = ["Laís", "Lolo", "Ana"]

i = 1

for menino in meninos:
    for menina in meninas:
        print(f"Casalzinho {i}: {menino} e {menina}")
        i += 1