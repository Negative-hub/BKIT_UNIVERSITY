# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'price': 5000, 'color': 'black'}
]

def field(items, *args):
	assert len(args) > 0

	result = []

	if len(args) == 1:
		for item in items:
			if item[args[0]]:
				result.append(item[args[0]])
	else:
		for item in items:
			d = {}
			for arg in args:
				if item[arg]:
					d[arg] = item[arg]
			result.append(str(d))
		
	print(', '.join(result))

field(goods, 'title')
field(goods, 'title', 'price')