# Compact Runge-Kutta flux reconstruction methods with entropy conservative fluxes

[![License: MIT](https://img.shields.io/badge/License-MIT-success.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/?.svg)](https://zenodo.org/doi/?)

This repository contains information and code to reproduce the results
presented in the article
```bibtex
@online{babbar2026crkes,
  title={Compact Runge-Kutta flux reconstruction methods with entropy and/or kinetic energy preserving fluxes},
  author={Babbar, Arpit and Chen, Qifan and Ranocha, Hendrik},
  year={2026},
  month={4},
  eprint={?},
  eprinttype={arxiv},
  eprintclass={math.NA}
}
```

If you find these results useful, please cite the article mentioned above.
If you use the implementations provided here, please **also** cite this repository as
```bibtex
@misc{babbar2026crkes,
  title={Reproducibility repository for
         "Compact Runge-Kutta flux reconstruction methods with entropy and/or kinetic energy preserving fluxes"},
  author={Babbar, Arpit and Chen, Qifan and Ranocha, Hendrik},
  year={2026},
  howpublished={\url{https://github.com/Arpit-Babbar/paper_crk_es}},
  doi={10.5281/zenodo.19388796}
}
```

## Abstract

Compact Runge-Kutta (cRK) methods are a class of high order methods for solving hyperbolic conservation laws characterized by their compact stencil including only immediate neighboring finite elements.
A Compact Runge-Kutta flux reconstruction (cRKFR) method for solver hyperbolic conservation laws was introduced in [Babbar, A., Chen, Q., Journal of Scientific Computing, 2025] which uses a time average flux formulation to perform evolution using a single numerical flux computation at each step, making it a single stage method.
Entropy or kinetic energy preserving numerical fluxes are often used for construction of high order entropy stable or kinetic energy preserving methods for hyperbolic conservation laws, and are known to enhance the robustness of numerical methods for under-resolved simulations.
In this work, we show how these fluxes can be incorporated into the cRKFR framework for general hyperbolic equations that consist of fluxes and non-conservative products.
We test the effectiveness of this new class of methods through numerical experiments for the compressible Euler equations, magnetohydronamics (MHD) equations and multi-ion MHD equations.
It is observed that the application of entropy or kinetic energy preserving fluxes enhances the robustness of the cRKFR methods.

## Numerical experiments

In order to generate the results from this repository, you need to install [Julia](https://julialang.org).
We recommend using `juliaup`, as detailed in the official website [https://julialang.org](https://julialang.org).

The results have been generated using Julia version 1.10.10, and we recommend installing the same.
Once you have installed Julia, you can clone this repository, enter this directory and start the executable `julia` with the following steps

```shell
git clone https://github.com/Arpit-Babbar/jin_xin_shock_capturing
cd jin_xin_shock_capturing
julia --project=. --threads=auto
```

Then enter the following commands to generate all the data, and plot the 1-D results

```julia
julia> include("run_all_and_plot_convergence.jl") # Generate all data
```

If you wish to visualize the 2D figures, you need [ParaView](https://www.paraview.org) and its command line version `pvpython`.
Then, in your shell, you can run

```shell
bash plot2d.sh
```

All the figures are now ready and available in the home directory of the repository

## Authors

- [Arpit Babbar](https://babbar.dev) (Johannes Gutenberg University Mainz, Germany)
- [Qifan Chen](https://qifan-chen.github.io) (The Ohio State University, USA)
- [Hendrik Ranocha](https://ranocha.de) (Johannes Gutenberg University Mainz, Germany)

## License

The code in this repository is published under the MIT license, see the `LICENSE` file.

## Disclaimer

Everything is provided as is and without warranty. Use at your own risk!
