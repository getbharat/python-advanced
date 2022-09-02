def func(x):
    x = 10
    print(x)


func(56)


def func_list(li):
    li.append(67)
    print(li)


l = [10, 20, 40]

func_list(l)
print(l)


def func_list_1(li):
    li[0] = 89
    print(li)


l2 = [12, 34, 56]
func_list_1(l2)


def func_list_2(li):
    li = [1, 2, 4, 5, 6]  # Will not change the outer list as reassignment happened
    print(li)


l3 = [45, 67, 88]
func_list_2(l3)
print(l3)
