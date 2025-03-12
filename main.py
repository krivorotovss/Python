import pandas as pd

# # Открываем файл
# input_file_path = 'D:\\test\\output.csv'  # замените на ваш файл
#
# # Читаем CSV файл
# data = pd.read_csv(input_file_path)
#
# # Преобразуем каждую строку в список и добавляем в общий список
# result = data.values.tolist()
#
# # Выводим полученные данные
# for row in result: # row - это строка из CSV в виде списка
#     print(row)
#     prefix = str(row[1])
#     center_start = str(row[2])
#     center_end = str(row[3])





# Печатающий метод
def write_in_file():
    pass

# Выводит простой диапазон 9237000000 - 9237099999 - 792370.{5}
def simple_range(prefix_number, result_list_middle_part_range, number_suffix, range_start_diffirence):
    suffix = f"{{{number_suffix}}}"
    middle_part_number = ''.join(result_list_middle_part_range) + ''.join(range_start_diffirence)[:-number_suffix]

    if number_suffix != 0:
        result = f"7{prefix_number}{middle_part_number}.{suffix}"
    else:
        result = f"7{prefix_number}{middle_part_number}"

    print(result)
    list_numbers_ranges0.append(result)


# Выводит простой диапазон 9232200000 - 9232599999 - 79232[2-5].{5}
def simple_range1(prefix_number, result_list_middle_part_range, number_suffix, range_start_diffirence,
                  range_end_diffirence):
    # Цифры диапазона добавленные в скобках [1-9]
    range_start_digit = ''.join(range_start_diffirence[0])
    range_end_digit = ''.join(range_end_diffirence[0])
    range_digits = f"[{range_start_digit}-{range_end_digit}]"

    suffix = f"{{{number_suffix}}}"
    middle_part_number = ''.join(result_list_middle_part_range)
    result = f"7{prefix_number}{middle_part_number}{range_digits}.{suffix}"
    print(f"7{prefix_number}{middle_part_number}{range_digits}.{suffix}")
    list_numbers_ranges1.append(result)


def simple_range2(prefix_number, result_list_middle_part_range, number_suffix, range_start_diffirence,
                  range_end_diffirence):
    # Цифры диапазона добавленные в скобках [1-9]
    range_start_digit = ''.join(range_start_diffirence[1])
    range_end_digit = ''.join(range_end_diffirence[1])
    range_digits = f"[{range_start_digit}-{range_end_digit}]"

    suffix = f"{{{number_suffix}}}"
    middle_part_number = ''.join(result_list_middle_part_range) + ''.join(range_start_diffirence[0])
    result = f"7{prefix_number}{middle_part_number}{range_digits}.{suffix}"
    print(result)
    list_numbers_ranges2.append(result)


def simple_range3(prefix_number, result_list_middle_part_range, number_suffix, range_start_diffirence,
                      range_end_diffirence):
    range_start_digit = ''.join(range_start_diffirence[2])
    range_end_digit = ''.join(range_end_diffirence[2])
    range_digits = f"[{range_start_digit}-{range_end_digit}]"

    suffix = f"{{{number_suffix}}}"
    middle_part_number = ''.join(result_list_middle_part_range) + ''.join(range_start_diffirence[0]) + ''.join(range_start_diffirence[1])
    result = f"7{prefix_number}{middle_part_number}{range_digits}.{suffix}"
    print(result)
    list_numbers_ranges3.append(result)


def simple_range4(prefix_number, result_list_middle_part_range, number_suffix, range_start_diffirence, range_end_diffirence):
    range_start_digit = ''.join(range_start_diffirence[3])
    range_end_digit = ''.join(range_end_diffirence[3])
    range_digits = f"[{range_start_digit}-{range_end_digit}]"

    suffix = f"{{{number_suffix}}}"
    middle_part_number = ''.join(result_list_middle_part_range) + ''.join(range_start_diffirence[0]) + ''.join(
        range_start_diffirence[1]) + ''.join(range_start_diffirence[2])
    result = f"7{prefix_number}{middle_part_number}{range_digits}.{suffix}"
    print(result)
    list_numbers_ranges4.append(result)


def simple_range5(prefix_number, result_list_middle_part_range, number_suffix, range_start_diffirence, range_end_diffirence):
    range_start_digit = ''.join(range_start_diffirence[4])
    range_end_digit = ''.join(range_end_diffirence[4])
    range_digits = f"[{range_start_digit}-{range_end_digit}]"

    suffix = f"{{{number_suffix}}}"
    middle_part_number = ''.join(result_list_middle_part_range) + ''.join(range_start_diffirence[0]) + ''.join(
        range_start_diffirence[1]) + ''.join(range_start_diffirence[2] + ''.join(range_start_diffirence[3]))
    result = f"7{prefix_number}{middle_part_number}{range_digits}.{suffix}"
    print(result)
    list_numbers_ranges5.append(result)


