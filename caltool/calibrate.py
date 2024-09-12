from torch import inverse
from .utils import * 
from .io import *
from numpy.polynomial import Polynomial
import json

def create_calibration_curve(device_name,
                             reference_values=None, # the values set
                             measured_values=None, # the values recorded
                             polyorder=1, # by default, linear
                             dry_run=False,
                             overwrite=False,
                             **kwargs):
    existing_path = Path(preferences['calibration_dir']) / f'{device_name}.json'
    if existing_path.exists() and not overwrite:
        print(f'Calibration curve already exists for {device_name}. Use --overwrite to overwrite it.')
        return
    if not dry_run:
        print('Writing measured values to file')
        data_dict = dict(reference_values=reference_values, 
                         measured_values=measured_values)
        json.dump(data_dict, open(Path(preferences['calibration_dir']) / f'{device_name}.json', 'w'))

    print(f'Reference values: {reference_values}')
    print(f'Measured values: {measured_values}')
    plt.plot(reference_values, measured_values, 'o-', color='black', label='Measured values')
    plt.xlabel('Reference values')
    plt.ylabel('Measured values')

    #coefs = Polynomial.fit(reference_values, measured_values, polyorder).coef
    coefs = np.polyfit(reference_values, measured_values, polyorder)
    x = np.linspace(min(reference_values) - 1, max(reference_values) + 1, 100)
    y = np.poly1d(coefs)(x)

    plt.plot(x, y, color='red', label=f'Calibration curve, order={polyorder}')
    plt.legend()
    plt.title('Calibration curve - close this plot to continue')
    if not dry_run:
        plt.savefig(Path(preferences['calibration_dir']) / f'{device_name}.png')
    plt.show()

    if not dry_run:
        print('Writing calibration curve to file')
        data_dict['coefs'] = coefs.tolist()
        json.dump(data_dict, open(Path(preferences['calibration_dir']) / f'{device_name}.json', 'w'))


def _load_calibration_curve(device_name):
    data = json.load(open(Path(preferences['calibration_dir']) / f'{device_name}.json', 'r'))
    return data

def apply_calibration_curve(device_name, target_value):
    cal = _load_calibration_curve(device_name)
    roots = inverse_from_coefficients(cal['coefs'], target_value)
    print(roots)
    input_value = sanitize_roots(roots, cal['reference_values'])
    return input_value