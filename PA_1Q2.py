import numpy as np


def generate_failures(mtbf, restore_time, years):
  total_hours = years * 365 * 24  # Total hours in 20 years
  failures = []
  current_time = 0
  while current_time < total_hours:
    # Generate next failure time based on Exponential distribution
    next_failure = np.random.exponential(mtbf)
    current_time += next_failure
    if current_time < total_hours:
      failures.append((current_time, current_time + restore_time))
      current_time += restore_time  # Add restore time before next failure
  return failures


def simulate_system_failure(mtbf, restore_time, years, num_simulations=1000):
  total_failures_time = 0
  for _ in range(num_simulations):
    np.random.seed()  # Ensure different seeds for each simulation
    server1_failures = generate_failures(mtbf, restore_time, years)
    server2_failures = generate_failures(mtbf, restore_time, years)

    # Check for overlap between any two failures in server1 and server2
    for f1_start, f1_end in server1_failures:
      for f2_start, f2_end in server2_failures:
        if f1_start < f2_end and f2_start < f1_end:  # If failures overlap
          total_failures_time += min(f1_end, f2_end) - max(f1_start, f2_start)
          break

  average_failure_time = total_failures_time / num_simulations
  return average_failure_time


# Part (a): Generate synthetic data for one server over 20 years
years = 20
mtbf = 500  # Mean Time Between Failures in hours
restore_time = 10  # Restoration time in hours
server_failures = generate_failures(mtbf, restore_time, years)

# Display first 5 failures for demonstration
print("First 5 failures and restoration times for a server over 20 years:")
for i, (fail, restore) in enumerate(server_failures[:5], 1):
  print(f"{i}. Failure at hour {fail:.2f}, restored by hour {restore:.2f}")

# Part (b): Find out how long until the whole system fails
average_system_fail_time = simulate_system_failure(mtbf, restore_time, years)
print(
    f"\nAverage time until the whole computing system fails: {average_system_fail_time}"
)
