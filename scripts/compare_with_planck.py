#!/usr/bin/env python3
"""Сравнение предсказания MEML v6.9 с Planck 2018."""
meml_value = 0.1188
planck_value = 0.120
planck_error = 0.001

deviation = abs(meml_value - planck_value) / planck_value * 100

print("=" * 50)
print("MEML v6.9 vs Planck 2018")
print("=" * 50)
print(f"MEML:    Omega_wdm h^2 = {meml_value:.4f}")
print(f"Planck:  Omega_DM  h^2 = {planck_value:.4f} +/- {planck_error:.4f}")
print(f"Deviation: {deviation:.2f}%")
print("=" * 50)

if deviation < 2.0:
    print("MATCH within 2% - model is consistent!")