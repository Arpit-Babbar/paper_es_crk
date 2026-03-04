import Pkg
Pkg.activate(joinpath(@__DIR__,".."))
using Tenkai
using Tenkai.TenkaicRK
using Tenkai.TenkaicRK: PicardSolver
using Tenkai.Trixi

using TrixiBase: trixi_include
using Tenkai.DelimitedFiles
import Tenkai.TimerOutputs as to

function sol_error(sol)
    return sol["errors"]["l2_error"]
end

function sol_time(sol)
    full_time = to.tottime(sol["aux"].timer)
    write_time = to.time(sol["aux"].timer["Write solution"])
    err_time = to.time(sol["aux"].timer["Compute error"])
    @show full_time, write_time, err_time
    return (full_time - write_time - err_time) * 1e-9
end

run_file = joinpath(@__DIR__, "run_multiion_convergence.jl")

final_time_global = 2.0
nx_array = [16, 32, 64, 128]
nx_length = length(nx_array)
array_gll = Vector([zeros(nx_length, 3) for _ in 1:3])

volume_integral = Trixi.VolumeIntegralFluxDifferencing((Trixi.flux_ruedaramirez_etal,
                                                        Trixi.flux_nonconservative_ruedaramirez_etal))

# Only cRK44 is implemented with the flux differencing volume integral
degree2crk = Dict(1 => cRK44(volume_integral), 2 => cRK44(volume_integral), 3 => cRK44(volume_integral))
#=
for (i, nx) in enumerate(nx_array)
    for degree in 1:3
        trixi_include(run_file, solver = degree2crk[degree],
                      degree = degree, final_time = 1e-6, nx = nx, ny = nx)
        sol_gll = trixi_include(run_file, solver = degree2crk[degree],
                                degree = degree, final_time = final_time_global, nx = nx,
                                ny = nx, solution_points = "gll",
                                correction_function = "g2",
                                limiter = setup_limiter_none(),
                                bflux = evaluate)
        error_gll = sol_error(sol_gll)
        time_gll = sol_time(sol_gll)
        array_gll[degree][i, 1:3] .= nx, error_gll, time_gll
    end
end

mkpath(joinpath(@__DIR__, "results"))
for degree in 1:3
    writedlm(joinpath(@__DIR__, "results", "multiion_convergence_gll$(degree).txt"),
             array_gll[degree])
end
=#
# Isentropic vortex

final_time_global = 20 * sqrt(2.0) / 0.5
volume_integral = Trixi.VolumeIntegralFluxDifferencing((Trixi.flux_ranocha_turbo,
                                                        nothing))
solver = cRK44(volume_integral)
nx_array = [64, 128, 256, 512]
run_file = joinpath(@__DIR__, "run_isentropic.jl")
for (i, nx) in enumerate(nx_array)
    for degree in 1:3
        # trixi_include(run_file, solver = solver,
        #               degree = degree, final_time = 1e-6, nx = nx, ny = nx,
        #               solution_points = "gll", correction_function = "g2",
        #               bflux = evaluate, limiter = setup_limiter_none())
        sol_gll = trixi_include(run_file, solver = solver,
                                degree = degree, final_time = final_time_global, nx = nx,
                                ny = nx, solution_points = "gll",
                                correction_function = "g2",
                                limiter = setup_limiter_none(),
                                cfl_safety_factor = 0.5,
                                bflux = extrapolate)
        error_gll = sol_error(sol_gll)
        time_gll = sol_time(sol_gll)
        array_gll[degree][i, 1:3] .= nx, error_gll, time_gll
    end
end

mkpath(joinpath(@__DIR__, "results"))
for degree in 1:3
    writedlm(joinpath(@__DIR__, "results", "isentropic_convergence_gll$(degree).txt"),
             array_gll[degree])
end
