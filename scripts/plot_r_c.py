#!/usr/bin/env python3
"""Построение r_c(M_6) из MEML v6.9."""
import numpy as np
import matplotlib.pyplot as plt

M6_TeV = np.logspace(0, 2, 200)
r_c_mkm = 2.4e-3 / M6_TeV**2 * 1e6

fig, ax = plt.subplots(figsize=(8, 5))
ax.loglog(M6_TeV, r_c_mkm, 'b-', lw=2, label='MEML v6.9')
ax.axhline(160, ls='--', lw=1.5, label='Eot-Wash (2004)')
ax.axhline(10, ls='--', lw=1.5, label='Stanford (2007)')
ax.axhline(1, ls='--', lw=1.5, label='Future')

ax.set_xlabel('M_6 [TeV]', fontsize=12)
ax.set_ylabel('r_c [microns]', fontsize=12)
ax.set_title('Crossover scale MEML v6.9', fontsize=13)
ax.set_xlim(1, 100)
ax.set_ylim(1e-2, 1e3)
ax.legend(loc='upper right', fontsize=9)
ax.grid(True, which='both', alpha=0.3)

plt.tight_layout()
plt.savefig('../paper/figures/r_c_vs_M6.pdf', dpi=150)
print("Saved: paper/figures/r_c_vs_M6.pdf")