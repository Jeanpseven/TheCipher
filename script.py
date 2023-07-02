# Função para codificar uma mensagem usando a Cifra de César
def cifra_cesar_codificar(texto, chave):
    resultado = ""
    for letra in texto:
        if letra.isalpha():
            if letra.islower():
                indice_letra = ord(letra) - ord("a")
                indice_codificado = (indice_letra + chave) % 26
                letra_codificada = chr(indice_codificado + ord("a"))
                resultado += letra_codificada
            else:
                indice_letra = ord(letra) - ord("A")
                indice_codificado = (indice_letra + chave) % 26
                letra_codificada = chr(indice_codificado + ord("A"))
                resultado += letra_codificada
        else:
            resultado += letra
    return resultado

# Função para decodificar uma mensagem usando a Cifra de César
def cifra_cesar_decodificar(texto, chave):
    return cifra_cesar_codificar(texto, -chave)


# Função para codificar uma mensagem usando a Cifra de Vigenère
def cifra_vigenere_codificar(texto, chave):
    texto = texto.upper()
    chave = chave.upper()
    resultado = ""
    chave_idx = 0
    for letra in texto:
        if letra.isalpha():
            if letra.islower():
                indice_letra = ord(letra) - ord("a")
                indice_chave = ord(chave[chave_idx]) - ord("A")
                indice_codificado = (indice_letra + indice_chave) % 26
                letra_codificada = chr(indice_codificado + ord("A")).lower()
                resultado += letra_codificada
            else:
                indice_letra = ord(letra) - ord("A")
                indice_chave = ord(chave[chave_idx]) - ord("A")
                indice_codificado = (indice_letra + indice_chave) % 26
                letra_codificada = chr(indice_codificado + ord("A"))
                resultado += letra_codificada
            chave_idx = (chave_idx + 1) % len(chave)
        else:
            resultado += letra
    return resultado


# Função para decodificar uma mensagem usando a Cifra de Vigenère
def cifra_vigenere_decodificar(texto, chave):
    texto = texto.upper()
    chave = chave.upper()
    resultado = ""
    chave_idx = 0
    for letra in texto:
        if letra.isalpha():
            if letra.islower():
                indice_letra = ord(letra) - ord("a")
                indice_chave = ord(chave[chave_idx]) - ord("A")
                indice_decodificado = (indice_letra - indice_chave) % 26
                letra_decodificada = chr(indice_decodificado + ord("A")).lower()
                resultado += letra_decodificada
            else:
                indice_letra = ord(letra) - ord("A")
                indice_chave = ord(chave[chave_idx]) - ord("A")
                indice_decodificado = (indice_letra - indice_chave) % 26
                letra_decodificada = chr(indice_decodificado + ord("A"))
                resultado += letra_decodificada
            chave_idx = (chave_idx + 1) % len(chave)
        else:
            resultado += letra
    return resultado


