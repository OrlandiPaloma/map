#exercicio: imprimri o dobro de um valor.
#isto pode ser feito com DEF ou com função MAP.

#DEF:

def dobro(x):
  return x*2
  
valor=2

print(dobro(valor))

#MAP: aqui é definido uma função, como o dobro, ou seja, x*2.
#Após são definidos os valores (1,2,3,4,5)
#É criada uma variavel (valor_dobrado) e dentro dela é colocado o MAP, que contem dois argumentos, sendo o primeiro a função que deseja chamar (neste caso, função dobro) e o segundo argumento é a lista que deseja aplicar o MAP.
#É necessario colocar o MAP dentro de uma lista para que seja possivel imprimi-lo depois.
#Feito um FOR dentro da função valor_dobrado, para que seja impresso CADA item dentro do MAP (o MAP esta dentro da funçao valor_dobrado)
#impresso o V que estava dentro do for anterior.

def dobro(x):
  return x*2
  
valor = [1,2,3,4,5]

valor_dobrado = map(dobro, valor)

for v in valor_dobrado:
  print(v)
  
#Outra opção ao invés de fazer um FOR, é transformar o valor_dobrado em uma lista, conforme linha 37:

def dobro(x):
  return x*2
  
valor = [1,2,3,4,5]

valor_dobrado = map(dobro, valor)
valor_dobrado = list(valor_dobrado)
print(valor_dobrado)