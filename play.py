import random


def guess_number_game():
  number_to_guess = random.randint(1, 100)
  attempts = 0

  print("Привет! Я загадал число от 1 до 100. Попробуй угадать.")

  while True:
    try:
      user_guess = int(input("Введи свой вариант: "))
      attempts += 1

      if user_guess < number_to_guess:
        print("Мое число больше.")
      elif user_guess > number_to_guess:
        print("Мое число меньше.")
      else:
        print(f"Поздравляю! Ты угадал число за {attempts} попыток.")
        break
    except ValueError:
      print("Пожалуйста, введи целое число.")


guess_number_game()
