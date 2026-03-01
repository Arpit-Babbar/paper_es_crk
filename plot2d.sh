BASEDIR=$(dirname "$0")
home_dir="$BASEDIR"
run_dir="$home_dir/run"

pvpython "$run_dir/plot_multiion_mhd_khi_color_bar.py"
for no in 10 16 20 24 28 32 36 40; do
    pvpython "$run_dir/plot_multiion_mhd_khi.py" --number $no
done

pvpython "$run_dir/plot_richtmeyer_color_bar.py"
for no in 000 010 020 030 040 050 060 070 080 090 100; do
    pvpython "$run_dir/plot_richtmeyer.py" --number $no
done

pvpython "$run_dir/plot_khi_color_bar.py"
for no in 00 03 10 15; do
    pvpython "$run_dir/plot_khi.py" --number $no
done
