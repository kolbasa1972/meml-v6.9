#!/usr/bin/env python3
"""Построение эволюции Omega_wdm h^2 (T) из вывода sterile-dm."""
import re
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

raw_file = Path("../data/output_T_evolution.dat")
lines = raw_file.read_text().splitlines()

T_list, omega_list = [], []
pattern = re.compile(r"T=\s*([\d.E+-]+).*Omega_wdm h\^2=\s*([\d.E+-]+)")

for line in lines:
    m = pattern.search(line)
    if m:
        T_list.append(float(m.group(1)))
        omega_list.append(float(m.group(2)))

T_arr = np.array(T_list)
omega_arr = np.array(omega_list)

fig, ax = plt.subplots(figsize=(8, 5))
ax.semilogx(T_arr, omega_arr, 'b-', lw=2, label='MEML v6.9')
ax.axhline(0.120, color='red', ls='--', lw=1.5,
           label='Planck 2018: 0.120')
ax.axhline(0.1188, color='green', ls=':', lw=1.5,
           label='MEML: 0.1188')

ax.set_xlabel('T [MeV]', fontsize=12)
ax.set_ylabel('Omega_wdm h^2', fontsize=12)
ax.set_title('Relic density of dark matter (MEML v6.9)', fontsize=13)
ax.set_xlim(10, 1e4)
ax.set_ylim(0, 0.25)
ax.legend(loc='lower left', fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('../paper/figures/omega_dm_evolution.pdf', dpi=150)
print("Saved: paper/figures/omega_dm_evolution.pdf")