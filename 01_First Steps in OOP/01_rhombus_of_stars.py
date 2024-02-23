size = int(input())


def upper_part(upper_size):
    for el in range(1, size):
        print(f"{' ' * (size - el)}{'* ' * el}")


def bottom_part(bottom_size):
    for el in range(size, -1, -1):
        print(f"{' ' * (size - el)}{'* ' * el}")


def full_rhomb():
    upper_part(size)
    bottom_part(size)


full_rhomb()
