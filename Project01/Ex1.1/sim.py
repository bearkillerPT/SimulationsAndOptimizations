from ServiceFacility import ServiceFacility
import sys

def main():
    # initialize
    # simulation clock
    if len(sys.argv) == 1:
        simulation = ServiceFacility(False)
        simulation.run(1000)
        simulation.show_stats_s1()   
        simulation.show_stats_s2()   
    elif len(sys.argv) == 2:
        for i in range(int(sys.argv[1])):
            stats_filename = "stats/stat" + str(i) + ".json" 
            simulation = ServiceFacility(False)
            simulation.run(1000)
            simulation.save_stats(stats_filename) 

if __name__ == "__main__":
    main()