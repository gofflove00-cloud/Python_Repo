def square(side):
    return side * side


user_input = input('введите длину стороны квадрата: ')

try:
    side_length = float(user_input)
    if side_length < 0:
        print('Ошибка! Длина стороны не может быть отрицательной!')
    else:
        if side_length != int(side_length):
            side_length = int(side_length) + 1
        else:
            side_length = int(side_length)

        result = square(side_length)
        print(f'Квадрат со стороной {side_length} имеет площадь {result}')

except ValueError:
    print('Пожалуйста, при вводе длины стороны используйте только цифры')
