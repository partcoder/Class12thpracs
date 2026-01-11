import pandas as pd

def main():
	data = {
		'Name': ['Alice', 'Bob', 'Charlie'],
		'Age': [28, 34, 25],
		'Department': ['HR', 'IT', 'Marketing'],
		'Salary': [50000, 65000, 45000]
	}

	df = pd.DataFrame(data)

	print("a) DataFrame:")
	print(df)

	print("b) Index of the DataFrame:")
	print(df.index)

	print("c) Column names:")
	print(list(df.columns))

	print("d) Data types of each column:")
	print(df.dtypes)
    
	print("e) Shape (rows, columns):")
	print(df.shape)


main()
    
