my_list = [x * x for x in range(20) if x % 2 == 0]
print(my_list)
my_gen = (x * x for x in range(20) if x % 2 == 0)
print(my_gen)


def square(x):
    return x * x


my_map = map(square, range(20))  # (x * x for x in range(20))
print(my_map)

def is_even(x) -> bool:
    return x % 2 == 0

my_filter = filter(is_even, range(20))  # (x for x in range(20) if x % 2 == 0)

my_filter_map = map(square, filter(is_even, range(20)))  # (x * x for x in range(20) if x % 2 == 0)
result = list(my_filter_map) == [x * x for x in range(20) if x % 2 == 0]
print(result)

my_lambda_function = lambda: 0
def my_lambda_function():
    return 0

my_lambda_square = lambda x, y: x * y
print(my_lambda_square)

# my_map = map(square, range(20))  # (x * x for x in range(20))
my_new_map = map(lambda x: x * x, range(20))