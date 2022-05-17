from re import T
import sys
import matplotlib.pyplot as plt
import numpy as np


class Simulation:
    def __init__(self, m, g, u, delta_t, z0, v0):
        self.m = m
        self.g = g
        self.u = u
        self.delta_t = delta_t
        self.z = z0
        self.v = v0
        self.z_results = [z0]
        self.v_results = [v0]
        self.simulation_time = 0

    def f(self, v):
        f1 = self.delta_t * v
        f2 = self.delta_t* (v + (- self.g + self.u * (v + f1/2)**2 /self.m)  * (self.delta_t/2))
        f3 = self.delta_t* (v + (- self.g + self.u * (v + f2/2)**2 /self.m)  * (self.delta_t/2))
        f4 = self.delta_t* (v + (- self.g + self.u * (v + f3)**2 /self.m)  * (self.delta_t))
        return v + 1/6* (f1 + 2*f2 + 2*f3 + f4)


    def rk4_update(self):
        current_v = self.f(self.v)
        new_z = self.z + current_v * self.delta_t
        self.simulation_time += self.delta_t
        if new_z >= 0:
            self.z = new_z
            self.v = current_v + (- self.g + self.u * current_v**2 /self.m)  * self.delta_t
        else:
            self.v = 0


    def observe(self):
        self.z_results.append(self.z)
        self.v_results.append(self.v)
        
    def run(self, total_t):
        for _ in np.arange(0, total_t, self.delta_t):
            self.rk4_update()
            self.observe()


def print_usage():
    print("Usage:\n\tpython3 EuclidianSim.py z0 v0 m g u delta_t total_t") 



def main():
    m = 0
    g = 0
    u = 0
    delta_t = 0
    z0 = 0
    v0 = 0
    total_t = 0
    if len(sys.argv) != 8:
        print_usage()
    else:
        m = float(sys.argv[3])
        g = float(sys.argv[4])
        u = float(sys.argv[5])
        delta_t = float(sys.argv[6])
        z0 = float(sys.argv[1])
        v0 = float(sys.argv[2])
        total_t = float(sys.argv[7])
        sim = Simulation(m, g, u, delta_t, z0, v0)
        sim.run(total_t)
        plt.plot([delta_t*x for x in range(len(sim.z_results))], sim.z_results)
        plt.plot([delta_t*x for x in range(len(sim.v_results))], sim.v_results)
        plt.xlabel('Time in seconds')
        plt.show()


if __name__ == "__main__":
    main()