def simple_range6(prefix_number, result_list_middle_part_range, number_suffix, range_start_diffirence, range_end_diffirence):
    range_start_digit = ''.join(range_start_diffirence[5])
    range_end_digit = ''.join(range_end_diffirence[5])
    range_digits = f"[{range_start_digit}-{range_end_digit}]"

    suffix = f"{{{number_suffix}}}"
    middle_part_number = ''.join(result_list_middle_part_range) + ''.join(range_start_diffirence[0]) + ''.join(
        range_start_diffirence[1]) + ''.join(range_start_diffirence[2] + ''.join(range_start_diffirence[3])+ ''.join(range_start_diffirence[4]))
    result = f"7{prefix_number}{middle_part_number}{range_digits}.{suffix}"
    print(result)
    list_numbers_ranges6.append(result)


def simple_range7(prefix_number, result_list_middle_part_range, number_suffix, range_start_diffirence, range_end_diffirence):
    range_start_digit = ''.join(range_start_diffirence[6])
    range_end_digit = ''.join(range_end_diffirence[6])
    range_digits = f"[{range_start_digit}-{range_end_digit}]"

    suffix = f"{{{number_suffix}}}"
    middle_part_number = ''.join(result_list_middle_part_range) + ''.join(range_start_diffirence[0]) + ''.join(
        range_start_diffirence[1]) + ''.join(range_start_diffirence[2] + ''.join(range_start_diffirence[3]) + ''.join(range_start_diffirence[4]) + ''.join(range_start_diffirence[5]))
    result = f"7{prefix_number}{middle_part_number}{range_digits}.{suffix}"
    print(result)
    list_numbers_ranges7.append(result)


def simple_range8(prefix_number, result_list_middle_part_range, number_suffix, range_start_diffirence,
                  range_end_diffirence):
    range_start_digit = ''.join(range_start_diffirence[7])
    range_end_digit = ''.join(range_end_diffirence[7])
    range_digits = f"[{range_start_digit}-{range_end_digit}]"

    suffix = f"{{{number_suffix}}}"
    middle_part_number = ''.join(result_list_middle_part_range) + ''.join(range_start_diffirence[0]) + ''.join(
        range_start_diffirence[1]) + ''.join(
        range_start_diffirence[2] + ''.join(range_start_diffirence[3]) + ''.join(range_start_diffirence[4]) + ''.join(
            range_start_diffirence[5]) + ''.join(range_start_diffirence[6]))
    result = f"7{prefix_number}{middle_part_number}{range_digits}.{suffix}"
    print(result)
    list_numbers_ranges8.append(result)



def range_method(prefix_number, result_list_middle_part_range, number_suffix, range_start_diffirence, range_end_diffirence):
    if range_start_diffirence[:number_suffix + 1] != range_end_diffirence[:number_suffix + 1]:
        range_start_digit = ''.join(range_start_diffirence[:number_suffix + 1])
        range_end_digit = ''.join(range_end_diffirence[:number_suffix + 1])
        range_digits = f"[{range_start_digit}-{range_end_digit}]"

        suffix = f"{{{number_suffix}}}"
        middle_part_number = ''.join(result_list_middle_part_range) + ''.join(range_start_diffirence[0])
        print(f"7{prefix_number}{middle_part_number}{range_digits}.{suffix}")
    else:
        suffix = f"{{{number_suffix}}}"
        middle_part_number = ''.join(result_list_middle_part_range) + ''.join(range_start_diffirence)[:-number_suffix]
        result = f"7{prefix_number}{middle_part_number}.{suffix}"
        print(result)
        list_numbers_ranges9.append(result)




def number_normalisation(middle_part_str):
    print("номер короче 7знаков")
    new_list = list(middle_part_str)
    length_difference = 7 - len(middle_part_str)

    for i in range(length_difference):
        new_list.insert(0, "0")

    return "".join(new_list)


def find_number_suffix(number_suffix, range_start_diffirence, range_end_diffirence):
    # try:
        for i in range(len(range_start_diffirence) - 1, -1, -1):
            if range_start_diffirence[i] == "0" and range_end_diffirence[i] == "9":
                number_suffix += 1
            else:
                break

        return number_suffix
    # except IndexError:
    #     print(f"Ошибка: индекс {range_start_diffirence} выходит за пределы строки.")
    #     print(f"Ошибка: индекс {range_end_diffirence} выходит за пределы строки.")


