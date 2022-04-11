import sys
import random
import matplotlib.pyplot as plt


class Simulation:
    def __init__(self):
        self.x = 1.0
        self.y = 1.0
        self.result = {
            "xResult": [self.x],
            "yResult": [self.y]
        }

    def update(self):
        new_x = 0.5 * self.x + self.y
        new_y = - 0.5 * self.x + self.y
        self.x, self.y = new_x, new_y

    def observe(self):
        self.result["xResult"].append(self.x)
        self.result["yResult"].append(self.y)

    def run(self, total_t):
        for _ in range(total_t):
            self.update()
            self.observe()


def print_usage():
    print("python3 sim3.py t\n\tt - markov model depth (default 100)")


def main():
    total_t = 100
    if len(sys.argv) == 1:
        print_usage()
    elif len(sys.argv) == 2:
        total_t = int(sys.argv[1])
    sim = Simulation()
    sim.run(total_t)
    plt.plot(sim.result["xResult"], sim.result["yResult"] )
    plt.show()


if __name__ == "__main__":
    main()
