def zad2(n, nums_list):
    return list({i for i in range(1, n + 1)}.difference(set(nums_list)))


n = 10


input_list = [2, 6, 7, 4, 9]

print(zad2(n, input_list))
