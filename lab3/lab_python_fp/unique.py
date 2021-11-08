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
        
    def __next__(self):
        self.index += 1

        return self.array[(self.index - 1) % len(self.array)] # возвращаем следующий элемент

    def __iter__(self):
        self.index = 0
        return self

if __name__ == "__main__":
    a = Unique(["a", "b", "A", "bb", "BB", "b", "c"], ignore_case = True)
    a.__iter__()
    print(a.__next__(), end=', ')
    print(a.__next__(), end=', ')
    print(a.__next__(), end=', ')
    print(a.__next__(), end=', ')
    print(a.__next__(), end=', ')
    print(a.__next__(), end=', ')
    print(a.__next__(), end=', ')
    print(a.__next__(), end=', ')
    print(a.__next__(), end=', ')
    print(a.__next__(), end=', ')
    print(a.__next__(), end=', ')
    print(a.__next__())