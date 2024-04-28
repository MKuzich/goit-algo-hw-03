def move_disk(start, end):
    print(f"Перемістити диск з {start} на {end}")

def hanoi(n, start, end, aux):
    if n == 1:
        move_disk(start, end)
        state[end].append(state[start].pop())
        print(f"Проміжний стан: {state}")
    else:
        hanoi(n-1, start, aux, end)
        move_disk(start, end)
        state[end].append(state[start].pop())
        print(f"Проміжний стан: {state}")
        hanoi(n-1, aux, end, start)

def main():
    global state
    n = int(input("Введіть кількість дисків: "))
    start = 'A'
    aux = 'B'
    end = 'C'

    state = {start: list(range(n, 0, -1)), aux: [], end: []}
    print(f"Початковий стан: {state}")

    hanoi(n, start, end, aux)

    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()

