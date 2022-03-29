
# based on Simulation Modeling and Analysis, Averil Law

import random
import statistics
import sys
import json
import os


class Company:
    def __init__(self, s, S, debug):
        self.sim_time = 0.0

        # state variables
        self.inventory_level = 60
        self.s = s
        self.S = S
        self.quantity_backlogged = 0
        self.time_last_event = 0.0
        self.ordered_quantity = 0

        # statistics

        # random.choices([1,2,3,4], [1/6,1/3,1/3,1/6], k=1) order size

        # event list
        self.time_next_event = {}
        self.time_next_event['order_arrival'] = self.sim_time + \
            random.uniform(0.5, 1)
        self.time_next_event['client_demand'] = self.sim_time + \
            random.expovariate(1/0.1)
        self.time_next_event['evaluation'] = 1
        self.time_next_event['end_simulation'] = 120
        self.next_event_type = ''
        self.time_arrival = []
        self.debug = debug

    def timing(self):

        min_time_next_event = 1

        for e in self.time_next_event:
            if self.time_next_event[e] < min_time_next_event:
                min_time_next_event = self.time_next_event[e]
                self.next_event_type = e

        self.sim_time = min_time_next_event

    def order_arrival(self):
        self.inventory_level += self.ordered_quantity
        self.time_next_event['order_arrival'] = 0

    def client_demand(self):
        pass

    def evaluation(self):
        if self.inventory_level < self.s:
            quantity_to_order = self.S - self.inventory_level

        self.time_next_event['evaluation'] += 1



    def end_simulation(self):
        pass

    def run(self):
        while self.num_custs_delayed < 5:
            self.timing()
            if self.next_event_type == 'arrive':
                self.arrive()
            elif self.next_event_type == 'depart':
                self.depart()

    def show_stats(self):
        print("\nDelay per costumer:")
        print(self.clients_statistics)
        clients = len(self.clients_statistics.keys())
        avg_delay = 0
        if(clients):
            print("\nAvg delay:")
            avg_delay = statistics.mean(self.clients_statistics.values())
            print(avg_delay)
        avg_queue_size = statistics.mean(self.size_of_queue)
        print("\nAvg queue size:")
        print(avg_queue_size)
        print("\nServer Frequency:")
        server_freq = self.clients_done/self.sim_time
        print(server_freq)

    def save_stats(self, filename):
        clients = len(self.clients_statistics.keys())
        avg_delay = 0
        if(clients):
            avg_delay = sum(self.clients_statistics.values())/clients
        avg_queue_size = sum(self.size_of_queue)/len(self.size_of_queue)
        server_freq = self.clients_done/self.sim_time

        if not os.path.exists('stats'):
            os.makedirs('stats')
        fp = open(filename, 'w')
        fp.write(
            json.dumps({
                "avg_delay": avg_delay,
                "avg_queue_size": avg_queue_size,
                "server_freq": server_freq
            }))
        # main


def main():
    # initialize
    # simulation clock
    if len(sys.argv) == 1:
        company = Company(True)
        company.run()
        company.show_stats()
    elif len(sys.argv) == 2:
        for i in range(int(sys.argv[1])):
            stats_filename = "stats/stat" + str(i) + ".json"
            company = Company(False)
            company.run()
            company.save_stats(stats_filename)


if __name__ == "__main__":
    main()
