import numpy as np
import matplotlib.pyplot as plt

# System parameters
N = 8
P_total = 100
N0 = 1

# Generate Rayleigh fading channel
h = (np.random.randn(N) + 1j * np.random.randn(N)) / np.sqrt(2)
g = np.abs(h) ** 2

# Uniform Power Allocation
P_uniform = np.ones(N) * (P_total / N)

# Water-Filling Algorithm
low = 0
high = P_total + np.max(N0 / g)

for i in range(100):
    mu = (low + high) / 2
    P_water = np.maximum(0, mu - N0 / g)

    if np.sum(P_water) > P_total:
        high = mu
    else:
        low = mu

# Final power allocation
mu = (low + high) / 2
P_water = np.maximum(0, mu - N0 / g)

# Calculate channel capacities
C_uniform = np.sum(np.log2(1 + P_uniform * g / N0))
C_water = np.sum(np.log2(1 + P_water * g / N0))

# Print results
print("Channel Gains:")
print(g)

print("\nUniform Power Allocation:")
print(P_uniform)

print("\nWater-Filling Power Allocation:")
print(P_water)

print("\nTotal Uniform Power:", np.sum(P_uniform))
print("Total Water-Filling Power:", np.sum(P_water))

print("\nCapacity with Uniform Allocation:", C_uniform, "bits/s/Hz")
print("Capacity with Water-Filling:", C_water, "bits/s/Hz")

print("\nCapacity Improvement:",
      ((C_water - C_uniform) / C_uniform) * 100, "%")

# Plot 1: Channel Gains
plt.figure(figsize=(8, 5))
plt.bar(range(1, N + 1), g)
plt.xlabel("Subchannel Number")
plt.ylabel("Channel Gain")
plt.title("Channel Gains")
plt.grid(axis="y")
plt.show()

# Plot 2: Power Allocation Comparison
plt.figure(figsize=(8, 5))
width = 0.35

plt.bar(np.arange(1, N + 1) - width / 2,
        P_uniform, width, label="Uniform")

plt.bar(np.arange(1, N + 1) + width / 2,
        P_water, width, label="Water-Filling")

plt.xlabel("Subchannel Number")
plt.ylabel("Allocated Power")
plt.title("Power Allocation Comparison")
plt.legend()
plt.grid(axis="y")
plt.show()