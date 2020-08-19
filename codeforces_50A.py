# Get two ints m and n for height and length
m_height, n_length = list(map(int, input().split()))

if m_height < 1 or m_height > n_length or n_length > 16:
    print("Wrong input")
    exit()

count_dominos = 0
is_vertical = False

for row in range(m_height):
    temp_n = n_length
    # while True:
    while temp_n > 0:
        if temp_n >= 2:
            temp_n -= 2
            count_dominos += 1
            # print(f"row is {row} and n_temp is {temp_n} and using branch 1")
        elif temp_n == 1 and m_height - row >= 2 and not is_vertical:
            temp_n -= 2
            count_dominos += 1
            is_vertical = True
            # print(f"row is {row} and n_temp is {temp_n} and using branch 2")
            # break
        elif temp_n == 1 and is_vertical:
            temp_n -= 2
            is_vertical = False
            # print(f"row is {row} and n_temp is {temp_n} and using branch 3")
        #     break
        else:
            # print(f"row is {row} and n_temp is {temp_n} and using branch 4")
            temp_n -= 2
            # break
print(count_dominos)
