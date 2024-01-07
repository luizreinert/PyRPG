import emoji 
from time import sleep
from random import choice, randint

# Define os inimigos e e atributos
class inimigos:
  def __init__(self, nome, ataque, defesa, vida, sorte, agilidade):
    self.nome = nome
    self.atk = ataque
    self.deff = defesa
    self.vida = vida
    self.sorte = sorte
    self.agil = agilidade
Aranha = inimigos("Aranha", 1, 1, 20, 1, 4)
Goblin = inimigos("Goblin", 1, 2, 20, 1, 1)
Esqueleto = inimigos("Esqueleto", 2, 3, 20, 1, 2)
lista_inimigos = [Aranha, Goblin, Esqueleto]
inimigo_escolhido = choice(lista_inimigos)
inimigo_batalha = inimigo_escolhido

# Define as classes e atributos
class classes:
  def __init__(self, nome, ataque, defesa, vida, sorte, agilidade):
    self.nome = nome
    self.atk = ataque
    self.deff = defesa
    self.vida = vida
    self.sorte = sorte
    self.agil = agilidade
Mago = classes("Mago", 6, 3, 20, 5, 1)
Guerreiro = classes("Guerreiro", 7, 7, 20, 4, 2)
Clerigo = classes("Clérigo", 2, 9, 20, 5, 4)
Ladino = classes("Ladino", 3, 2, 20, 5, 10)
Arqueiro = classes("Arqueiro", 5, 4, 20, 5, 6)
lista_classes = [Mago, Guerreiro, Clerigo, Ladino, Arqueiro]
classe_aleatoria = choice(lista_classes) 

# Define a cor desejada utilizando a bibloteca colorama
def cor(x):
  if x == "yl" or x == "2" or x == Guerreiro:
    cor = "\033[1;33m"
  if x == "gr" or x == "3" or x == Clerigo:
    cor = "\033[1;32m"
  if x == "red" or x == "5" or x == Arqueiro:
    cor = "\033[0;31m"
  if x == "pink" or x == "4" or x == Ladino:
    cor = "\033[1;35m"
  if x == "blue" or x == "1" or x == Mago:
    cor = "\033[1;34m" 
  if x == "cy":
    cor = "\033[1;36m"
  if x == "reset":
    cor = "\033[0m"
  return cor

# Adiciona emojis que representem as classes em strings específicas
def emojis(a):
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
  elif a == "aranha" or a == "Aranha":
    return emoji.emojize(" :spider:")
  elif a == "goblin" or a == "Goblin":
    return emoji.emojize(" :goblin:")
  elif a == "esqueleto" or a == "Esqueleto":
    return emoji.emojize(" :skull:")

# Define a descrição referente à classe no menu de escolha
def descricao(d):
  if d == 'mago':
    return f'''\nUm praticante arcano ágil, hábil em magias.
Tem {cor('gr')}vantagem em ataque e sorte{cor('reset')}, possuindo {cor("red")}desvantagem em defesa e vida{cor('reset')}.\n'''
  if d == 'guer':
    return f'''\nO guerreiro é especializado em combate corpo a corpo, forte e resistente.
Tem {cor('gr')}vantagem em ataque, defesa e vida{cor('reset')}, porém com uma baixa {cor("red")}agilidade{cor('reset')}.\n'''
  if d == 'cler':
    return f'''\nCurandeiros com excelentes habilidades defensivas, clérigos priorizam a proteção.
Tem {cor('gr')}vantagem em defesa e vida{cor('reset')}, possuindo {cor("red")}desvantagem em ataque{cor('reset')}.\n'''
  if d == 'lad':
    return f'''\nEspecialistas ágeis e sorrateiros, ladinos se destacam na agilidade e na sorte, preferindo ataques rápidos e furtivos.
Tem {cor('gr')}vantagem na agilidade e na sorte{cor('reset')}, porém com {cor("red")}desvantagem em defesa{cor('reset')}.\n'''
  if d == 'arq':
    return f'''\nEspecialistas em ataques à distância, arqueiros são precisos e ágeis, porém menos resistentes em combates próximos.
Tem {cor('gr')}vantagem na agilidade e ataque{cor('reset')}, porém com {cor("red")}desvantagem em defesa{cor('reset')}.\n'''

