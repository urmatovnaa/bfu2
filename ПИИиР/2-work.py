def go_to_finish():
    print('Ура! Вы добрались до дома бабушки')
    print('Попробуете еще раз?')
    answer = input()
    if answer == 'Да':
        go_to_start()
    else:
        exit()

def go_to_cave():
    print('Упс! Вас съел медведь')
    print('Попробуете еще раз?')
    answer = input()
    if answer == 'Да':
        go_to_start()
    else:
        exit()

def go_to_forest():
    print('Идем по лесу')
    print('Идем в пещеру?')
    answer = input()
    if answer == 'Да':
        go_to_cave()
    else:
        go_to_finish()

def go_to_swamp():
    print('Упс! Вы утанули')
    print('Попробуете еще раз?')
    answer = input()
    if answer == 'Да':
        go_to_start()
    else:
        exit()

def go_to_plain():
    print('Идем по равнине')
    print("Идем в болото?")
    answer = input()
    if answer == "Да":
        go_to_swamp()
    else:
        go_to_finish()

def go_to_start():
  print('Вы - красная шапочка, и ваша цель добраться до дома бабушки')
  print('Идем в лес?')
  answer = input()
  if answer == 'Да':
    go_to_forest()
  else:
    go_to_plain()

def main():
  go_to_start()

main()
