import random
import numpy as np

def create_process_sequence(total_processes, lambda_arrival, mu_service):
    processes = []
    current_time = 0
    for process_id in range(total_processes):
        # Calculating the time between arrivals
        arrival_gap = np.random.exponential(1.0 / lambda_arrival)
        current_time += arrival_gap
        # Determining the duration of service
        duration_of_service = np.random.exponential(1.0 / mu_service)
        processes.append((process_id + 1, current_time, duration_of_service))
    return processes

# Setting the parameters for the simulation
total_processes = 1000
lambda_arrival = 2  # Rate of arrival
mu_service = 1      # Rate of service
scheduled_processes = create_process_sequence(total_processes, lambda_arrival, mu_service)

# Deriving the real arrival rate and service duration averages
arrival_intervals = [process[1] for process in scheduled_processes]
durations = [process[2] for process in scheduled_processes]
real_arrival_rate = total_processes / (arrival_intervals[-1] - arrival_intervals[0])
average_duration = np.mean(durations)

print("Process ID, Time of Arrival, Requested time of Service")
for process in scheduled_processes:
    print(process)

print("\nCalculated average rate of arrival:", real_arrival_rate)
print("Calculated average service duration:", average_duration)
