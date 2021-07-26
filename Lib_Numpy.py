import numpy as np

my_List = [9, 5, 8, 1]
array = np.array(my_List)
print(my_List)  # [9, 5, 8, 1]
print(array)  # [9 5 8 1]
print(type(array))  # <class 'numpy.ndarray'>
print(array[2])  # 8
array = np.append(array, 2)
print(array)  # [9 5 8 1 2]
array = np.delete(array, 4)
print(array)  # [9 5 8 1]
array = np.sort(array)
print(array)  # [1 5 8 9]

# N-dimensional array
my_List = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
array = np.array(my_List)
print(my_List)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(array)
print(type(array))  # <class 'numpy.ndarray'>
print(array[2])  # [7 8 9]
print(array[0][0])  # 1
print(array.ndim)  # 2
print(array.size)  # 9
print(array.shape)  # (3, 3)

# Changing the shape
array = array.reshape((9, 1))
print(array)
print(array.shape)  # (9, 1)
array = array.reshape((3, 3))
print(array)


array = np.arange(0, 4.02, 0.02)
print(array)
print(array.shape)  # (201,)

# Indexing and Slicing
print(array[0:7])   # [0.   0.02 0.04 0.06 0.08 0.1  0.12]
print(array[:7])    # [0.   0.02 0.04 0.06 0.08 0.1  0.12]
print(array[198:])  # [3.96 3.98 4.  ]
print(array[-3:])   # [3.96 3.98 4.  ]
print(array[array >= 3.96])  # [3.96 3.98 4.  ]

# Array Operations
print(array.sum())  # 402.0
print(array[0:7] * 2)  # [0.   0.04 0.08 0.12 0.16 0.2  0.24]
print(array.max())  # 4.0
print(np.mean(array[0:7]))  # 0.060000000000000005
print(np.mean(array[0:7])*10000000)  # 600000.0
print(np.median(array[0:7]))  # 0.06
print(np.std(array))  # standard deviation = 1.1604596790352808
