
def take_value():
    value = input('Введите число: ')
    try:
        value = float(value)
        return value
    except ValueError:
        print('Это не число. Попробуйте снова...')
        return take_value()

# def zero_err():
#     try:
#         model_div.div()
#     except ZeroDivisionError:
#         print('Делить на ноль нельзя')
