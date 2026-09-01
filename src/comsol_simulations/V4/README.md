# Auri-FlexTEG V4
## Multiphysics FEA Study of a Flexible Thermoelectric Generator for Industrial Waste-Heat Harvesting

Auri-FlexTEG V4 is a computational materials and multiphysics design study investigating
a thin, conformal thermoelectric generator (TEG) architecture for harvesting industrial
waste heat.

The project combines thermoelectric transport, heat transfer, electrical conduction,
geometry optimization, and finite-element analysis in COMSOL Multiphysics.

This repository documents the final computational iteration of the project.

> **Project status:** Computational study completed.  
> No physical prototype or experimental validation has been performed.

---

## Research Question

Can a thin, flexible thermoelectric architecture maintain a useful temperature gradient
and electrical potential when attached to a high-temperature industrial surface?

The study focuses on three coupled limitations:

1. Maintaining ΔT across an ultra-thin flexible structure
2. Reducing electrical losses while scaling from a unit cell to an array
3. Improving heat rejection from the cold side of the device

---

## Proposed Architecture

The simulated structure consists of:

- **Flexible substrate:** Polyimide (Kapton)
- **Thermoelectric material:** Ag₂Se/PEDOT:PSS composite
- **Electrical interconnects:** Silver conductive paths
- **Encapsulation:** PDMS-based polymer layer
- **Heat-rejection concept:** BaSO₄-containing upper layer combined with surface micro-features

Representative thermophysical and electrical parameters used in the model are documented
in the simulation files.

These parameters should be interpreted as model inputs rather than experimentally measured
properties of a fabricated device.

---

## Simulation Development

### V1 — Initial Unit Cell

The first simulations established the coupled thermal and electrical model.

The architecture exhibited a major thermal bottleneck: insufficient heat rejection reduced
the temperature gradient across the thermoelectric region.

---

### V2 — Heat-Rejection Modification

The upper structure was modified to improve cold-side heat transfer.

The resulting simulations predicted a larger temperature gradient and therefore increased
thermoelectric potential relative to the initial geometry.

This stage should be interpreted as a numerical design comparison rather than experimental
validation of the cooling mechanism.

---

### V3 — Array Scaling

The optimized unit cell was expanded into a 5 × 4 array.

Electrical connections were arranged using series/parallel combinations to investigate the
trade-off between voltage scaling and internal resistance.

Under the selected boundary conditions:

- Ambient temperature: 25 °C
- Convective heat-transfer coefficient: 15 W/(m²·K)

the model predicted a peak open-circuit potential of approximately 45 mV.

---

### V4 — Adverse Boundary Conditions

The array was subsequently evaluated under a more restrictive simulated environment:

- Ambient temperature: 50 °C
- Convective heat-transfer coefficient: 5 W/(m²·K)

The model predicted:

- Open-circuit voltage ≈ 18 mV
- Internal resistance ≈ 0.0195 Ω

Using the matched-load approximation:

Pmax = Voc² / (4Rint)

the corresponding theoretical maximum electrical output is approximately:

**Pmax ≈ 4.15 mW**

This value represents a simulation result under the stated assumptions and has not been
experimentally verified.

---

## Geometry Scaling Study

A longer patch geometry was also simulated to examine whether the electrical and thermal
model remained numerically stable as the architecture was expanded.

This stage is therefore described as an **array-scale FEA study**, not commercial validation.

The simulation indicates that the architecture can be numerically scaled without losing the
expected spatial potential distribution under the modeled conditions.

---

## FEA Troubleshooting

One of the most important outcomes of the project was not a performance result but a modeling
failure.

During 3D array construction, Boolean difference operations performed after array generation
removed previously assigned electrical boundary selections.

This caused the stationary solver to reach its maximum segregated iterations without convergence.

### Solution

The geometry sequence was restructured:

1. Build the complete unit cell
2. Perform all Boolean operations
3. Preserve the required domains and boundaries
4. Apply the array operation only after the unit-cell geometry is complete

This modification restored the required terminal/ground selections and allowed the model
to converge.

---

## What This Project Demonstrates

The project demonstrates experience with:

- Coupled heat-transfer and electrical FEA
- Thermoelectric transport modeling
- Materials-property selection
- Parametric engineering design
- Series/parallel thermoelectric array architecture
- Boundary-condition sensitivity
- Geometry scaling
- COMSOL solver troubleshooting
- Scientific interpretation of numerical results

---

## Limitations

This project is computational.

Important effects not yet experimentally validated include:

- Real Ag₂Se/PEDOT:PSS composite properties
- Contact resistance
- Interface thermal resistance
- Film thickness variation
- Mechanical bending
- Fabrication defects
- Long-term thermal stability
- Oxidation and environmental degradation
- Real surface emissivity
- Real convective flow around the device
- Experimentally measured power output

Therefore, the reported electrical performance should be considered a **model prediction**
rather than demonstrated device performance.

---

## Project Outcome

Auri-FlexTEG V4 established a complete computational workflow from unit-cell design to
multiphysics array analysis.

The project is currently archived at the computational proof-of-concept stage.

Future experimental work would require fabrication and characterization of the
thermoelectric composite before meaningful model validation could be performed.

For portfolio purposes, the project is considered:

**COMPLETED — COMPUTATIONAL / UNVALIDATED EXPERIMENTALLY**
