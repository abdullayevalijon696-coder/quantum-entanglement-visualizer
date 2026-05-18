from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Bell State (Entanglement) yaratish
qc = QuantumCircuit(2, 2)
qc.h(0)           # Hadamard gate
qc.cx(0, 1)       # CNOT gate
qc.measure([0, 1], [0, 1])

print("Quantum Circuit:")
print(qc.draw())

# Simulyatsiya
simulator = AerSimulator()
result = simulator.run(qc, shots=10000).result()
counts = result.get_counts()

print("\nNatijalar:", counts)

# Vizualizatsiya
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

qc.draw('mpl', ax=ax[0])
ax[0].set_title("Bell State Circuit")

plot_histogram(counts, ax=ax[1])
ax[1].set_title("Measurement Results")

plt.tight_layout()
plt.savefig("bell_state_result.png", dpi=300, bbox_inches='tight')
plt.show()

print("\n✅ Rasm saqlandi: bell_state_result.png")
