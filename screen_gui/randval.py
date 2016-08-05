from random import uniform, randint


def randgen():
    sensID = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
              'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
    y = randint(0, 17)
    x = round(uniform(15, 20), 2)
    x = sensID[y] + str(x)
    return x

if __name__ == "__main__":
    randgen()