# Implementa o menu principal de classes, monstrando as classes, suas respectivas descrições e atributos.
def menu():
  print(f'''{cor("blue")}[1] Mago{emojis("mago")} {cor('reset')}\n{descricao('mago')}\nAtaque = 5\nDefesa = 2\nVida = 10\nSorte = 8\nAgilidade = 5 \n
{cor("yl")}[2] Guerreiro{emojis("guer")}{cor('reset')} {descricao('guer')}\nAtaque = 7\nDefesa = 7\nVida = 10\nSorte = 4\nAgilidade = 2\n
{cor("gr")}[3] Clérigo{emojis("cler")}{cor('reset')} {descricao('cler')}\nAtaque = 2\nDefesa = 9\nVida = 10\nSorte = 5\nAgilidade = 4\n
{cor("pink")}[4] Ladino{emojis("lad")}{cor('reset')} {descricao('lad')}\nAtaque = 3\nDefesa = 2\nVida = 10\nSorte = 5\nAgilidade = 10\n
{cor("red")}[5] Arqueiro{emojis("arq")}{cor('reset')}{descricao('arq')}\nAtaque = 5\nDefesa = 4\nVida = 10\nSorte = 5\nAgilidade = 6\n''')

# Função para efeito de digitação nos textos
def texto_anim(texto):
  for c in texto:   
    print(c, end='', flush=True)
    sleep(0.04)
  return c

# Função principal que permite ao jogador escolher a classe do jogador a partir do menu
def main():
  clas = {'1': Mago, '2': Guerreiro, '3': Clerigo, '4': Ladino, '5': Arqueiro}
  print(f'\n{cor("yl")}Escolha a sua classe!{cor('reset')}\n')
  menu()
  classe_selecionada = input(f'{cor("yl")}Digite o número: {cor('reset')}')
  while True:
    if classe_selecionada in clas:
      while True:
        confirmar = input(f'\nVocê escolheu [{cor(classe_selecionada)}{clas[classe_selecionada].nome}{cor('reset')}{emojis(clas[classe_selecionada].nome)}], confirmar?\n\n{cor("gr")}[1] Sim\n{cor("red")}[2] Não\n{cor('reset')}')
        if confirmar == '1':
          global classe_escolhida
          classe_escolhida = clas.get(classe_selecionada)
          print(f'Você é um [{cor(classe_escolhida)}{clas[classe_selecionada].nome}{cor('reset')}{emojis(clas[classe_selecionada].nome)}]!')
          return True
        elif confirmar == '2':
          main()
        else:
          print('Não entendi! Digite novamente\n')
          continue
        return
    else:
      print('Não entendi! Digite novamente: ')
      classe_selecionada = input(f'{cor("yl")}Digite o número: {cor('reset')}')
    return

# Define o valor do dano e a ocorrência de dano critico dos ataques do jogador e do adversário, retornando esse valor inicial.
def ataque_turno(vez):
  if vez == "jogador":
    dano_ataque = randint(1, classe_escolhida.atk)
    sorte_ataque = classe_escolhida.sorte*4
    chance_critico = randint(1, 100)
    if chance_critico <= sorte_ataque:
      dano_ataque += int(classe_escolhida.atk*1.5)
      texto_anim(f'{cor("red")}Ataque crítico! {cor("cy")}Você infligiu {cor("red")}{dano_ataque} {cor("yl")}de dano{cor("reset")}\n')
    else:
      texto_anim(f'{cor("cy")}Você infligiu {cor("red")}{dano_ataque} {cor("cy")}de dano!{cor("reset")}\n')
    return dano_ataque
  if vez == "adversario":
    dano_ataque = 0
    dano_ataque = randint(1, inimigo_batalha.atk)
    sorte_ataque = inimigo_batalha.sorte*4
    chance_critico = randint(1, 100)
    if chance_critico <= sorte_ataque:
      dano_ataque += int(inimigo_batalha.atk*1.5)
      texto_anim(f'{cor("red")}Ataque crítico! {cor("cy")}Seu adversário infligiu {cor("red")}{dano_ataque} {cor("yl")}de dano{cor("reset")}\n')
    else:
      texto_anim(f'{cor("cy")}Seu adversário infligiu {cor("red")}{dano_ataque} {cor("cy")}de dano!{cor("reset")}')
    return dano_ataque

# Define o valor total do dano do jogador, adicionando mais uma vez dano/dano com crítico caso seja sorteado dois ataques.
def dano_turnoJogador(turno):
  dano_ataquetotal = 0
  if turno == "turno_jogador":
    print(f"{cor("gr")}\n    ↜———✧ Seu turno ✧———↝{cor("reset")}\n")
    dano_ataquetotal += ataque_turno("jogador")
    agili = classe_escolhida.agil*5
    chance_ataque2 = randint(1, 100)
    if chance_ataque2 <= agili:
      print(f'{cor("gr")}Você conseguiu atacar de novo!{cor("reset")}')
      dano_ataquetotal += ataque_turno("jogador")
      print(f'\n{cor("yl")}\nVocê causou {cor("red")}{dano_ataquetotal}{cor("yl")} de dano nesse turno!{cor("reset")}')
  return dano_ataquetotal