# TODO
def range_definition(prefix_number, number_suffix, general_list_middle_part_range, numbers_range, range_start_diffirence, range_end_diffirence, check_flag):
    # Проверить, что количеству "0" соответствует такое же количество "9", находим значение суффикса номера
    number_suffix = 0
    print("===============range_definition============")
    number_suffix = find_number_suffix(number_suffix, range_start_diffirence, range_end_diffirence)
    print(f"number_suffix = {number_suffix}")

    if range_start_diffirence == "":
        range_start_diffirence = "0"

    if range_end_diffirence == "":
        range_end_diffirence = "0"

    # Проверка есть ли в стартовом диапазоне столько же нулей свободных, сколько результат numbers_range (количество номеров в диапазоне)
    range_size = int(''.join(range_end_diffirence)) - int(''.join(range_start_diffirence)) + 1
    print(f"range_size = {range_size}")
    print(f"range_start_diffirence = {range_start_diffirence}")
    print(f"range_end_diffirence = {range_end_diffirence}")

    # try:
    if 10 ** number_suffix == range_size:
        print("============true simple_range()============")
        simple_range(prefix_number, general_list_middle_part_range, number_suffix, range_start_diffirence)
    elif range_start_diffirence[0] != range_end_diffirence[0] and range_start_diffirence[1] == "0" and range_end_diffirence[1] == "9":
        print("============true_simple_range1()============")
        simple_range1(prefix_number, general_list_middle_part_range, number_suffix, range_start_diffirence,
                      range_end_diffirence)
    elif range_start_diffirence[0] == range_end_diffirence[0] and range_start_diffirence[1] != range_end_diffirence[1]:
        print("============true_simple_range2()============")
        simple_range2(prefix_number, general_list_middle_part_range, number_suffix, range_start_diffirence,
                      range_end_diffirence)
    elif range_start_diffirence[0] == range_end_diffirence[0] and range_start_diffirence[1] == range_end_diffirence[1] and range_start_diffirence[2] != range_end_diffirence[2]:
        print("============true_simple_range3()============")
        simple_range3(prefix_number, general_list_middle_part_range, number_suffix, range_start_diffirence,
                      range_end_diffirence)
    elif range_start_diffirence[0] == range_end_diffirence[0] and range_start_diffirence[1] == range_end_diffirence[1] and range_start_diffirence[2] == range_end_diffirence[2] and range_start_diffirence[3] != range_end_diffirence[3]:
        print("============true_simple_range4()============")
        simple_range4(prefix_number, general_list_middle_part_range, number_suffix, range_start_diffirence, range_end_diffirence)

    elif range_start_diffirence[0] == range_end_diffirence[0] and range_start_diffirence[1] == range_end_diffirence[1] and range_start_diffirence[2] == range_end_diffirence[2] and range_start_diffirence[3] == range_end_diffirence[3] and range_start_diffirence[4] != range_end_diffirence[4]:
        print("============true_simple_range5()============")
        simple_range5(prefix_number, general_list_middle_part_range, number_suffix, range_start_diffirence, range_end_diffirence)
    elif range_start_diffirence[0] == range_end_diffirence[0] and range_start_diffirence[1] == range_end_diffirence[1] and range_start_diffirence[2] == range_end_diffirence[2] and range_start_diffirence[3] == range_end_diffirence[3] and range_start_diffirence[4] == range_end_diffirence[4] and range_start_diffirence[5] != range_end_diffirence[5]:
        print("============true_simple_range6()============")
        simple_range6(prefix_number, general_list_middle_part_range, number_suffix, range_start_diffirence, range_end_diffirence)
    elif range_start_diffirence[0] == range_end_diffirence[0] and range_start_diffirence[1] == range_end_diffirence[1] and range_start_diffirence[2] == range_end_diffirence[2] and range_start_diffirence[3] == range_end_diffirence[3] and range_start_diffirence[4] == range_end_diffirence[4] and range_start_diffirence[5] == range_end_diffirence[5] and range_start_diffirence[6] != range_end_diffirence[6]:
        print("============true_simple_range7()============")
        simple_range7(prefix_number, general_list_middle_part_range, number_suffix, range_start_diffirence, range_end_diffirence)
    elif range_start_diffirence[0] == range_end_diffirence[0] and range_start_diffirence[1] == range_end_diffirence[1] and range_start_diffirence[2] == range_end_diffirence[2] and range_start_diffirence[3] == range_end_diffirence[3] and range_start_diffirence[4] == range_end_diffirence[4] and range_start_diffirence[5] == range_end_diffirence[5] and range_start_diffirence[6] == range_end_diffirence[6] and range_start_diffirence[7] != range_end_diffirence[7]:
        print("============true_simple_range8()============")
        simple_range8(prefix_number, general_list_middle_part_range, number_suffix, range_start_diffirence, range_end_diffirence)
    elif number_suffix == 0:
        print(f"не удалось обработать диапазон - {prefix_number} {range_start_diffirence} {range_end_diffirence}")
        list_numbers_ranges0.append(f"не удалось обработать диапазон - {prefix_number} {''.join(map(str,general_list_middle_part_range))}{range_start_diffirence} - {''.join(map(str,general_list_middle_part_range))}{range_end_diffirence}")
    elif check_flag == True:
            range_method(prefix_number, general_list_middle_part_range, number_suffix, range_start_diffirence, range_end_diffirence)
    else:
        print("============распознан сложный номер===========")

        # # Нужно на основе известного суффикса вычислить, нужно ли искать другой конец диапазона
        # # for i in range(len(range_start_diffirence), -1, -1):
        # test_range_start_diffirence = range_start_diffirence[:-3]
        # test_range_end_diffirence = range_end_diffirence[:-3]
        # print(f"test_range_start_diffirence - suffix = {test_range_start_diffirence}")
        # print(f"test_range_end_diffirence - suffix = {test_range_end_diffirence}")
        #
        # if len(range_start_diffirence[:-number_suffix]) > 1:
        #     # TODO слишком рано находится суффикс для больших диапазонов ???
        #     # TODO придумать условие для входа в расчет нового конца диапазона
        #     range_end_diffirence = find_next_end_of_range(prefix_number, number_suffix, general_list_middle_part_range,
        #                                                   numbers_range, range_start_diffirence, range_end_diffirence)

        # Нужно новый диапазон разделить на обрабатываемые уже диапазоны

        # 995	3465000	3479999 -------- 7995346[5-9].{3}, 7995347.{4}
        # 3465000 - 34569999 и 34570000 - 34579999

        # TODO
        # мы знаем размер диапазона - 15000, те больше нельзя
        # мы знаем старт диапазона и конец, нам нужно нижнюю границу догнать до девяток, известна разная часть 65000, известна следующая цифра 7 - 79999
        # берем следующую цифру (7) и заполняем ее нулями, проверяем, что не вышли за диапазон 15000, считаем 70000 - 65000 = 5000.
        # Раз мы в диапазоне, то вычитаем из 70000 - 1 = 69999 - запоминаем в переменную, рекурсивно вызываем главный метод
        # Теперь создаем вторую переменную, в нее записываем диапазон 79999 - 70000 = 9999 + 1. Проверяем что 15000 - 5000 - 10000 == 0
        # Рекурсивно вызываем главный метод

        # Нужно склеить обратно general часть с обоими диапазонами
        # range_start_diffirence = general_list_middle_part_range + range_start_diffirence
        # range_end_diffirence = general_list_middle_part_range + range_end_diffirence
        # print("склейка номера")
        # print(range_start_diffirence)
        # print(range_end_diffirence)

        splitting_large_ranges(range_start_diffirence, range_end_diffirence, number_suffix, prefix_number, numbers_range, general_list_middle_part_range, check_flag)
    # except TypeError:
    #     print("unsupported operand type(s) for ** or pow(): 'int' and 'NoneType'")
    # except IndexError:
    #     print("string index out of range")


