def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            print(" файл:")
            print(content)
    except FileNotFoundError:
        print(f"Помилка: файл шляха '{filepath}' не існує")
    except Exception as e:
        print(f"Сталася помилка: {e}")


path = input("Введіть шлях к файлу: ")
read_file(path)
