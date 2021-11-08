def print_result(function):
	def wrapper():
		print(function.__name__)
		
		if type(function()) == type([]):
			for item in function():
				print(item)
		elif type(function()) == type({}):
			for key in function().keys():
				print("{} = {}".format(key, function()[key]))
		else:
			print(function())
			
	return wrapper

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()