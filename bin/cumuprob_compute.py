#!/usr/bin/env python
import sys
import cumuprob_ops
import random

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: %s <data-file1> [<data-file2> [...]]" % sys.argv[0])
        sys.exit(1)
    output = sys.argv[-1]
    use_log = True
    plots = []
    idx = 0
    global_min = None
    for name in sys.argv[1:]:
        lines = open(name).readlines()
        data = list(map(float, filter(lambda x: x[0] != '#', lines)))

        cumu = cumuprob_ops.Prob(data, True)
        min_v = min(data)
        max_v = max(data)
        if (global_min == None):
            global_min = min_v
        else:
            global_min = min(min_v, global_min)

        delta = (max_v-min_v)/float(1000)
        points = [min_v+i*delta for i in range(0, 1000)]
        plots.append([idx, []])
        for t in points:
            plots[-1][1].append((t, cumu.get_qt(t)))
        idx += 1

    print('#!/usr/bin/env gnuplot')
#    print('set term cairolatex pdf standalone size 5cm,5cm')
    print('set term pngcairo')
    print('set size 0.6,0.6')
#    print('set output "%s"' % output)
    print('set xlabel "time"')
    print('set ylabel "probability"')
    if (use_log):
        print('set logscale x')
#        print 'set logscale y'
    print('set key right bottom')
    print('set xrange [%f:]' % global_min)
#    if (not use_log):
#        print 'set xrange [0:]'
    print('set yrange [0:1]')
    print('set pointsize 1.5')

    for i in range(0, len(plots)):
        el = plots[i]
        xoffs = el[1][-1][0]*1.01
        yoffs = 1.01 + float(i) / len(plots)
        print('set arrow from %f,%f to %f, graph %f nohead lc %d' %
              (el[1][-1][0], 1, el[1][-1][0]+xoffs, yoffs, el[0]))
        print('set label "%s" at %f,%f' % (i, el[1][-1][0]+xoffs,
                                           yoffs))
#    print 'plot %s' % (", ".join([('"-" title "%s" with lines' % x[0]) for x in plots]))
    print('plot %s' % (", ".join([('"-" title "" with lines lc %d' %
                                   x[0]) for x in plots])))
    print("\ne\n".join(["\n".join(map(lambda y: "%f %f" % (y[0], y[1]),
                                      x[1])) for x in plots]))

