## cumuprobs

This is a set of scripts for producing cumulative probabilities from
data and plotting them with `gnuplot`'s `pngcairo` driver.

### Dependecies

- `gnuplot`

### Usage

```bash
mkdir figures; ./bin/cumuprob_compute.py examples/example1.list examples/example2.list figures/example.gp
gnuplot figures/example.gp > figures/example.png
```

### Tuning

Check the file `./bin/cumuprob_compute.py` for adjusting the plot.