def suffix_calculation(prefix_number, middle_part_start, middle_part_end, general_list_middle_part_range):
    print("==========suffix_calculation============")
    # TODO здесь нужно отдельный метод
    # print(type(middle_part_end))
    if type(middle_part_end) != int:
        middle_part_end = (''.join(map(str, middle_part_end)))

    if type(middle_part_start) != int:
        middle_part_start = int(''.join(map(str, middle_part_start)))
    print(f"middle_part_start = {middle_part_start}")
    print(f"middle_part_end = {middle_part_end}")


    # Находим размер диапазона - кол-во номеров в нем
    numbers_range = int(middle_part_end) - int(middle_part_start) + 1
    print(numbers_range)

    # Переводим данные в строковые для списков
    middle_part_start_str = f"{middle_part_start}"
    middle_part_end_str = f"{middle_part_end}"
    list_range_start = list(middle_part_start_str)
    list_range_end = list(middle_part_end_str)

    # Нужно учесть, что номер без префикса может быть короче 7 знаков в таблице, тогда нужно добавить нули перед номером
    if len(middle_part_start_str) < 7:
        list_range_start = number_normalisation(middle_part_start_str)

    if len(middle_part_end_str) < 7:
        list_range_end = number_normalisation(middle_part_end_str)

    print(f"list_range_start = {list_range_start}")
    print(f"list_range_end = {list_range_end}")

    # Нахождение общей части номера
    general_list_middle_part_range = []

    for i in range(len(list_range_start)):
        if list_range_start[i] == list_range_end[i]:
            general_list_middle_part_range.append(list_range_start[i])
        else:
            break

    # print(general_list_middle_part_range)

    # Отрезаем общую часть номера
    range_start_diffirence = list_range_start[len(general_list_middle_part_range):]
    print(range_start_diffirence)
    range_end_diffirence = list_range_end[len(general_list_middle_part_range):]
    print(range_end_diffirence)

    number_suffix = 0
    check_cycle_flag = False
    range_definition(prefix_number, number_suffix, general_list_middle_part_range, numbers_range, range_start_diffirence, range_end_diffirence, check_cycle_flag)






