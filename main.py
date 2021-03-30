#Discente: Patrícia D da Silva 
#P1 de teoria da computação

#função para executar ação dos estados
def acao(entrada,troca, mova): #Configurações da fita
  global cabecadafita
  if (fita[cabecadafita] == entrada):
    fita[cabecadafita] = troca
    if mova == 'E':
      cabecadafita -= 1
    else:
      cabecadafita += 1
    return True
  return False

fita = ['U']*50 #Fita inicializada com U
string = input("Entre com a cadeia de strings [Z]: ") #Entrada 
i = 5
cabecadafita = 5

for s in string: #loop para colocar amarração na fita de 5 posições
  fita[i] = s #Coloquei 5 posições pra testar rápido
  i += 1

estado = 1
U,X,Y,Z,E,D = 'U','X','Y','Z','E','D' #movimentos e simbolos da fita[Z de 0]
cabecadafitanterior = -1
aceita = False
#################################################################
#====> ATENÇÃO: Estado 6 = qaceita, Estado 7 = qrejeita**********
#################################################################
while(cabecadafitanterior != cabecadafita): #se a cabeça da fita não move, significa que encerrou a mt
      #sempre recebe a fita anterior
      cabecadafitanterior  = cabecadafita

      #CONFIGURAÇÕES DA MT
      if estado == 1:
        if acao(U, U, D) or acao(X,X,D):
          estado = 7 #Esses estados foram pré definidos para facilitar os testes das cadeias de Z(Zeros).
        elif acao(Z,Y,D):
          estado = 2

      elif estado == 2:
        if acao(X,X,D):
          estado = 2
        elif acao(U,U,D):
          estado = 6
        elif acao(Z,X,D):
          estado = 3

      elif estado == 3:
        if acao(X,X,D):
          estado = 3
        elif acao(U,U,E):
          estado = 5
        elif acao(Z,Z,D):
          estado = 4
    
      elif estado == 4:
        if acao(X,X,D):
          estado = 4
        elif acao(Z,X,D):
          estado = 3
        elif acao(U,U,D):
          estado = 7
    
      elif estado == 5:
        if acao(Z,Z,E) or acao(X,X,E):
          estado  = 5
        elif acao(Y,Y,D):
          estado = 2 

      else:
       aceita = True
#Printando o resultado da mt
if estado==6:
  print("Cadeia aceita!")
else:
  print("Cadeia rejeitada!")