def calculate_lab_recipe(target_volume_percent, polymer_mass_g):
    """
    Converts the targeted volumetric leakage threshold (%), into a measurable mass (grams) on a scale.
    """
    density_ag2se = 8.0      # Nanowire Density
    density_pedot = 1.0      # density of PEDOT:PSS polymer matrix
    
    phi = target_volume_percent / 100.0
    
    # Mass ratio of nanowires = (phi * p_wire) / (phi * p_wire + (1-phi) * p_polymer)
    numerator = phi * density_ag2se
    denominator = numerator + ((1 - phi) * density_pedot)
    
    mass_fraction_nw = numerator / denominator
    mass_fraction_polymer = 1 - mass_fraction_nw
    
    required_nw_mass = (polymer_mass_g / mass_fraction_polymer) * mass_fraction_nw
    
    # 4. Laboratuvar Fişini Yazdırma
    print("="*40)
    print("🔬 AURI LABS - COMPOSITE PRESCRIPTION 🔬")
    print("="*40)
    print(f"Targeted Volume Ratio : %{target_volume_percent}")
    print(f"Polymer to be used  : {polymer_mass_g:.2f} gram (PEDOT:PSS)")
    print("-" * 40)
    print(f"AMOUNT OF NANOTELIERS TO BE WEIGHED ON THE SCALE")
    print(f"👉 {required_nw_mass:.2f} gram (Ag2Se)")
    print("="*40)
    print(f"Total Composite Mass: {(polymer_mass_g + required_nw_mass):.2f} gram")

# Test
# Ex: We want %6 Percolation Threshold and we have 50grams of polymer
calculate_lab_recipe(target_volume_percent=6.0, polymer_mass_g=50.0)