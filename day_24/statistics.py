import numpy as np
python_list = [1,2,3,4,5]
print('Type:', type (python_list))
print(python_list)
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
print(two_dimensional_list)
numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list))
#
numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2)
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)
#####
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))
print(numpy_two_dimensional_list)
##
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ',
numpy_two_dimensional_list.tolist())
#
python_tuple = (1,2,3,4,5)
print(type (python_tuple))
print('python_tuple: ', python_tuple)
# 
numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple))
print('numpy_array_from_tuple: ', numpy_array_from_tuple)
#
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ',
numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
[4,5,6,7],
[8,9,10, 11]])
print(three_by_four_array.shape)
##
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)
#
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8]])
print('The size:', numpy_array_from_list.size)
print('The size:', two_dimensional_list.size)
#
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list + 10
print(ten_plus_original)
#
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list - 10
print(ten_minus_original)
#
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)
#
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)
#
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)
#
# Floor division: the division result without the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)
#
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list ** 2
print(ten_times_original)
#
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)
#
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
numpy_int_arr 
#
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
numpy_int_arr
#
np.array([-3, -2, 0, 1,2,3], dtype='bool')
#
normal_array = np.random.normal(79, 15, 80)
normal_array
from scipy import stats
import matplotlib.pyplot as plt
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean,
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))
plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()
#
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
pressure
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
#
import seaborn as sns 
mu = 28
sigma = 15
samples = 100000
x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x)
ax.set(xlabel="x", ylabel='y')
plt.show()