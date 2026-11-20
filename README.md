# Water-Filling Algorithm Simulation

## Project Overview

This project implements and compares two power allocation methods in a discrete Rayleigh fading communication channel using Python.

The main objective is to evaluate the performance of the Water-Filling algorithm compared to Uniform Power Allocation in terms of channel capacity.

## System Parameters

- Number of subchannels: 8
- Total transmission power: 100
- Noise power: 1
- Channel model: Rayleigh Fading

## Power Allocation Methods

### 1. Uniform Power Allocation

In this method, the total transmission power is distributed equally among all subchannels.

### 2. Water-Filling Algorithm

In this method, transmission power is allocated according to the channel conditions. More power is assigned to subchannels with better channel gains, while weaker subchannels may receive less or no power.

## Channel Capacity

The channel capacity is calculated using the Shannon capacity formula:

C = sum(log2(1 + Pi * gi / N0))

Where:

- C: Total channel capacity
- Pi: Power allocated to each subchannel
- gi: Channel gain
- N0: Noise power

## Implementation

The project is implemented in Python using the following libraries:

- NumPy: Numerical calculations and channel simulation
- Matplotlib: Plotting and visualization

## How to Run

1. Install Python.
2. Install the required libraries:

   pip install -r requirements.txt

3. Run the Python script:

   python water_filling.py

## Results

The program generates random Rayleigh fading channel conditions and compares the two power allocation methods.

It displays:

- Channel gain of each subchannel
- Power allocation comparison
- Channel capacity for both methods
- Percentage of capacity improvement

Since the channel gains are randomly generated, the numerical results and plots may change with each execution.

## Conclusion

The Water-Filling algorithm provides an optimal power allocation strategy for maximizing channel capacity under a total power constraint and is compared with Uniform Power Allocation in this project.