def check_out_of_range(numbers_range, prefix_number, number_suffix, general_list_middle_part_range,middle_part_start, middle_part_end):
    print("===IN=========check_out_of_range=============")
    list_real_end_of_range = list(str(int_real_end_of_range))

    print(f"list_real_end_of_range[len(list_real_end_of_range):] = {list_real_end_of_range[:len(general_list_middle_part_range)]}")

    # Здесь вычитаются первые знаки, наверное, если general_list_middle_part_range != числу на которое начинается list_real_end_of_range, то general_list_middle_part_range не нужно обрезать
    if general_list_middle_part_range == list_real_end_of_range[:len(general_list_middle_part_range):]:
        modified_list_real_end_of_range = list_real_end_of_range[len(general_list_middle_part_range):]
        print("modify")
    else:
        modified_list_real_end_of_range = list_real_end_of_range
        print("UNmodify")

    print("modified_list_real_end_of_range")
    print(modified_list_real_end_of_range)
    int_modified_list_real_end_of_range = int(''.join(map(str, modified_list_real_end_of_range)))
    print(f"int_modified_list_real_end_of_range = {int_modified_list_real_end_of_range}")
    int_middle_part_end = int(''.join(map(str, list(middle_part_end))))
    print(f"int_middle_part_end = {int_middle_part_end}")

    if int(int_middle_part_end) > int(int_modified_list_real_end_of_range):
        print("---выход из диапазона---")
        middle_part_end = f"{int_modified_list_real_end_of_range}"

    print(f"middle_part_start = {middle_part_start}")
    print(f"middle_part_end = {middle_part_end}")

    # Вычисляем для проверки, сколько номеров осталось не обработано из диапазона
    print(type(middle_part_start))
    print(type(middle_part_end))
    if type(middle_part_start) != str:
        middle_part_start = ''.join(map(str, middle_part_start))

    numbers_range1 = (int(middle_part_end) - int(middle_part_start) + 1)
    print(f"numbers_range1 = {numbers_range1}")
    numbers_range = numbers_range - (int(middle_part_end) - int(middle_part_start) + 1)
    print(f"numbers_range = {numbers_range}")

    # TODO Перед передачей номер нужно обратно склеить с общей частью, но это неточно 28.20.25
    print(type(general_list_middle_part_range))
    # general_part_numbers = "".join(map(str, general_list_middle_part_range))

    # middle_part_start = general_part_numbers + middle_part_start
    # middle_part_end = general_part_numbers + middle_part_end

    print(f"middle_part_start = {middle_part_start}")
    print(f"middle_part_end = {middle_part_end}")

    # suffix_calculation(prefix_number, middle_part_start, middle_part_end, general_list_middle_part_range)
    # range_definition(prefix_number, number_suffix, general_list_middle_part_range, numbers_range, middle_part_start,
    #                  middle_part_end)
    print("====OUT=====check_out_of_range======")

    return numbers_range, middle_part_end




def splitting_large_ranges(range_start_diffirence, range_end_diffirence, number_suffix, prefix_number, numbers_range, general_list_middle_part_range, check_flag):
    # Принимаем сложный диапазон чисел, берем нижнюю границу, узнаем размер суффикса, по размеру суффикса назначаем конец диапазона, затем сравниваем конец диапазона
    # Вычитаем из верхней границы нижнюю, количество знаков разницы - 1 и есть наш новый суффикс
    # с реальным концом, если он меньше, то продолжаем работать с ним, если больше, то назначаем сам конец диапазона
    # range_definition() приводит сюда
    count = 0
    # new_suffix = len(str(int(numbers_range / 10)))
    # new_range_start_diffirence = range_start_diffirence
    new_list_num_end = 0

    while numbers_range > 0:
        check_flag = True
        print("================splitting_large_ranges================")
        print(f"range_start_diffirence = {range_start_diffirence}")
        print(f"general_list_middle_part_range = {general_list_middle_part_range}")

        new_range_start_diffirence = range_start_diffirence


        new_suffix = find_number_suffix(0, range_start_diffirence, range_end_diffirence) + 1
        # Подсчет количества порядков в числе номеров, пример 1000 - это 3 порядка
        new_suffix1 = int(len(str(numbers_range))) - 1

        # Нужно для компенсации одного или другого суффикса
        if new_suffix > new_suffix1:
            new_suffix = new_suffix1

        # Вычисляем новый суффикс для поддиапазона
        # new_suffix = len(str(int(numbers_range / 10)))
        # new_suffix = len(str(int(numbers_range)))
        # new_suffix = number_suffix
        print(f"new_suffix = {new_suffix}")

        list_num_start = list(new_range_start_diffirence)[:-new_suffix]
        print(f"list_num_start = {list_num_start}")


        # вычисляем новый конец поддиапазона
        new_list_num_end = list_num_start
        for i in range(len(list_num_start), len(new_range_start_diffirence)):
            new_list_num_end.append("9")
        print(f"new_list_num_end = {new_list_num_end}")

        middle_part_start = f"{''.join(new_range_start_diffirence)}"
        middle_part_end = f"{''.join(new_list_num_end)}"
        print(type(middle_part_end))
        print(f"middle_part_end = {middle_part_end}")
        print(type(middle_part_start))
        print(f"middle_part_start = {middle_part_start}")



        # Проверка, что мы не вышли за пределы диапазона, для этого нужно отклеить общую часть от real_end_of_list_range
        # И подсчет numbers_range - остатка номеров в диапазоне
        # numbers_range = check_out_of_range(numbers_range, prefix_number, number_suffix, general_list_middle_part_range, middle_part_start, middle_part_end)

        check_out = int(middle_part_end) - int(middle_part_start) + 1
        print(f"check_out = {check_out}")

        if int(middle_part_end) - int(middle_part_start) + 1 > numbers_range:
            numbers_range, middle_part_end = check_out_of_range(numbers_range, prefix_number, number_suffix, general_list_middle_part_range, middle_part_start, middle_part_end)
        else:
            numbers_range = numbers_range - (int(middle_part_end) - int(middle_part_start) + 1)


        range_definition(prefix_number, number_suffix, general_list_middle_part_range, numbers_range, middle_part_start, middle_part_end, check_flag)

        # Здесь нужно поменять границы диапазона
        print(type(middle_part_end))
        print(f"middle_part_end = {middle_part_end}")
        range_start_diffirence = str(int(middle_part_end) + 1)
        # for i in range(len(middle_part_start)-1, -1, -1):
        #     if middle_part_start[i] == "0":
        #         middle_part_end[i] = "9"

        count += 1
        print(f"count = {count}")

        print(f"numbers_range = {numbers_range}")
        if numbers_range <= 0:
            print("Завершение цикла, нумерация исчерпана")
            break




