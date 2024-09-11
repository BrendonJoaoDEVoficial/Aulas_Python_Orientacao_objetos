# Curso de Desenvolvimento de Sistemas.
# Turma: 0152.
# Data: 06/09/2024.
# Autor: Brendon João Campos Neves.
# C) Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

# Importação da biblioteca:
import os


# Definição das classes:
class Intervalos:
    def __init__(self, inicio, final):
        self.inicio = int(inicio)
        self.final = int(final) 
    
    def imprimir_intervalo(self, inicio, final):
        # Método que será sobrecarregado.
        pass

class Imprimir(Intervalos):
    def __init__(self, inicio, final):
        super().__init__(inicio, final)

    def imprimir_intervalo(self):
        for i in range(self.inicio, self.final - 1, -1):
            print(i, end=', ')
            if i in range(self.inicio, self.final, 20) and i > 1:
                print()


# Declarações de variáveis:
intervalo = object

# Limpeza do terminal:
os.system('cls' if os.name == 'nt' else 'clear')

# Instânciação dos objetos:
intervalo = Imprimir(inicio=10, final=0)

# Imprimindo título:
print('.'*79)
print(
    f'Intervalo de {intervalo.inicio} até {intervalo.final - 1} ao contrário')
print('.'*79)

# Imprimindo o intervalo:
intervalo.imprimir_intervalo()
print()

print('.'*79)
print('Fim do programa! Obrigado ;)')
print('.'*79)
