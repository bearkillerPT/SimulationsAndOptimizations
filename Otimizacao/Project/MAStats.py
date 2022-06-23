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


servers = [[78, 50, 33, 40, 74, 13, 49, 42],
           [40, 74, 50, 13, 49, 33, 78, 42],
           [50, 33, 74, 42, 78, 49, 40, 13],
           [40, 78, 49, 13, 74, 42, 33, 50],
           [78, 50, 74, 42, 13, 49, 40, 33],
           [50, 74, 40, 78, 13, 33, 49, 42],
           [78, 47, 49, 50, 13, 35, 74, 40],
           [49, 33, 78, 50, 13, 74, 40, 42],
           [50, 40, 13, 49, 33, 78, 74, 42],
           [13, 49, 74, 50, 40, 78, 42, 33]]

connp = [943, 943, 943, 943, 943, 943, 952, 943, 943, 943]

times = [100.2100, 89.3253, 41.3196, 82.1311, 111.9374,
         59.3975, 54.1134, 41.6176, 71.0139, 58.6268]
print("CONNP")
print(stats_stat(connp))
print("TIMES")
print(stats_stat(times))