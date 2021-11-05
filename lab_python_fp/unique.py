class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items # массив элементов
        
        try:
            self.ignore_case = kwargs["ignore_case"]
        except:
            self.ignore_case = False
       
        self.array = []

        for item in items: 
            item = (self.ignore_case and str(item).lower()) or item # переводим элементы в нижний регистр, если стоит флаг ignore_case

            try: # проверяем наличие элемента в массиве
                self.array.index(item) 
            except:
                self.array.append(item)
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
       
    def __next__(self):
        self.index += 1

        return self.array[(self.index - 1) % len(self.array)] # возвращаем следующий элемент

    def __iter__(self):
        self.index = 0
        return self


data = ["a", "a", "b", "B", "c"]
a = Unique(data, ignore_case = True)
print(a.__iter__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
