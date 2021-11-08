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
		
	return ', '.join(result)

if __name__ == "__main__":
	print(field(goods, 'title'))
	print(field(goods, 'title', 'price'))

