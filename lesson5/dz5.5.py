from random import randint

with open("text_5_test.txt", "w+", encoding="utf-8") as my_file:
    #text = my_file.read()
    my_file.write(" ".join([str(randint(1, 77)) for _ in range(10)]))
    my_file.seek(0)
    print(sum(map(int, my_file.readline().split())))