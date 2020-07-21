import yaml
import matplotlib.pyplot as plt

def main():
    CONFIG =  yaml.load(open('config_global.yaml', 'rU'))

    plt.hist('%s/draws.csv' % CONFIG['build']['draw_data'])
    plt.savefig('%s/draw_plot.eps' % CONFIG['build']['plot'])

main()