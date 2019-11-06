from numpy import (array,average,delete,subtract,subtract,
	sum,multiply,square,sqrt)

matrix = array((
		(5,3,4,4,None),
		(3,1,2,3,3),
		(4,3,4,3,5),
		(3,3,1,5,4),
		(1,5,5,2,1)
	))

removal_collumns = []
required_rows = []

for row in range(0, matrix.shape[0]):
	for col in range(0, matrix.shape[1]):
		if matrix[row][col] is None:
			if col not in removal_collumns:
				removal_collumns.append(col)
				required_rows.append(row)
				break

matrix_2 = delete(matrix, removal_collumns, axis=1)
average_collumn = average(matrix_2, axis=1).reshape((matrix_2.shape[0],1))


a = b = c = d = None
similar_point = None
similar_row = None
similarity = []
for item in required_rows:
	for i in range(0,matrix_2.shape[0]):
		if i == item:
			continue
		a = subtract(matrix_2[item], average_collumn[item])
		b = subtract(matrix_2[i], average_collumn[i])

		c = sqrt(sum(square(a)))
		d = sqrt(sum(square(b)))
		similar_point = sum(multiply(a,b))/(c*d)
		similarity.append(similar_point)
		if similar_point == max(similarity):
			similar_row = i

	for index in range(0, matrix.shape[1]):
		if matrix[item][index] is None:
			matrix[item][index] = matrix[similar_row][index]

print(matrix)
