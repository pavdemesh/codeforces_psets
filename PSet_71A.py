n = int(input())
input_words = []
if (n >= 0) and (n <= 100):
    for i in range(n):
        input_words.append(str(input()))

    for i in range(n):
        if len(input_words[i]) > 10:
            print(input_words[i][0] + str(len(input_words[i]) - 2) + input_words[i][-1])
        else:
            print(input_words[i])
