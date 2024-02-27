# Resilient Computing Systems Simulator

## Project Description
The "Resilient Computing Systems Simulator" is designed to model and simulate two critical aspects of computing systems: process scheduling efficiency and system failure resilience. It features a process scheduling simulator that calculates the dynamics of process arrivals and service durations, alongside a system failure simulation that assesses the resilience of mirrored server setups against simultaneous failures. This tool is invaluable for researchers, system administrators, and IT professionals aiming to enhance the performance and reliability of computing systems.

## How to Use

### Prerequisites
- Python 3.x
- NumPy library

### Installation
1. Ensure Python 3.x is installed on your system.
2. Install NumPy if not already installed: `pip install numpy`

### Running the Simulations

#### Process Scheduling Simulation
1. Navigate to the directory containing the simulation script.
2. Run the command: `python process_scheduling_simulator.py`
   - This executes the process scheduling simulation and outputs the simulation results.

#### System Failure Simulation
1. Navigate to the directory containing the failure simulation script.
2. Run the command: `python system_failure_simulator.py`
   - This executes the system failure simulation, displaying the average time until total system failure.

### Interpreting Results
- The output of the process scheduling simulation will include the ID, arrival time, and service duration for each process, along with the calculated average arrival rate and service duration.
- The system failure simulation outputs the first few failure and restoration times for a single server over a specified period, and the average time until the whole computing system fails due to overlapping server failures.

## Testing
To test the system's behavior under different conditions, modify the parameters at the beginning of each script (e.g., `total_processes`, `lambda_arrival`, `mu_service` for the process scheduling simulation, and `mtbf`, `restore_time`, `years` for the system failure simulation).

## Compatibility
This software is designed to run on any system with Python 3.x installed, including virtual environments such as those provided by Zeus or other cloud-based computing platforms.

## License
This project is open-sourced under the MIT license. Feel free to fork, modify, and use it in your projects with attribution.

---

For more detailed information on customization and extended usage, please refer to the comments within each script.
