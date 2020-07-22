import yaml
import matplotlib.pyplot as plt
import numpy as np

def main():
    CONFIG =  yaml.load(open('config_global.yaml', 'rU'))
    data = np.genfromtxt('%s/draws.csv' % CONFIG['build']['draw_data'], delimiter =",")
    plt.hist(data)
    plt.xlabel('Draw')
    plt.ylabel('Count')
    plt.title('Histogram')
    plt.text(2, 1700, r'$N(0,1)$')
    plt.savefig('%s/draw_plot.eps' % CONFIG['build']['plot'])

main()