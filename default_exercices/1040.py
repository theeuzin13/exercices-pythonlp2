n1, n2, n3, n4 = map(float, input().split())

x = (((n1*2)+(n2*3)+(n3*4)+(n4*1)) / 10)
print(f"Media: {x:.1f}")

if x >= 7.0:
    print('Aluno aprovado.')
elif x < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota = float(input())
    print(f"Nota do exame: {nota:.1f}")
    Me = (x + nota)/2
    if Me >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f"Media final: {Me:.1f}")
