
# based on Simulation Modeling and Analysis, Averil Law

import random
import statistics
import sys
import json
import os

class Hospital:
    def __init__(self, debug):
        self.sim_time = 0.0
        self.client_id = 0
        self.client_ids_queue = []
        self.size_of_queue = []
        self.clients_statistics = {}
        self.clients_done = 0
        # state variables
        self.server_status = ['idle', 'idle']
        self.num_in_q = 0
        self.time_last_event = 0.0

        # statistics
        self.num_custs_delayed = 0

        # event list
        self.time_next_event = {}
        self.time_next_event['arrive'] = self.sim_time + random.uniform(0, 10)
        self.time_next_event['depart'] = 1e10
        self.next_event_type = ''
        self.time_arrival = []
        self.debug = debug

    def timing(self):

        min_time_next_event = 1e9

        self.next_event_type = ''

        for e in self.time_next_event:
            if self.time_next_event[e] < min_time_next_event:
                min_time_next_event = self.time_next_event[e]
                self.next_event_type = e

        if self.next_event_type == '':
            print('Event list is emply at time', self.sim_time)
            sys.exit()

        self.sim_time = min_time_next_event

    def arrive(self):
        self.time_next_event['arrive'] = self.sim_time + random.uniform(0, 5)

        if all([x == 'busy' for x in self.server_status]):
            self.time_arrival.append(self.sim_time)
            self.client_ids_queue.append(self.client_id)
            self.client_id += 1
        else:
            self.num_custs_delayed += 1
            for server_status in self.server_status:
                if server_status == 'idle':
                    server_status = 'busy'
                    break
            self.time_next_event['depart'] = self.sim_time + random.uniform(0, 10)
        self.size_of_queue.append(len(self.time_arrival))
        if self.debug:
            print('arrive event at {0:5.2f} size of queue is {1:2d}'.format(
            self.sim_time, len(self.time_arrival)))
    def depart(self):

        if len(self.time_arrival) == 0:
            for server_status in self.server_status:
                server_status = 'idle'
            self.time_next_event['depart'] = 1e10
        else:
            self.num_custs_delayed += 1
            self.time_next_event['depart'] = self.sim_time + random.uniform(3, 9)
            client_start_time = self.time_arrival.pop(0)
            current_client_id = self.client_ids_queue.pop(0)
            self.clients_statistics[current_client_id] = self.time_next_event['depart'] - \
                client_start_time
        if self.debug:
            print('depart event at {0:5.2f} size of queue is {1:2d}'.format(
            self.sim_time, len(self.time_arrival)))
        self.clients_done += 1

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
        hosp = Hospital(True)
        hosp.run()
        hosp.show_stats()   
    elif len(sys.argv) == 2:
        for i in range(int(sys.argv[1])):
            stats_filename = "stats/stat" + str(i) + ".json" 
            hosp = Hospital(False)
            hosp.run()
            hosp.save_stats(stats_filename) 

if __name__ == "__main__":
    main()
