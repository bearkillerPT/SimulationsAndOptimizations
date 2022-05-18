
import matplotlib.pyplot as plt

from unittest import result


class LGC:
    def __init__(self, a, c, m, seed=4):
        if seed >= m:
            self = None
        self.seed = seed
        self.current_number = seed
        self.a = a
        self.c = c
        self.m = m

    def getRandom(self):
        self.current_number = (self.a * self.current_number + self.c) % self.m
        return self.current_number


def main():
    a = 995
    c = 993
    m = 1000
    seed = 4
    generator = LGC(a, c, m, seed)
    result = []
    for i in range(32):
        result.append(generator.getRandom())
    plt.plot(result)
    plt.show()


if __name__ == "__main__":
    main()
