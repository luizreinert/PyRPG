import emoji 
from colorama import Fore
from time import sleep

# Define a cor desejada utilizando a bibloteca colorama
def cor(x):
  if x == "yl" or x == 2:
    cor = Fore.LIGHTYELLOW_EX
  if x == "gr" or x == 3:
    cor = Fore.LIGHTGREEN_EX
  if x == "red" in x or x == 5:
    cor = Fore.LIGHTRED_EX
  if x == "pink" in x or x == 4:
    cor = Fore.LIGHTMAGENTA_EX
  if x == "blue" in x or x == 1:
    cor = Fore.LIGHTBLUE_EX
  if x == "cyan":
     cor = Fore.LIGHTCYAN_EX
  return cor

# Reseta a cor
def reset():
  resetar = (Fore.RESET)
  return resetar

# Adiciona emojis que representem as classes em strings específicas
def personagem(a):
  if a == "mago" or a == "Mago":
    return emoji.emojize(" :mage:")
  if a == "guer" or a == "Guerreiro":
    return emoji.emojize(" :person_fencing:")
  elif a == "cler" or a == "Clérigo":
    return emoji.emojize(" :elf:")
  elif a == "arq" or a == "Arqueiro":
    return emoji.emojize(" :supervillain:")
  elif a == "lad" or a == "Ladino":
    return emoji.emojize(" :bust_in_silhouette:")

# Define a descrição referente à classe no menu de escolha
def descricao(d):
  if d == 'mago':
    return f'''\nUm praticante arcano ágil, hábil em magias.
Tem {cor('gr')}vantagem em ataque e sorte{reset()}, possuindo {cor("red")}desvantagem em defesa e vida{reset()}.\n'''
  if d == 'guer':
    return f'''\nO guerreiro é especializado em combate corpo a corpo, forte e resistente.
Tem {cor('gr')}vantagem em ataque, defesa e vida{reset()}, porém com uma baixa {cor("red")}agilidade{reset()}.\n'''
  if d == 'cler':
    return f'''\nCurandeiros com excelentes habilidades defensivas, clérigos priorizam a proteção.
Tem {cor('gr')}vantagem em defesa e vida{reset()}, possuindo {cor("red")}desvantagem em ataque{reset()}.\n'''
  if d == 'lad':
    return f'''\nEspecialistas ágeis e sorrateiros, ladinos se destacam na agilidade e na sorte, preferindo ataques rápidos e furtivos.
Tem {cor('gr')}vantagem na agilidade e na sorte{reset()}, porém com {cor("red")}desvantagem em defesa{reset()}.\n'''
  if d == 'arq':
    return f'''\nEspecialistas em ataques à distância, arqueiros são precisos e ágeis, porém menos resistentes em combates próximos.
Tem {cor('gr')}vantagem na agilidade e ataque{reset()}, porém com {cor("red")}desvantagem em defesa{reset()}.\n'''

# Implementa o menu principal de classes, monstrando as classes, suas respectivas descrições e atributos.
def menu():
  print(f'''{cor("blue")}[1] Mago{personagem("mago")} {reset()}\n{descricao('mago')}\nAtaque = 5\nDefesa = 2\nVida = 10\nSorte = 8\nAgilidade = 5 \n
{cor("yl")}[2] Guerreiro{personagem("guer")}{reset()} {descricao('guer')}\nAtaque = 7\nDefesa = 7\nVida = 10\nSorte = 4\nAgilidade = 2\n
{cor("gr")}[3] Clérigo{personagem("cler")}{reset()} {descricao('cler')}\nAtaque = 2\nDefesa = 9\nVida = 10\nSorte = 5\nAgilidade = 4\n
{cor("pink")}[4] Ladino{personagem("lad")}{reset()} {descricao('lad')}\nAtaque = 3\nDefesa = 2\nVida = 10\nSorte = 5\nAgilidade = 10\n
{cor("red")}[5] Arqueiro{personagem("arq")}{reset()}{descricao('arq')}\nAtaque = 5\nDefesa = 4\nVida = 10\nSorte = 5\nAgilidade = 6\n''')

# Introduz o combate inicial após escolha da classe
def mensagem():
  mensagem_inicial = f'Seu primeiro inimigo é um {Mago.nome}'
  for linha in mensagem_inicial:
    for c in linha:
      print(c, end='', flush=True)
      sleep(0.1)
  
# Define as classes e atributos
class classes:
  def __init__(self, nome, ataque, defesa, vida, sorte, agilidade):
    self.nome = nome
    self.atk = ataque
    self.deff = defesa
    self.vida = vida
    self.sorte = sorte
    self.agilidade = agilidade
Mago = classes("Mago", 5, 2, 10, 8, 5)
Guerreiro = classes("Guerreiro", 7, 7, 10, 4, 2)
Clerigo = classes("Clérigo", 2, 9, 10, 5, 4)
Ladino = classes("Ladino", 3, 2, 10, 5, 10)
Arqueiro = classes("Arqueiro", 5, 4, 10, 5, 6)

# Define os inimigos e e atributos
class monstros:
  def __init__(self, nome, ataque, defesa, vida, sorte, agilidade):
    self.nome = nome
    self.atk = ataque
    self.deff = defesa
    self.vida = vida
    self.sorte = sorte
    self.agilidade = agilidade
Aranha = monstros("Aranha", 1, 1, 3, 1, 4)
Goblin = monstros("Goblin", 1, 2, 5, 1, 1)
Esqueleto = monstros("Esqueleto", 2, 3, 6, 1, 2)

# Função principal que permite ao jogador escolher uma classe de personagem a partir de um menu, confirmar a escolha e prosseguir com o jogo
def main():
  clas = {1: 'Mago', 2: 'Guerreiro', 3: 'Clérigo', 4: 'Ladino', 5: 'Arqueiro'}
  print(f'\n{cor("yl")}Escolha a sua classe!{reset()}\n')
  menu()
  classe_escolhida = 0
  classe_selecionada = int(input(f'{cor("yl")}Digite o número: {reset()}'))
  while True:
    if classe_selecionada in range(0, 6):
      while True:
        confirmar = int(input(f'\nVocê escolheu [{cor(classe_selecionada)}{clas[classe_selecionada]}{reset()}{personagem(clas[classe_selecionada])}], confirmar?\n\n{cor("gr")}[1] Sim\n{cor("red")}[2] Não\n{reset()}'))
        if confirmar == 1:
          classe_escolhida = classe_selecionada
          print(f'Você é um [{cor(classe_escolhida)}{clas[classe_escolhida]}{reset()}{personagem(clas[classe_escolhida])}]!')
          return True
        elif confirmar == 2:
          main()
        else:
          print('Não entendi! Digite novamente\n')
          continue
        return True
    else:
      print('Não entendi! Digite novamente: ')
      classe_selecionada = int(input(f'{cor("yl")}Digite o número: {reset()}')) 

main()
mensagem()

