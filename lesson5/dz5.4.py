from googletrans import Translator


with open("text_4_translate.txt", "w", encoding="utf-8") as my_file:
    with open("text_4.txt", "r", encoding="utf-8") as new_file:
        text = new_file.read()
    try:
        my_file.write(Translator().translate(text, dest="ru").text)
    except AttributeError:
        print("Произошла ошибка")



