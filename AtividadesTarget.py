#Exercicio 1
indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k

print(f"A soma será {soma}")

print("")
print("")

# Exercicio 2

numero = int(input("Digite um número para saber se ele pertence a sequência Fibonacci: "))

def seq_Fibonacci(seq):
    seqFibo = [0, 1]
    while seqFibo[-1] <= seq:
      seqFibo.append(seqFibo[-1] + seqFibo[-2])
    return seqFibo

def pertence_seq(numero, sequencia):
    if numero in sequencia:
        return True
    else:
        return False

seqFibonacci = seq_Fibonacci(numero)
if pertence_seq(numero, seqFibonacci):
    print(f"O número {numero} pertence a sequência Fibonacci!")
else:
    print(f"O número {numero} não pertence a sequência Fibonacci!")

print("")
print("")

# Exercicio 3

def prox_num_a(seq):
    return seq[-1] + 2

def prox_num_b(seq):
    return seq[-1] * 2

def prox_num_c(seq):
    return "{:.0f}".format(seq[-1] + ((len(seq)- 5) ** 3.7))

def prox_num_d(seq):
    return ((len(seq) + 1) * 2) ** 2

def prox_num_e(seq):
    return seq[-1] + seq[-2]

def prox_num_f(seq):
    if len(seq) % 2 == 0:
        return seq[-1] + 1
    else:
        return seq[-1] + 2

seqA = [1, 3, 5, 7]
seqB = [2, 4, 8, 16, 32, 64]
seqC = [0, 1, 4, 9, 16, 25, 36]
seqD = [4, 16, 36, 64]
seqE = [1, 1, 2, 3, 5, 8]
seqF = [2, 10, 12, 16, 17, 18, 19]

print("Próximos números serão: ")
print("Sequência A: ", prox_num_a(seqA))
print("Sequência B: ", prox_num_b(seqB))
print("Sequência C: ", prox_num_c(seqC))
print("Sequência D: ", prox_num_d(seqD))
print("Sequência E: ", prox_num_e(seqE))
print("Sequência F: ", prox_num_f(seqF))

print("")
print("")

# Exercicio 4

import time
def qual_interruptor():

    print("Indo pela primeira vez: Ligando o interruptor de número 1")
    time.sleep(2)
    print("Primeira vez indo: OK")
    time.sleep(2)

    print("Indo pela segunda vez: Desligando o interruptor de número 1 e ligando o interruptor de número 2")
    time.sleep(2)
    print("Segunda vez indo: OK")
    time.sleep(2)

    print("Colocando as mãos nas lâmpadas para verificar sua temperatura")
    print("")
    time.sleep(2)

    lamp1 = "apagada e quente"
    lamp2 = "acessa"
    lamp3 = "apagada e fria"

    if lamp1 == "apagada e quente":
      print("A lâmpada 1 está apagada e quente, então:")
      print("O interruptor de número 1 acende a lampada 1")
    if lamp2 == "acessa":
      print("A lâmpada 2 está acessa, então:")
      print("O interruptor de número 2 acende a lampada 2")
    if lamp3 == "apagada e fria":
      print("A lâmpada 3 está apagada e fria, então:")
      print("O interruptor de número 3 acende a lampada 3")

qual_interruptor()

print("")
print("")

# Exercicio 5

def inverte_String(str):
    return str[:: -1]

strOriginal = input("Digite uma palavra: ")
strInvertida = inverte_String(strOriginal)

print(f"Palavra original: {strOriginal}")
print(f"Palavra invertida: {strInvertida}")















