import Pkg
Pkg.activate(joinpath(@__DIR__, ".."))

# Convergence tests
include(joinpath(@__DIR__, "convergence.jl")) # Isentropic and multi-ion convergence test
include(joinpath(@__DIR__, "plot_convergence.jl")) # Plotting convergence results

# KHI test case from Chan et al. 2022
include(joinpath(@__DIR__, "run_khi_chan2022.jl"))

# Richmyer-Meshkov instability test case
include(joinpath(@__DIR__, "run_richtmeyer_meshkov_chan.jl"))

# Multi-ion KHI
include(joinpath(@__DIR__, "run_multiion_khi_crk_es.jl"))
