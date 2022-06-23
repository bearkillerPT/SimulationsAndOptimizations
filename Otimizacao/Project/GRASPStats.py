import sys
import json
import statistics


def print_stat(stat):
    print("\tAvg: -> " + str(stat["avg"]) + " s")
    print("\tStd deviation -> " + str(stat["std_d"]))
    print("\tMedian -> " + str(stat["median"]))


def stats_stat(stat):
    return {
        "avg": statistics.mean(stat),
        "std_d": statistics.stdev(stat),
        "median": statistics.median(stat)
    }


servers = [[22, 93, 20, 38, 1, 21, 18, 24],
           [93, 22, 38, 20, 1, 13, 18, 32],
           [22, 38, 20, 93, 1, 13, 18, 32],
           [22, 38, 20, 93, 1, 13, 18, 32],
           [22, 20, 38, 93, 1, 13, 18, 32],
           [22, 20, 93, 38, 13,  9, 21, 26],
           [22, 93, 20, 38, 1, 13, 18, 32],
           [22, 93, 20, 38, 1, 13, 18, 32],
           [13, 93,  9, 21, 22, 26, 20, 38],
           [22, 20, 93, 38, 1, 21, 18, 24]]

connp = [2521, 2516, 2516, 2516, 2516, 2574, 2516, 2516, 2574, 2521]

times = [92.4973, 72.5501, 168.8381, 45.9820, 174.3291,
         2.9128, 266.7612, 187.6602, 7.3633, 295.8131]


print("CONNP")
print(stats_stat(connp))
print("TIMES")
print(stats_stat(times))
