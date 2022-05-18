import sys
import json
import statistics

def print_stat(stat):
    print("\tAvg: -> " + str(stat["avg"]))
    print("\tStd deviation -> " + str(stat["std_d"]))
    print("\tMedian -> " + str(stat["median"]))
    
    
def stats_stat(stat):
    return {
        "avg" : statistics.mean(stat),
        "std_d" : statistics.stdev(stat),
        "median": statistics.median(stat)
    }
def main():
    if len(sys.argv) == 1:
        print("You must provide a number of tests already ran with sim1.py\n\tpython3 sim1.py number_tests?")
        sys.exit(0)
    delays_s1 = []
    queue_sizes_s1 = []
    server_freqs_s1 = []
    delays_s2 = []
    queue_sizes_s2 = []
    server_freqs_s2 = []
    total_events = []
    for i in range(int(sys.argv[1])):
        try:
            fp = open("stats/stat" + str(i) + ".json")
            current_stats = json.load(fp)
            delays_s1.append(current_stats["server1"]["avg_delay"])
            queue_sizes_s1.append(current_stats["server1"]["avg_queue_size"])
            server_freqs_s1.append(current_stats["server1"]["server_freq"])
            delays_s2.append(current_stats["server2"]["avg_delay"])
            queue_sizes_s2.append(current_stats["server2"]["avg_queue_size"])
            server_freqs_s2.append(current_stats["server2"]["server_freq"])
            total_events.append(current_stats["EventsCount"])
        except Exception as e:
            print(e)
    print("RESULTS AFTER " + sys.argv[1] + " RUNS\n*\nServer 1\n*")
    print("Delays:")
    print_stat(stats_stat(delays_s1))
    print("Queue Sizes:")
    print_stat(stats_stat(queue_sizes_s1))
    print("Server Frequencies:")
    print_stat(stats_stat(server_freqs_s1))
    print("*\nServer 2\n*")
    print("Delays:")
    print_stat(stats_stat(delays_s2))
    print("Queue Sizes:")
    print_stat(stats_stat(queue_sizes_s2))
    print("Server Frequencies:")
    print_stat(stats_stat(server_freqs_s2))
    print("Total Events:")
    print_stat(stats_stat(total_events))


if __name__ == "__main__":
    main()
