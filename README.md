## cumuprobs

This is a set of scripts for producing cumulative probabilities from
data and plotting them with `gnuplot`'s `epslatex` driver.

### Dependecies

- `latex`
- `gnuplot`
- `dvips` (shipped with `latex`?)

### Usage

```
$ mkdir figures; ./bin/cumuprob_compute.py examples/example1.list examples/example2.list figures/example.tex
$ make figures/example.pdf
```

The result is

```
$ ls figures
example.gp      example.pdf
```

### Tuning

Check the file `./bin/cumuprob_compute.py` for adjusting the plot.