# Обединение диапазонов
def union_ranges(list_numbers_result, list_numbers_ranges, list_numbers_ranges0, list_numbers_ranges2, list_numbers_ranges3, list_numbers_ranges4, list_numbers_ranges5, list_numbers_ranges6, list_numbers_ranges7, list_numbers_ranges8, list_numbers_ranges9, list_numbers_ranges10):
    # dot_index = list_numbers_ranges0[0].find('.')
    # print(f"dot_index = {dot_index}")

    print("=================================================================================")
    print("=================================================================================")
    print("=================================================================================")
    print("=================================================================================")

    index = 0
    while list_numbers_ranges0:
        dot_index = list_numbers_ranges0[0].find('.')
        print(f"dot_index = {dot_index}")

        list_numbers_ranges = []
        print(f"index = {index}")
        elems_list = list_numbers_ranges0[index]
        list_indexes = []
        # print(f"elems_list = {elems_list}")

        list_size = len(list_numbers_ranges0)
        min_digit = 9
        max_digit = 0
        result_digits = 0


        # TODO по идее попнуть нужно из старого списка, сразу после добавления в новый
        for j in range(list_size):
            # elems_list[-2:-1] - значение суффикса
            # elems_list[-6:-5] - это последний равный знак в нумерации, следующий будет у всех разный
            # elems_list[-5:-4] - это следующий знак, который различается, следующая будет точка
            # Зная положение точки, мы знаем фикс позиции относительно нее
            # dot_index + 2 - это суффикс
            # [dot_index - 1 : dot_index - 0] - это изменяемое значение для мин и макс диапазона
            # dot_index - 2 - это последнее значение в равной части
            # if elems_list[-2:-1] == list_numbers_ranges0[j][-2:-1] and elems_list[-6:-5] == list_numbers_ranges0[j][-6:-5]:
            if elems_list[dot_index + 1:dot_index + 2] == list_numbers_ranges0[j][
                                                          dot_index + 1:dot_index + 2] and elems_list[
                                                                                           dot_index - 2: dot_index - 1] == \
                    list_numbers_ranges0[j][dot_index - 2: dot_index - 1]:
                list_numbers_ranges.append(list_numbers_ranges0[j])
                # Составить список индексов совпавших элементов, чтобы потом их удалить из списка, после цикла
                list_indexes.append(j)

                # Нужно найти мин и макс значения [min - max] - elems_list[-5:-4]
                # print(f"list_numbers_ranges[j] = {list_numbers_ranges[j]}")
                # print(f"list_numbers_ranges[j][-5:-4] = {list_numbers_ranges[j][-5:-4]}")

                # if int(''.join(map(str, list_numbers_ranges[j][-5:-4]))) > max_digit:
                #     max_digit = int(''.join(map(str, list_numbers_ranges[j][-5])))

                print(f"digit = {int(''.join(map(str, list_numbers_ranges[j][dot_index - 1: dot_index - 0])))}")
                # TODO косяк тут
                if int(''.join(map(str, list_numbers_ranges[j][dot_index - 1: dot_index - 0]))) > max_digit:
                    max_digit = int(''.join(map(str, list_numbers_ranges[j][dot_index - 1])))

                # if int(''.join(map(str, list_numbers_ranges[j][-5:-4]))) < min_digit:
                #     min_digit = int(''.join(map(str, list_numbers_ranges[j][-5])))
                if int(''.join(map(str, list_numbers_ranges[j][dot_index - 1: dot_index - 0]))) < min_digit:
                    min_digit = int(''.join(map(str, list_numbers_ranges[j][dot_index - 1])))

                # result_digits = list_numbers_ranges[j][:7]
                result_digits = list_numbers_ranges[j][:dot_index - 1]

        print()
        # # print(f"{result_digits}[{min_digit}-{max_digit}].{list_numbers_ranges0[j][-2]}")
        # Итоговый вывод объединенного значения (сейчас нет учета размера суффикса, нужно искать положение точки)
        # print(f"{result_digits}[{min_digit}-{max_digit}].{{{list_numbers_ranges0[j][-2]}}}")
        # print(f"{result_digits}[{min_digit}-{max_digit}].{{{list_numbers_ranges0[j][dot_index + 2]}}}")
        print(f"{result_digits}[{min_digit}-{max_digit}].{{{list_numbers_ranges[0][dot_index + 2]}}}")
        print(f"list_numbers_ranges0[j][dot_index + 2] = {list_numbers_ranges[0][dot_index + 2]}")
        list_numbers_result.append(f"{result_digits}[{min_digit}-{max_digit}].{{{list_numbers_ranges[0][dot_index + 2]}}}")
        print()
        # print(f"list_numbers_ranges = {list_numbers_ranges}")
        # print(f"list_numbers_ranges0 = {list_numbers_ranges0}")
        # print(f"list_indexes = {list_indexes}")

        # Удаление уже обработанных значений из list_numbers_ranges
        index_k = 0
        for k in range(len(list_numbers_ranges)):
            # print(f"k = {k}")
            # print(f"index_k = {index_k}")
            # print(f"list_indexes[k] = {list_indexes[k]}")
            # print(type(list_indexes[k]))

            # print("pop")
            # print(f"list_indexes[k] - index_k = {list_indexes[k] + index_k}")
            # # Тк индекс_к - отрицательное число, то знак "+"
            # print(list_numbers_ranges0.pop(int(list_indexes[k]) + index_k))
            list_numbers_ranges0.pop(int(list_indexes[k]) + index_k)
            # print("===========================================")
            # print()
            list_size -= 1
            index_k -= 1

        # сохранить совпавшие элементы в новый список и можно сразу их обработать, соединить в диапазон (list_numbers_ranges)

        index += 1

    print(f"list_numbers_ranges = {list_numbers_ranges}")
    print(f"list_numbers_ranges0 = {list_numbers_ranges0}")






