my_file = open("text_2.txt", "r", encoding="utf-8")
# content = my_file.read()
# print(content)
# print("Текущая позиция", my_file.tell())
count = 0

for line in my_file:
    count = count + 1
    # count += count почему то выводил количество строк 0
print(f"количество строк в файле - {count}")

#my_file_len = [len(x) for x in my_file.split()]
#otvet = max(my_file_len) / min(my_file_len)
#print(otvet)