def ler_dados():
    lista = []
    resp = 's'

    while resp == 's':
        nome = input('Nome: ')
        nota = float(input('Nota: '))
        lista.append([nome, nota])
        resp = input('Continuar (s/n)')
    return lista

if __name__ == '__main__':

    lista = ler_dados()
    print(lista)

    print(f'Quantidade de alunos {len(lista)}')

    soma = 0
    for aluno in lista:
        soma += aluno[1]
    media = soma/len(lista)
    print(f'Media: {media}')

    for aluno in lista:
        if aluno[1] > media:
            print(aluno[0])

    lista.sort(key=lambda x: x[1])
    print(lista)