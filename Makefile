.SUFFIXES: .pdf .gp

all:
	@echo "Provide a .gp file as an argument"

.gp.pdf: %.gp %.list macros.tex
	gnuplot $<
	pdflatex $*.tex
	mv `basename $*`.pdf `dirname $*`
	rm -f `basename $*`.{aux,log}
	rm -f `dirname $*`/`basename $* .pdf`-inc.pdf
	rm -f `dirname $*`/`basename $* .pdf`.tex

