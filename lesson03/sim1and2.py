import sys
import random
import matplotlib.pyplot as plt

class Simulation:
    def __init__(self):
        self.x = 1.0
        self.result = [self.x]
        self.a = random.random() + 0.5
        self.b = random.randint(10,20)
    def update(self):
        self.x *= self.a 
        self.x += self.b 

    def observe(self):
        self.result.append(self.x)

    def run(self, total_t):
        for _ in range(total_t):
            self.update()
            self.observe()

def print_usage():
    print("python3 sim1and2.py t n_sims\n\tt - markov model depth\n\tn_sims - number of simulations to be performed")

def main():
    total_t = 10
    total_sims = 20
    simulation_results = []
    if len(sys.argv) == 1:
        print_usage()
    elif len(sys.argv) == 3:
        total_t = int(sys.argv[1])
        total_sims = int(sys.argv[2])
    for i in range(total_sims):
        sim = Simulation()
        sim.run(total_t)
        plt.plot(sim.result)
    plt.show()
if __name__ == "__main__":
    main()