# * Перенс поиск суффикса из range_definition (самый верх) в suffix_calculation (самый низ)

# ============================= START =================================

# # 792370.{5}
# prefix_number = 923
# middle_part_start = 7000000
# middle_part_end = 7099999

# # 982	22000	23999 -- 7982002[2-3].{3}
# prefix_number = 982
# middle_part_start = 22000
# middle_part_end = 23999

# # 995	3465000	3479999 - 7995346[5-9].{3}, 7995347.{4}
# prefix_number = 995
# middle_part_start = 3465000
# middle_part_end = 3479999

# # 995	0095000	0119999 - 7995009[5-9].{3}, 799501[0-1].{4}    - TODO line 119: range_end_diffirence[i] == "9" - IndexError: string index out of range
# prefix_number = 995      #<------------ OK
# middle_part_start = 95000
# middle_part_end = 119999

# # 986	1366000	1370999 - 7986136[6-9].{3}, 79861370.{3}
# prefix_number = 986
# middle_part_start = 1366000
# middle_part_end = 1370999

# # 983	200000	339999 - 798302.{5}, 798303[0-3].{4} TODO line 119: range_end_diffirence[i] == "9" - IndexError: string index out of range
# prefix_number = 983                 # OK
# middle_part_start = 200000
# middle_part_end = 339999

# 969	5165000	5184999 - 7969516[5-9].{3}, 7969517.{4}, 7969518[0-4].{3} #
# prefix_number = 969
# middle_part_start = 5165000
# middle_part_end = 5184999

# # 983	3000000	3249999 - 79833[0-1].{5}, 798332[0-4].{4}   # TODO 798330.{5} 798331.{5} отдельно выводит
# prefix_number = 983                   # OK но разбивает на 2 диапазона 79833[0-1].{5}
# middle_part_start = 3000000
# middle_part_end = 3249999

# # 993	8692000	8718999 - 7993869[2-9].{3}, 7993870.{4}, 7993871[0-8].{3} #
# prefix_number = 993
# middle_part_start = 8692000
# middle_part_end = 8718999

# # 991	3761000	3793999	33000  - 7991376[1-9].{3}, 799137[7-8].{4}, 7991379[0-3].{3} # TODO 7991377.{4} 7991378.{4} отдельно выводит
# prefix_number = 991                          # OK но разбивает на 2 диапазона 799137[7-8].{4}
# middle_part_start = 3761000
# middle_part_end = 3793999

# 991	4464500	4482999 18500 - 79914464[5-9].{2}, 7991446[5-9].{3}, 7991447.{4}, 7991448[0-2].{3}
# prefix_number = 991
# middle_part_start = 4464500
# middle_part_end = 4482999

# # 993	8692000	8718999	27000	7993869[2-9].{3}, 7993870.{4}, 7993871[0-8].{3}
# prefix_number = 993
# middle_part_start = 8692000
# middle_part_end = 8718999

# 993	0	329999	330000	79930[0-2].{5}, 799303[0-2].{4} TODO падает, выход из диапазона - line 119: range_end_diffirence[i] == "9" - IndexError: string index out of range
# prefix_number = 993                  # TODO OK но разбивает на 3 диапазона 79930[0-2].{5}, нужно сделать изменения с плавающей точкой
# middle_part_start = 0
# middle_part_end = 329999

# 983	0	99999	100000	798300.{5}  OK
# prefix_number = 983
# middle_part_start = 0
# middle_part_end = 99999

# 958	2860000	2860499	500	79582860[0-4].{2}
# prefix_number = 958
# middle_part_start = 2860000
# middle_part_end = 2860499

# 958	5418510	5418519	10	7958541851.{1}  OK
# prefix_number = 958
# middle_part_start = 5418510
# middle_part_end = 5418519

