import sys
import matplotlib.pyplot as plt


class Simulation:
    def __init__(self):
        self.x = 0.1
        self.K = 1.0
        self.r = 0.2
        self.delta_t = 0.01
        self.result = [self.x]

    def euclidian_update(self):
        self.x = self.x + self.r * self.x * \
            (1 - self.x / self.K) * self.delta_t

    def f(self, x):
        return x + self.r * x * \
            (1 - x / self.K)

    def runge_kutta_update(self):
        
        k1 = self.delta_t * self.f(self.x)
        k2 = self.delta_t * self.f(self.x + self.delta_t/2)
        k3 = self.delta_t * self.f(self.x + self.delta_t/2)
        k4 = self.delta_t * self.f(self.x + self.delta_t)
    def observe(self):
        self.result.append(self.x)

    def run(self, total_t):
        for _ in range(total_t):
            self.euclidian_update()
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
    plt.plot([0.01*x for x in range(len(sim.result))], sim.result)
    plt.show()


if __name__ == "__main__":
    main()
