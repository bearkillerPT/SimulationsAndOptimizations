
# based on Simulation Modeling and Analysis, Averil Law

import random
import statistics
import sys
import json
import os


class Company:
    def __init__(self, s, S, order_incremetal_cost):
        self.sim_time = 0.0

        # state variables
        self.inventory_level = 60
        self.s = s
        self.S = S
        self.quantity_backlogged = 0
        self.time_last_event = 0.0
        self.ordered_quantity = 0
        self.order_incremetal_cost = order_incremetal_cost

        # statistics
        self.shortage_cost = 0
        self.handling_cost = 0
        self.ordering_cost = 0

        # event list
        self.time_next_event = {}
        self.time_next_event['order_arrival'] = 121
        self.time_next_event['client_demand'] = self.sim_time + \
            random.expovariate(1/0.1)
        self.time_next_event['evaluation'] = 1
        self.time_next_event['end_simulation'] = 120
        self.next_event_type = ''
        self.time_arrival = []

    def timing(self):

        min_time_next_event = 121

        for e in self.time_next_event:
            if self.time_next_event[e] < min_time_next_event:
                min_time_next_event = self.time_next_event[e]
                self.next_event_type = e

        self.sim_time = min_time_next_event

    def order_arrival(self):
        if self.quantity_backlogged > 0:
            inventory_increment = self.ordered_quantity - self.quantity_backlogged
            if inventory_increment >= 0:
                self.inventory_level += inventory_increment
                self.quantity_backlogged = 0
            else:
                self.quantity_backlogged -= self.ordered_quantity
        else:      
            self.inventory_level += self.ordered_quantity

        self.time_next_event['order_arrival'] = 121

    def client_demand(self):
        [quantity_demanded] = random.choices(
            [1, 2, 3, 4], [1/6, 1/3, 1/3, 1/6], k=1)
        if self.inventory_level >= quantity_demanded:
            self.inventory_level -= quantity_demanded
        else:
            self.quantity_backlogged += quantity_demanded

        self.time_next_event['client_demand'] = self.sim_time + \
                random.expovariate(1/0.1)

    def evaluation(self):
        if self.inventory_level < self.s:
            self.ordered_quantity = self.S - self.inventory_level
            self.time_next_event['order_arrival'] = self.sim_time + \
                random.uniform(0.5, 1)
            self.ordering_cost += 32 + self.order_incremetal_cost*self.ordered_quantity
        if self.quantity_backlogged > 0:
            self.shortage_cost += 5*self.quantity_backlogged
        if self.inventory_level > 0:
            self.handling_cost += self.inventory_level

        #print("Inventory: " + str(self.inventory_level))
        #print("Backlog: " + str(self.quantity_backlogged))


        self.time_next_event['evaluation'] += 1

    def run(self):
        while self.sim_time < 120:
            self.timing()
            if self.next_event_type == 'order_arrival':
                self.order_arrival()
            elif self.next_event_type == 'client_demand':
                self.client_demand()
            elif self.next_event_type == 'evaluation':
                self.evaluation()


    def show_stats(self):
        print("Shortage Cost:"+ str(self.shortage_cost))
        print("Handling Cost:"+ str(self.handling_cost))
        print("Ordering Cost:"+ str(self.ordering_cost))
        print("Total Cost:" +str(self.shortage_cost + self.handling_cost + self.ordering_cost))


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
        company = Company(20,40, 3)
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
