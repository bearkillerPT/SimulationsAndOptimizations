
import sys
import matplotlib.pyplot as plt


class MidSquareGenerator:
    def __init__(self, seed=4):
        self.seed = seed
        self.current_number = seed

    def getRandom(self):
        result = self.current_number ** 2
        result = result % 10**6
        result -= result % 100
        result /= 100
        if result == self.current_number:
            self.current_number = 0
            return 0
        self.current_number = int(result)
        return self.current_number


def main():
    depth = 1
    if len(sys.argv) == 2:
        depth = int(sys.argv[1])
    used_values = {}
    for i in range(1000, 10000):
        current_generator = MidSquareGenerator(i)
        current_depth = 0
        while(current_depth < depth):
            current_value = current_generator.getRandom()
            if str(current_value) not in used_values.keys():
                used_values.setdefault(str(current_value), 1)
            else:
                used_values[str(current_value)] += 1
            current_depth += 1
    plt.plot(used_values.keys(), used_values.values())
    plt.show()


if __name__ == "__main__":
    main()
