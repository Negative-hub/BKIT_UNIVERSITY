import sys
import math

def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
        coef = float(coef_str)
    except:
        # Вводим с клавиатуры
        coef_str = input(prompt)
        try:
            # Переводим строку в действительное число
            coef = float(coef_str)
        except:
            # В случае невозможности перевода делаем рекурсивный алгоритм
            return get_coef(index, prompt)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        list[float]: Список корней
    '''
    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        result.append(root1)
        result.append(root2)
    return result

def get_roots_b(roots):
    '''
    Вычисление корней для биквадратного уравнения

    Args:
        list [float]: массив корней квадратного уравнения
    
    Returns:
        list [float]: массив корней биквадратного уравнения
    '''

    result = []

    for root in roots:
        if root == 0:
            result.append(root)
        elif root > 0:
            sqRoot = math.sqrt(root)
            result.append(sqRoot)
            result.append(-sqRoot)
        
    return result

def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')
    
    # Вычисление корней
    roots = get_roots(a,b,c)

    # Вычисление корней для биквадратного уравнения
    roots = get_roots_b(roots)

    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Примеры запуска
# qr.py 1 11 10 - нет корней
# qr.py 1 16 0 - {0}
# qr.py 1 -2 -8 - {2, -2}
# qr.py 1 -4 0 - {2, -2, 0}
# qr.py 1 -10 9 - {3, -3, 1, -1}