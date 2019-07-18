numero = None

while numero is None:
    try:
        numero = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Erro! Era pra ter digitado um número inteiro. Tente de novo.")

print(f"O número digitado foi {numero}")