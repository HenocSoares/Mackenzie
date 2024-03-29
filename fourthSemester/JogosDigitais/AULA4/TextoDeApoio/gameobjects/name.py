if __name__ == "__main__":
	A = (10.0, 20.0)
	B = (30.0, 35.0)
	AB = Vector2.from_points(A, B)
	step = AB * .1
	position = Vector2(*A)
	for n in range(10):
		position += step
		print(position)
