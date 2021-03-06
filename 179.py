def sort_max(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:
            array[i], array[idx_min] = array[idx_min], array[i]
    return array

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

try:
    array = list(map(int, input('Введите числа через пробел >> ').split()))
except ValueError:
    print('Вы ввели НЕ ЧИСЛО')
    array = list(map(int, input('Повторите внимательно ввод чисел через пробел >> ').split()))

try:
    element = int(input('Введите любое число >> '))
except ValueError:
    print('Вы ввели НЕ ЧИСЛО')
    element = int(input('Повторите внимательно ввод любого числа >> '))

array.append(element)
array_sort = sort_max(array)
result = binary_search(array_sort, element, 0, len(array_sort))

print('Номер позиции элемента слева -', result-1)
print('Номер позиции элемента справа -', result+1)