# Função para codificar uma mensagem usando a Cifra de Transposição
def cifra_transposicao_codificar(texto, chave):
    chave = chave.upper()
    tamanho_chave = len(chave)
    tamanho_texto = len(texto)
    num_colunas = tamanho_texto // tamanho_chave
    if tamanho_texto % tamanho_chave != 0:
        num_colunas += 1
    matriz = [[''] * tamanho_chave for _ in range(num_colunas)]
    coluna_atual = 0
    for letra in texto:
        matriz[coluna_atual // tamanho_chave][coluna_atual % tamanho_chave] = letra
        coluna_atual += 1
    resultado = ''
    for coluna in range(tamanho_chave):
        for linha in range(num_colunas):
            if coluna < tamanho_texto % tamanho_chave and linha == num_colunas - 1:
                break
            resultado += matriz[linha][coluna]
    return resultado


# Função para decodificar uma mensagem usando a Cifra de Transposição
def cifra_transposicao_decodificar(texto, chave):
    chave = chave.upper()
    tamanho_chave = len(chave)
    tamanho_texto = len(texto)
    num_linhas = tamanho_texto // tamanho_chave
    if tamanho_texto % tamanho_chave != 0:
        num_linhas += 1
    matriz = [[''] * tamanho_chave for _ in range(num_linhas)]
    posicao = 0
    for coluna in range(tamanho_chave):
        for linha in range(num_linhas):
            if posicao < tamanho_texto:
                matriz[linha][coluna] = texto[posicao]
                posicao += 1
    resultado = ''
    for linha in range(num_linhas):
        resultado += ''.join(matriz[linha])
    return resultado


# Função para codificar uma mensagem usando a Cifra de Bloco
def cifra_bloco_codificar(texto, chave):
    chave = chave.upper()
    tamanho_chave = len(chave)
    tamanho_texto = len(texto)
    num_blocos = tamanho_texto // tamanho_chave
    if tamanho_texto % tamanho_chave != 0:
        num_blocos += 1
    resultado = ''
    for bloco in range(num_blocos):
        inicio = bloco * tamanho_chave
        fim = (bloco + 1) * tamanho_chave
        bloco_texto = texto[inicio:fim]
        if len(bloco_texto) < tamanho_chave:
            bloco_texto += ' ' * (tamanho_chave - len(bloco_texto))
        bloco_codificado = cifra_substituicao_codificar(bloco_texto, chave)
        resultado += bloco_codificado
    return resultado


# Função para decodificar uma mensagem usando a Cifra de Bloco
def cifra_bloco_decodificar(texto, chave):
    chave = chave.upper()
    tamanho_chave = len(chave)
    tamanho_texto = len(texto)
    num_blocos = tamanho_texto // tamanho_chave
    resultado = ''
    for bloco in range(num_blocos):
        inicio = bloco * tamanho_chave
        fim = (bloco + 1) * tamanho_chave
        bloco_texto = texto[inicio:fim]
        bloco_decodificado = cifra_substituicao_decodificar(bloco_texto, chave)
        resultado += bloco_decodificado
    return resultado


# Função para codificar uma mensagem usando a Cifra Meow
def cifra_meow_codificar(texto):
    texto_codificado = texto.replace("1", "meow").replace("0", "me0w")
    return texto_codificado


# Função para decodificar uma mensagem usando a Cifra Meow
def cifra_meow_decodificar(texto):
    texto_decodificado = texto.replace("meow", "1").replace("me0w", "0")
    return texto_decodificado


# Função principal
def main():
    opcao = input("Escolha a opção:\n1 - Codificar\n2 - Decodificar\n")
    mensagem = input("Digite a mensagem: ")
    chave = input("Digite a chave ou palavra-chave: ")

    if opcao == "1":
        print("Escolha a cifra:")
        print("1 - Cifra de César")
        print("2 - Cifra de Vigenère")
        print("3 - Cifra de Substituição Simples")
        print("4 - Cifra de Transposição")
        print("5 - Cifra de Bloco")
        print("6 - Cifra Meow")
        cifra_opcao = input("Opção: ")

        if cifra_opcao == "1":
            chave_numerica = int(chave)
            mensagem_codificada = cifra_cesar_codificar(mensagem, chave_numerica)
        elif cifra_opcao == "2":
            mensagem_codificada = cifra_vigenere_codificar(mensagem, chave)
        elif cifra_opcao == "3":
            mensagem_codificada = cifra_substituicao_codificar(mensagem, chave)
        elif cifra_opcao == "4":
            mensagem_codificada = cifra_transposicao_codificar(mensagem, chave)
        elif cifra_opcao == "5":
            mensagem_codificada = cifra_bloco_codificar(mensagem, chave)
        elif cifra_opcao == "6":
            mensagem_codificada = cifra_meow_codificar(mensagem)
        else:
            print("Opção inválida!")
            return

        print("Mensagem codificada:", mensagem_codificada)

    elif opcao == "2":
        print("Escolha a cifra:")
        print("1 - Cifra de César")
        print("2 - Cifra de Vigenère")
        print("3 - Cifra de Substituição Simples")
        print("4 - Cifra de Transposição")
        print("5 - Cifra de Bloco")
        print("6 - Cifra Meow")
        cifra_opcao = input("Opção: ")

        if cifra_opcao == "1":
            chave_numerica = int(chave)
            mensagem_decodificada = cifra_cesar_decodificar(mensagem, chave_numerica)
        elif cifra_opcao == "2":
            mensagem_decodificada = cifra_vigenere_decodificar(mensagem, chave)
        elif cifra_opcao == "3":
            mensagem_decodificada = cifra_substituicao_decodificar(mensagem, chave)
        elif cifra_opcao == "4":
            mensagem_decodificada = cifra_transposicao_decodificar(mensagem, chave)
        elif cifra_opcao == "5":
            mensagem_decodificada = cifra_bloco_decodificar(mensagem, chave)
        elif cifra_opcao == "6":
            mensagem_decodificada = cifra_meow_decodificar(mensagem)
        else:
            print("Opção inválida!")
            return

        print("Mensagem decodificada:", mensagem_decodificada)

    else:
        print("Opção inválida!")


# Chamada da função principal
main()