# Define o valor total do dano do adversário, adicionando mais uma vez dano/dano com crítico caso seja sorteado dois ataques.
def dano_turnoAdversário(turno):
  dano_ataquetotal = 0
  if turno == "turno_adversario":
    print(f"{cor("red")}\n  ↜———✧ Turno do adversário ✧———↝{cor("reset")}\n")
    dano_ataquetotal += ataque_turno("adversario")
    agili = inimigo_batalha.agil*5
    chance_ataque2 = randint(1, 100)
    if chance_ataque2 <= agili:
      print(f'{cor("gr")}Seu adversário conseguiu atacar de novo!{cor("reset")}')
      dano_ataquetotal += ataque_turno("adversario")
      print(f'\n{cor("yl")}Seu adversário causou {cor("red")}{dano_ataquetotal}{cor("yl")} de dano nesse turno!{cor("reset")}')
  return dano_ataquetotal

# Define o combate caso comece pelo adversário
def turno_adversario():
  vida_jogador = classe_escolhida.vida
  vida_inimigo = inimigo_escolhido.vida
  while True:
    vida_jogador -= dano_turnoAdversário("turno_adversario")
    if vida_jogador > 0 and vida_jogador <= 0.30*classe_escolhida.vida:
      print(f'\n{cor("yl")}Você está enfraquecido! Lhe resta {cor("red")}{vida_jogador} de vida{cor("reset")}\n')
    if  vida_jogador > 0 and vida_jogador > 0.30*classe_escolhida.vida:
      print(f'\n{cor("yl")}Você está com {cor("red")}{vida_jogador} {cor("yl")}de vida{cor("reset")}\n')
    if vida_jogador <= 0:
      print(f'{cor("red")}Você foi derrotado!{cor("reset")}')
      return True
    vida_inimigo -= dano_turnoJogador("turno_jogador")
    if vida_inimigo > 0 and vida_inimigo <= 0.30*inimigo_escolhido.vida:
      print(f'{cor("yl")}Seu inimigo está enfraquecido! Restam apenas {cor("red")}{vida_inimigo} de vida{cor("reset")}\n') 
    if vida_inimigo > 0 and vida_inimigo > 0.30*inimigo_escolhido.vida:
      print(f'{cor("yl")}Seu inimigo está com {cor("red")}{vida_inimigo} {cor("yl")}de vida{cor("reset")}')
    if vida_inimigo <= 0:
      print(f'{cor("gr")}Parabéns, você derrotou o adversário!{cor("reset")}')
      return True

# Define o combate caso comece pelo jogador
def turno_jogador():
  vida_jogador = classe_escolhida.vida
  vida_inimigo = inimigo_escolhido.vida
  while True:
    vida_inimigo -= dano_turnoJogador("turno_jogador")
    if vida_inimigo > 0 and vida_inimigo <= 0.30*inimigo_escolhido.vida:
      print(f'{cor("yl")}Seu inimigo está enfraquecido! Lhe resta {cor("red")}{vida_inimigo} de vida{cor("reset")}\n') 
    if vida_inimigo > 0 and vida_inimigo > 0.30*inimigo_escolhido.vida:
      print(f'{cor("yl")}Seu inimigo está com {cor("red")}{vida_inimigo} {cor("yl")}de vida{cor("reset")}')
    if vida_inimigo <= 0:
      print(f'{cor("gr")}Parabéns, você derrotou o adversário!{cor("reset")}')
      return True
    vida_jogador -= dano_turnoAdversário("turno_adversario")
    if vida_jogador > 0 and vida_jogador <= 0.30*classe_escolhida.vida:
      print(f'\n{cor("yl")}Você está enfraquecido! Restam apenas {cor("red")}{vida_jogador} de vida{cor("reset")}\n')
    if  vida_jogador > 0 and vida_jogador > 0.30*classe_escolhida.vida:
      print(f'\n{cor("yl")}Você está com {cor("red")}{vida_jogador} {cor("yl")}de vida{cor("reset")}\n')
    if vida_jogador <= 0:
      print(f'{cor("red")}Você foi derrotado!{cor("reset")}')
      return True

# Introduz o combate inicial após escolha da classe
def combate():
  if inimigo_batalha.nome == "Aranha":
    mensagem_inicial = f"\n{cor("cy")}《 Seu primeiro inimigo é uma{cor("reset")} {inimigo_batalha.nome}{emojis(inimigo_batalha.nome)}{cor("cy")}》{cor("reset")}"
  else:
    mensagem_inicial = f"\n{cor("cy")}《 Seu primeiro inimigo é um{cor("reset")} {inimigo_batalha.nome}{emojis(inimigo_batalha.nome)}{cor("cy")} 》{cor("reset")}"
  texto_anim(mensagem_inicial)
  ataque = {1: "Você ataca primeiro!", 2: "O inimigo ataca primeiro!"}
  primeiro_ataque = choice(list(ataque.values()))
  if primeiro_ataque == "Você ataca primeiro!":
    turno_jogador()
  if primeiro_ataque == "O inimigo ataca primeiro!":
    turno_adversario()

main()
combate()
