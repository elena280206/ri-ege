n = input()
range = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
vowels = 0
consonant = 0
for i in n:
    if i in range:
        vowels += 1
    else:
        consonant += 1
print(vowels, consonant)