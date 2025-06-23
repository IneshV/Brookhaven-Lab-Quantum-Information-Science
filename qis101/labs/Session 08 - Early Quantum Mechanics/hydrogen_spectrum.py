#!/usr/bin/env python3
"""hydrogen_spectrum.py"""

e = 1.602e-19          # elementary charge (C)
m_e = 9.109e-31        # electron mass (kg)
ε_0 = 8.854e-12        # vacuum permittivity (F/m)
h = 6.626e-34          # Planck's constant (J·s)
c = 2.998e8            # speed of light (m/s)
R = 1.0967757e7        # Rydberg constant (1/m)

# Bohr's formula for ground state energy
e_0 = pow(e_charge, 4) * e_mass / (8 * pow(permittivity, 2) * pow(h_plank, 2))


# ---------------- BOHR FORMULA ----------------
def bohr_wavelength(n_final: int, n_initial: int) -> float:
    """Wavelength (nm) using Bohr energy levels"""
    Ei = -E0 / n_initial**2
    Ef = -E0 / n_final**2
    ΔE = Ei - Ef
    λ_m = h * c / ΔE
    return λ_m * 1e9  # convert to nm


# ---------------- RYDBERG FORMULA ----------------
def rydberg_wavelength(n_final: int, n_initial: int) -> float:
    """Wavelength (nm) using Rydberg's formula"""
    inverse_lambda = R * (1 / n_final**2 - 1 / n_initial**2)
    λ_m = 1 / inverse_lambda
    return λ_m * 1e9  # convert to nm


# ---------------- Display table ----------------
def show_series(series_name: str, n_final: int):
    print(f"{series_name} Series (n = {n_final})")
    print("-" * 40)
    print(f"{'nᵢ → nᶠ':<10} {'Bohr (nm)':>12} {'Rydberg (nm)':>15}")
    for n_i in range(n_final + 1, n_final + 6):
        λ_bohr = bohr_wavelength(n_final, n_i)
        λ_rydberg = rydberg_wavelength(n_final, n_i)
        print(f"{n_i:>2} → {n_final:<2}   {λ_bohr:12.1f}   {λ_rydberg:15.1f}")
    print()


# ---------------- Main ----------------
def main():
    show_series("Pfund", 5)
    show_series("Humphreys", 6)


if __name__ == "__main__":
    main()
