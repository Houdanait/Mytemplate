import yaml
import numpy as np

def main():
    CONFIG = yaml.load(open('config_global.yaml', 'rU'))
    np.random.seed(1)
    draw = np.random.normal(size=10000)

    np.savetxt('%s/draws.csv' % CONFIG['build']['draw_data'], draw, delimiter=',')

main()
