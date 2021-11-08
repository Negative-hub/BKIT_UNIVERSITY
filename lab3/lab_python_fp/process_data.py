import json
from cm_timer import cm_timer_1
from unique import Unique
from gen_random import gen_random

path = "data_light.json"

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding = "utf-8") as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

def print_result(function):
    def wrapper(arg):
        print(function(arg))
        return function(arg)
    return wrapper

@print_result
def f1(arg):
    return sorted(Unique([item["job-name"] for item in arg], ignore_case = True).array)

@print_result
def f2(arg): 
    return list(filter(lambda x: x.split()[0] == "программист", arg))


@print_result
def f3(arg):
    return list(map(lambda x: "{} c опытом Python".format(x), arg))


@print_result
def f4(arg):
    zipped = list(zip(arg, gen_random(len(arg), 100000, 200000)))
    return list(map(lambda x: "{}, зарплата {} руб.".format(x[0], x[1]), zipped))


if __name__ == '__main__':
  with cm_timer_1():
    f4(f3(f2(f1(data))))