# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# A) Faça um programa que imprima os números no intervalo entre 1 e 100.
# Os números devem ser apresentados na horizontal.

# Importação da biblioteca:
import os


# Definição da classe:
class Intervalos:
    def __init__(self, inicio, final, passo=1):
        self.inicio = int(inicio)
        self.final = int(final) 
        self.passo = int(passo)

    def imprimir_intervalo(self):
        for i in range(self.inicio, self.final, self.passo):
            print(i, end=', ')


# Declarações de variáveis:
intervalo = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

# Instânciação do objeto:
intervalo = Intervalos(inicio=1, final=100 + 1)

# Imprimindo título:
print('.'*79)
print(f'Intervalo de {intervalo.inicio} até {intervalo.final - 1}')
print('.'*79)

# Imprimindo o intervalo:
intervalo.imprimir_intervalo()
print()

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
