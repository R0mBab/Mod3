

calls_one = 0
calls_two = 0
def count_calls_one():
    global calls_one
    calls_one += 1
def count_calls_two():
    global calls_two
    calls_two += 1


def string_info(input_string):
    length = len(input_string) #длина
    upper_str = input_string.upper() #Верхний регистр
    lower_str = input_string.lower() #Нижний регистр
    count_calls_one()
    return (length, upper_str, lower_str)


def  is_contains(string, list_to_search):
    if string.lower() in list_to_search.lower():
        count_calls_two()
        return True
    else:
        count_calls_two()
        return False


for i in range(12):
    print(string_info('Hello world'))


for k in range(3):
    print(is_contains('5', '13, 94, Members'))


print(calls_one,calls_two)