# 958	8471250	8471349	100	795884712[5-9].{1}, 795884713[0-4].{1} OK
prefix_number = 958
middle_part_start = 8471250
middle_part_end = 8471349

# # 939	9396800	9426799	30000	79399396[8-9].{2}, 7939939[7-9].{3}, 793994[0-1].{4}, 7939942[0-5].{3},  79399426[0-7].{2} TODO много строк в выде с мелкими диапазонами
# prefix_number = 939             # TODO похоже сломалось 7939939[6-9].{2} вместо 79399396[8-9].{2}
# middle_part_start = 9396800
# middle_part_end = 9426799


# 923 800000 824999  25000   792308[0-1].{4}, 7923082[0-4].{3} OK
# prefix_number = 923
# middle_part_start = 800000
# middle_part_end = 824999

# 923	0	999	1000	79230000.{3} ОК
# prefix_number = 923
# middle_part_start = 0
# middle_part_end = 999

# 913	8900000	9599999	700000	791389.{5}, 79139[0-5].{5}
# prefix_number = 913
# middle_part_start = 8900000
# middle_part_end = 9599999

# 913	0	199999	200000	79130[01].{5}
# prefix_number = 913
# middle_part_start = 0
# middle_part_end = 199999

# 923	7808000	7819999	12000	7923780[8-9].{3}, 7923781.{4}
# prefix_number = 923
# middle_part_start = 7808000
# middle_part_end = 7819999


# корявые диапазоны обрабатываются
# suffix = 0, решено
# 958	936100	936156	57   TODO 83 line^ range_end_diffirence[i] == "9": IndexError: string index out of range
# prefix_number = 958
# middle_part_start = 936100
# middle_part_end = 936156

# suffix = 0, решено
# 958	936452	936499	48  TODO RecursionError: maximum recursion depth exceeded
# prefix_number = 958
# middle_part_start = 936452
# middle_part_end = 936499


# 958	936157	936157	1    TODO падает все еще
# prefix_number = 958
# middle_part_start = 936157
# middle_part_end = 936157



print("===================================START================================================================")



numbers_range = 0
general_list_middle_part_range = 0
end_range = middle_part_end
int_real_end_of_range = middle_part_end
list_numbers_result = []
list_numbers_ranges = []
list_numbers_ranges0 = []
list_numbers_ranges1 = []
list_numbers_ranges2 = []
list_numbers_ranges3 = []
list_numbers_ranges4 = []
list_numbers_ranges5 = []
list_numbers_ranges6 = []
list_numbers_ranges7 = []
list_numbers_ranges8 = []
list_numbers_ranges9 = []
list_numbers_ranges10 = []
# ====================================================================================================

# Считаем диапазоны
suffix_calculation(prefix_number, middle_part_start, middle_part_end, general_list_middle_part_range)

print()
if len(list_numbers_ranges0) != 0:
    print(list_numbers_ranges0)
    print()
    if len(list_numbers_ranges0) <= 1:
        list_numbers_result += list_numbers_ranges0
if len(list_numbers_ranges1) != 0:
    print(1)
    print(list_numbers_ranges1)
    list_numbers_result += list_numbers_ranges1
if len(list_numbers_ranges2) != 0:
    print(2)
    print(list_numbers_ranges2)
    list_numbers_result += list_numbers_ranges2
if len(list_numbers_ranges3) != 0:
    print(3)
    print(list_numbers_ranges3)
    list_numbers_result += list_numbers_ranges3
if len(list_numbers_ranges4) != 0:
    print(4)
    print(list_numbers_ranges4)
    list_numbers_result += list_numbers_ranges4
if len(list_numbers_ranges5) != 0:
    print(5)
    print(list_numbers_ranges5)
    list_numbers_result += list_numbers_ranges5
if len(list_numbers_ranges6) != 0:
    print(list_numbers_ranges6)
    list_numbers_result += list_numbers_ranges6
if len(list_numbers_ranges7) != 0:
    print(list_numbers_ranges7)
    list_numbers_result += list_numbers_ranges7
if len(list_numbers_ranges8) != 0:
    print(list_numbers_ranges8)
    list_numbers_result += list_numbers_ranges8
if len(list_numbers_ranges9) != 0:
    print(list_numbers_ranges9)
    list_numbers_result += list_numbers_ranges9
if len(list_numbers_ranges10) != 0:
    print(list_numbers_ranges10)
    list_numbers_result += list_numbers_ranges10

# TODO Нужно перенести объединение диапазонов в новый файл

if(len(list_numbers_ranges0) > 1):
    # dot_index = text.find('.') # Example

    union_ranges(list_numbers_result, list_numbers_ranges, list_numbers_ranges0, list_numbers_ranges2, list_numbers_ranges3, list_numbers_ranges4, list_numbers_ranges5, list_numbers_ranges6, list_numbers_ranges7, list_numbers_ranges8, list_numbers_ranges9, list_numbers_ranges10)

print()
print("===================================RESULT=============================================================")

print()
print(f"list_numbers_result = {list_numbers_result}")


print()
print("===================================END================================================================")
print()


