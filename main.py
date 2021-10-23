import random

# Набор доступных символов
ARRAY_SYMBOLS = [
    '0', '1', '2', '3', '4',
    '5', '6', '7', '8', '9',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z',
    '!', '@', '_', '.', '*', '^', '$', '#', '&', '?', '+', '=', '~', '-']

# Получение кол-ва символов в пароле
COUNT_SYMBOLS = 4
input_count = input('Введите кол-во символов в пароле: ')
if input_count.isdigit():
    count_symbols = int(input_count)
else:
    count_symbols = COUNT_SYMBOLS

# Узн колво всех возм комбинаций
count_variant = len(ARRAY_SYMBOLS) ** count_symbols


# Получ рандом символ
def random_symbols():
    return ARRAY_SYMBOLS[
        random.randint(0, len(ARRAY_SYMBOLS) - 1)
    ]


print(f'Версия программы: v0.0.1')
print(f'Кол-во доступных символов: {len(ARRAY_SYMBOLS)}')
# print(f'Доступные символы: {ARRAY_SYMBOLS}')
print(f'Кол-во возможных комбинаций: {count_variant}')

password = ''

# ген уник пароля
for i in range(0, count_symbols):
    password = password + f'{random_symbols()}'

print(f'Сгенерированный пароль: {password}')

# Запись пароля в файл
with open('password.txt', 'a') as password_string:
    password_string.write('{}\n'.format(f'{password}'))
