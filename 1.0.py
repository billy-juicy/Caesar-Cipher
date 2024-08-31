# Пропишем алфавиты на русском и английском с двумя регистрами
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"] # Не забудем написать также символы

# Пропишем запросы вводной информации
language = input('Выберите язык: английский - eng или русский - rus ')
cipher = input('Выберите шифрование: зашифровать - encrypt или расшифровать - decrypt ')
shift = int(input('Введите сдвиг: '))
text = input('Введите текст: ')

# Создадим функцию
def my_cipher(language, cipher, shift, text):
    if language == 'eng':
        power = 26 # Переменная power означает мощность алфавита
    if language == 'rus':
        power = 32
    if cipher == 'decrypt':
        shift = -shift # Если мы расшифровываем текст, то сдвиг будет со знаком "-"
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i] == text[i].upper():
                for j in range(power):
                    if power == 32:
                        if text[i] == rus_upper_alphabet[j]:
                            print(rus_upper_alphabet[(j + shift) % power], end='')
                            break
                    if power == 26:
                        if text[i] == eng_upper_alphabet[j]:
                            print(eng_upper_alphabet[(j + shift) % power], end='')
                            break
            else:
                for j in range(power):
                    if power == 32:
                        if text[i] == rus_lower_alphabet[j]:
                            print(rus_lower_alphabet[(j + shift) % power], end='')
                            break
                    if power == 26:
                        if text[i] == eng_lower_alphabet[j]:
                            print(eng_lower_alphabet[(j + shift) % power], end='')
                            break
        else:
            print(text[i], end='')

# Вызываем функцию
my_cipher(language, cipher, shift, text)