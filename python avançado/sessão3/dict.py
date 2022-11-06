aluno = {
    'nome': 'joana',
    'idade': 17,
    'inscrito': True,
}
print(aluno['nome'])
print(aluno.get('ano','Não Existe a chave ""')) 

aluno['ano'] = 10

print(aluno.get('ano','Não Existe a chave "ano"!'))