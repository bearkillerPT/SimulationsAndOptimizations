
# based on Simulation Modeling and Analysis, Averil Law

import random
import statistics
import sys
import json
import os

from numpy import min_scalar_type


class ServiceFacility:
    def __init__(self, debug):
        self.sim_time = 0.0
        self.client_id_s1 = 0
        self.client_id_s2 = 0
        self.client_ids_queue_s1 = []
        self.client_ids_queue_s2 = []
        self.size_of_queue_s1 = []
        self.size_of_queue_s2 = []
        self.clients_statistics_s1 = {}
        self.clients_statistics_s2 = {}
        self.clients_done_s1 = 0
        self.clients_done_s2 = 0
        # state variables
        self.server1_status = 'idle'
        self.server2_status = 'idle'

        # statistics
        self.num_custs_delayed_s1 = 0
        self.num_custs_delayed_s2 = 0

        # event list server 1
        self.time_next_event_s1 = {}
        self.time_next_event_s1['arrive'] = self.sim_time + \
            random.expovariate(1)
        self.time_next_event_s1['depart'] = 1e10
        self.next_event_type_s1 = ''
        self.time_arrival_s1 = []

        # event list server 2
        self.time_next_event_s2 = {}
        self.time_next_event_s2['arrive'] = 1e10
        self.time_next_event_s2['depart'] = 1e10
        self.next_event_type_s2 = ''
        self.time_arrival_s2 = []
        self.debug = debug

    def timing(self):

        min_time_next_event_s1 = 1e9
        min_time_next_event_s2 = 1e9

        next_event_type = ''
        self.next_event_type_s1 = ''
        for e in self.time_next_event_s1:
            if self.time_next_event_s1[e] < min_time_next_event_s1:
                min_time_next_event_s1 = self.time_next_event_s1[e]
                next_event_type = e

        self.next_event_type_s2 = ''
        for e in self.time_next_event_s2:
            if self.time_next_event_s2[e] <= min_time_next_event_s2:
                min_time_next_event_s2 = self.time_next_event_s2[e]
                if min_time_next_event_s2 < min_time_next_event_s1:
                    next_event_type = e

        min_time_next_event = 0

        if min_time_next_event_s1 < min_time_next_event_s2:
            self.next_event_type_s1 = next_event_type
            min_time_next_event = min_time_next_event_s1
        else:
            self.next_event_type_s2 = next_event_type
            min_time_next_event = min_time_next_event_s2
        if self.next_event_type_s1 == '' and self.next_event_type_s2 == '':
            print('There is no event to be performed at the time', self.sim_time)
            sys.exit()

        self.sim_time = min_time_next_event
        if min_time_next_event < self.run_time:
            return True
        return False

    def arrive_s1(self):
        self.time_next_event_s1['arrive'] = self.sim_time + \
            random.expovariate(1)

        if self.server1_status == 'busy':
            self.time_arrival_s1.append(self.sim_time)
            self.client_ids_queue_s1.append(self.client_id_s1)
            self.client_id_s1 += 1
        else:
            self.num_custs_delayed_s1 += 1
            self.server1_status = 'busy'
            self.time_next_event_s1['depart'] = self.sim_time + \
                random.expovariate(10/7)
        self.size_of_queue_s1.append(len(self.time_arrival_s1))
        if self.debug:
            print('arrive event at {0:5.2f} size of queue is {1:2d}'.format(
                self.sim_time, len(self.time_arrival_s1)))

    def depart_s1(self):
        self.time_next_event_s1['depart'] = 1e10
        if self.server2_status == 'idle':
            self.time_next_event_s2['arrive'] = self.sim_time

        else:
            self.server1_status = 'busy'

        if self.debug:
            print('depart event at {0:5.2f} size of queue is {1:2d}'.format(
                self.sim_time, len(self.time_arrival_s1)))
        self.clients_done_s1 += 1

    def arrive_s2(self):

        self.time_next_event_s2['arrive'] = 1e10
        self.num_custs_delayed_s2 += 1
        self.server2_status = 'busy'
        self.time_next_event_s2['depart'] = self.sim_time + \
            random.expovariate(10/9)
        

        self.size_of_queue_s2.append(len(self.time_arrival_s2))
        if self.debug:
            print('arrive event at {0:5.2f} size of queue is {1:2d}'.format(
                self.sim_time, len(self.time_arrival_s2)))

    def depart_s2(self):
        self.time_next_event_s1['depart'] = self.time_next_event_s2['depart']
        self.time_next_event_s2['depart'] = 1e10
        self.server2_status = 'idle'
        if not len(self.time_arrival_s1) == 0:
            self.num_custs_delayed_s1 += 1
            client_start_time = self.time_arrival_s1.pop(0)
            current_client_id = self.client_ids_queue_s1.pop(0)
            self.clients_statistics_s1[current_client_id] = self.time_next_event_s1['depart'] - client_start_time
        if self.debug:
            print('depart event at {0:5.2f} size of queue is {1:2d}'.format(
                self.sim_time, len(self.time_arrival_s2)))
        self.clients_done_s2 += 1

    def run(self, run_time):
        self.run_time = run_time
        while self.timing():
            if self.next_event_type_s1 != '':
                if self.debug:
                    print("Server1")
                if self.next_event_type_s1 == 'arrive':
                    self.arrive_s1()
                elif self.next_event_type_s1 == 'depart':
                    self.depart_s1()
            if self.next_event_type_s2 != '':
                if self.debug:
                    print("Server 2")
                if self.next_event_type_s2 == 'arrive':
                    self.arrive_s2()

                elif self.next_event_type_s2 == 'depart':
                    self.depart_s2()

    def show_stats_s1(self):
        print("*\nServer 1")
        clients = len(self.clients_statistics_s1.keys())
        avg_delay = 0
        if(clients):
            print("*\nAvg delay:")
            avg_delay = statistics.mean(self.clients_statistics_s1.values())
            print(avg_delay)
        avg_queue_size = statistics.mean(self.size_of_queue_s1)
        print("\nAvg queue size:")
        print(avg_queue_size)
        print("\nServer Frequency:")
        server_freq = self.clients_done_s1/self.sim_time
        print(server_freq)

    def show_stats_s2(self):
        print("*\nServer 2")
        clients = len(self.clients_statistics_s2.keys())
        avg_delay = 0
        if(clients):
            print("*\nAvg delay:")
            avg_delay = statistics.mean(self.clients_statistics_s2.values())
            print(avg_delay)
        avg_queue_size = statistics.mean(self.size_of_queue_s2)
        print("\nAvg queue size:")
        print(avg_queue_size)
        print("\nServer Frequency:")
        server_freq = self.clients_done_s2/self.sim_time
        print(server_freq)

    def save_stats(self, filename):
        clients_s1 = len(self.clients_statistics_s1.keys())
        avg_delay_s1 = 0
        if(clients_s1):
            avg_delay_s1 = sum(self.clients_statistics_s1.values())/clients_s1
        avg_queue_size_s1 = sum(self.size_of_queue_s1) / \
            len(self.size_of_queue_s1)
        server_freq_s1 = self.clients_done_s1/self.sim_time
        clients_s2 = len(self.clients_statistics_s2.keys())
        avg_delay_s2 = 0
        if(clients_s2):
            avg_delay_s2 = sum(self.clients_statistics_s2.values())/clients_s2
        avg_queue_size_s2 = sum(self.size_of_queue_s2) / \
            len(self.size_of_queue_s2)
        server_freq_s2 = self.clients_done_s2/self.sim_time

        if not os.path.exists('stats'):
            os.makedirs('stats')
        fp = open(filename, 'w')
        fp.write(
            json.dumps({
                "server1": {
                    "avg_delay": avg_delay_s1,
                    "avg_queue_size": avg_queue_size_s1,
                    "server_freq": server_freq_s1
                },
                "server2": {
                    "avg_delay": avg_delay_s2,
                    "avg_queue_size": avg_queue_size_s2,
                    "server_freq": server_freq_s2
                }
            }))
        # main


def usage():
    print("\nThis file contains the service facilty class and is not meant to be called on it's own!\nInstead run sim.py\n")


if __name__ == "__main__":
    usage()
