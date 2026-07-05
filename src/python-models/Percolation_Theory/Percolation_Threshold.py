import numpy as np
import matplotlib.pyplot as plt


sigma_0 = 20000
phi_c = 0.04
t = 1.5

phi = np.linspace(0, 0.20, 500)

sigma = np.zeros_like(phi)
mask = phi > phi_c
sigma[mask] = sigma_0 * (phi[mask] - phi_c)**t


plt.figure(figsize=(10, 6))
plt.plot(phi * 100, sigma, color='purple', linewidth=3)
plt.axvline(x=phi_c * 100, color='red', linestyle='--', label=f'Percolation Threshold (phi_c = %{phi_c*100})')

plt.title('Auri-Band Conductivity vs. Nanowire Volume Ratio', fontsize=14)
plt.xlabel('Ag2Se Nanowire Volume Ratio (%)', fontsize=12)
plt.ylabel('Electrical Conductivity (S/m)', fontsize=12)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()
plt.show()