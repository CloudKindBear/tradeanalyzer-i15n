from validateclass import CustomObjects

if __name__ == "__main__":
    v = CustomObjects()
    while True:
        data = input("Введите что нибудь: ")
        if data is None:
            break
        if len(data) == 0:
            break
        v.store(data)
    print(v.to_string())
