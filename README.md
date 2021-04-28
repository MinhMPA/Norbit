N <img src="Norbit_logo.jpeg" alt="drawing" width="35" align="top"/>
==========

*Norbit - yet another (lite) toy N-body simulation*
--------------------

This mini package provides a proof-of-concept of N-body simulations of systems that evolve under only gravitational forces.

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) ![](https://img.shields.io/github/commit-activity/m/MinhMPA/Norbit) ![](https://img.shields.io/github/last-commit/MinhMPA/Norbit)

## Currently Implemented Features


- Direct summation for force evaluation, which scales as <img src="https://latex.codecogs.com/gif.latex?\mathcal{O}(N^2)" title="\mathcal{O}(N^2)" />
- 2nd-order symplectic and 4th-order non-symplectic integrators

## Examples

- An example of initial conditions for the Outer Solar System is provided at `./examples/initial_conditions_outer_solar.py`. The example is taken from section I.2.4 of <a href=”https://link.springer.com/book/10.1007/3-540-30666-8”> Geometric Numerical Integration, Hairer 2006</a>.
- For more details, please see the notebook `./Norbit_demo.ipynb`

![Orbits](./examples/Example_orbits_in_Outer_Solar_System.png)

![Relative error in total momentum](./examples/Example_total_momentum_conservation_during_orbit_simulation.png)
