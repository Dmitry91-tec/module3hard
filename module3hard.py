data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),"Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = data_structure
def open_list(list_):
    global result
    for i in list_:
        result.extend([i])
    return

def open_int(int_):
    global result
    return result.extend([int_])
def open_str(str_):
    global result
    str_ = len(str_)
    return result.extend([str_])
def open_dict(dict_):
    global result
    k_v_pairs = [(k, v) for k, v in dict_.items()]                             # Кортежи с парами ключ-значение
    flat_list = [element for pair in dict_.items() for element in pair]        # Плоский список с ключами и значениями
    return result.extend(flat_list)

def open_tuple(tuple_):
    global result
    tuple_ = list(tuple_)
    return result.extend(tuple_)
def open_set(set_):
    global result
    set_ = list(set_)
    return result.extend(set_)
def calculate_structure_sum(result):
    if all(type(x) == int for x in result):                          #проверка, что все элементы списка цифры
        print(sum(result))                                           #Правда, то вычисляемих сумму
    else:
        #print('Не все совпадают')                                   #Ложь, перебираем элементы, удалем из списка, раскрываем и добавляем в конец списка
        for i in result:
            if isinstance(i, list):
                open_list(i)
                result.remove(i)
            elif isinstance(i, tuple):
                open_tuple(i)
                result.remove(i)
            elif isinstance(i, str):
                open_str(i)
                result.remove(i)
            elif isinstance(i, dict):
                open_dict(i)
                result.remove(i)
            elif isinstance(i, int):
                open_int(i)
                result.remove(i)
            elif isinstance(i, set):
                open_set(i)
                result.remove(i)
        return calculate_structure_sum(result)

calculate_structure_sum(data_structure)


