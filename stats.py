import sys
import json
import statistics

def print_stat(stat):
    print("\tAvg: -> " + str(stat["avg"]) + " s")
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
    delays = []
    queue_sizes = []
    server_freqs = []
    for i in range(int(sys.argv[1])):
        try:
            fp = open("stats/stat" + str(i) + ".json")
            current_stats = json.load(fp)
            delays.append(current_stats["avg_delay"])
            queue_sizes.append(current_stats["avg_queue_size"])
            server_freqs.append(current_stats["server_freq"])
        except Exception as e:
            print(e)
    print("RESULTS AFTER " + sys.argv[1] + " RUNS")
    print("Delays:")
    print_stat(stats_stat(delays))
    print("Queue Sizes:")
    print_stat(stats_stat(queue_sizes))
    print("Server Frequencies:")
    print_stat(stats_stat(server_freqs))


if __name__ == "__main__":
    main()
