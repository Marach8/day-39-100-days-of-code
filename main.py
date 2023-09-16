import os, time, random

def game():
  k = '\033[4mINSTRUCTIONS\033[0m'
  print(f'{k:^40}')
  print()
  
  print('''You have chosen a random name from a list of names of people. You are to choose letters that are in the name you have chosen😎. Goodluck!
  \033[35mGame Loading...\033[0m''')
  print()
  time.sleep(10)
  os.system('clear')
  
  a = '\033[4mTHE HANGMAN GAME\033[0m'
  print(f'{a:^40}')
  print()
  
  words = ['jane', 'noah', 'paul', 'elias', 'miracle', 'john', 'mary', 'daniel', 'gabriel', 'mark']
  
  y = 0
  a = random.choice(words)
  time.sleep(2)
  print(f'''\033[34mAs a hint, the first and last letters of the name are "{a[0]}" and "{a[len(a)-1]}". Also, the name has {len(a)} letters''')
  time.sleep(1)
  c = []
  h = 0
  for e in a:
    c.append('_')
  pics = ["  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
  
          "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
  
          "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 
  
          "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",
  
          "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",
  
          "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 
  
  def printer():
    print()
    for d in c:
      print(f'\033[32m{d}\033[0m', end='')
    print
  

  while y <= 5:
    print()
    print()
    ask = input('\033[0mChoose a letter: ').lower()
    
    if ask in a:
      b = a.index(ask)
      if ask not in c:
        c[b] = ask
        h += 1
        print('\033[32mCorrect! You found a letter😊')
      else:
        print('\033[33mYou have chosen that letter before🙄🙄. Choose another\033[0m')
      
    else:
      print()
      print('\033[31mNope, not in there!')
      print
      print(pics[y])
      y += 1
      time.sleep(1)
      if (6-y) == 1:
        print(f'You have {6-y} life remaining!😢')
      elif (6-y) == 0:
        print('''You have hung yourself completely and you have no life remaining. See you in the underworld!😭😭''')
      else:
        print(f'You have {6-y} lives remaining!😢')
      printer()
      continue
      
    printer()
    
    if h == len(a):
      print()
      print(f'Hurray! 🤩🤩You have won with {6-y} lives left.')
      break

while True:
  game()
  print()
  time.sleep(4)
  ask = input('Do you want to play again? y/n: ')
  if ask == 'y':
    os.system('clear')
    time.sleep(1)
    continue
  else:
    time.sleep(1.5)
    break
print()
print('Byeee! Hope You had a good time playing our HANGMAN game😎😎')