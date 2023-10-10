def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': substract,
    '*': multiply,
    '/': divide
}

def calculation():
    num1 = float(input('Write the 1st number: '))
    num2 = float(input('Write the 2nd number: '))

    for i in operations:
        print(i)

    operation_symbol = input('Choose an opertion: ')
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f'{num1} {operation_symbol} {num2} = {answer}')

    a = True
    while a:
        option = input('Do you want to do another calculation? yes / reset / no: ').lower()
        if option == 'yes':
            operation_symbol = input('Choose an opertion: ')
            num3 = float(input('Write the next number: '))
            calculation_function = operations[operation_symbol]
            second_answer = calculation_function(answer, num3)
            print(f'{answer} {operation_symbol} {num3} = {second_answer}')
            answer = second_answer
        elif option == 'reset':
            calculation()
        else:
            a = False


calculation()