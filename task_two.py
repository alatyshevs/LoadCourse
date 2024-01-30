def main(_str):
	_dict = {}

	for i in _str:
		if i in _dict:
			_dict[i] += 1
		else : _dict[i] = 1

	for key, i in _dict.items():
		if i > 1:
			print(f'Repeating character : {key}')


if __name__ == "__main__":
	main("Hello")


