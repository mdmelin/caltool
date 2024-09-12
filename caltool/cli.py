import argparse
from .utils import *
from .calibrate import create_calibration_curve

def main(command_line=None):
    parser = argparse.ArgumentParser('caltool')
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Print debug info'
    )
    subparsers = parser.add_subparsers(dest='command')

    # The calibration subparser
    calibrate = subparsers.add_parser('calibrate', help='Run calibration')
    calibrate.add_argument(
        '--dry-run',
        help='do not write the results to calibration file',
        action='store_true',
    )
    calibrate.add_argument('device_name', help='The name of the device to calibrate')
    calibrate.add_argument('--COM', help='The com port number of the device') # TODO: implement this functionality eventually
    calibrate.add_argument('--overwrite', help='Overwrite existing calibration curve', action='store_true')
    calibrate.add_argument('--reference_values', 
                           help='Input values for a calibration curve',
                           nargs='+',
                           type=float)
    calibrate.add_argument('--measured_values', 
                           help='Measured output values for a calibration curve',
                           nargs='+',
                           type=float)
    calibrate.add_argument('--polyorder',
                           help='The order of the polynomial to fit to the calibration curve (by default, linear).',
                           type=int,
                           default=1)

    # The show_calibration subparser
    show_calibration = subparsers.add_parser('show_calibration', help='Show calibration curve for a device')

    args = parser.parse_args(command_line)

    if args.debug:
        print("debug: " + str(args))
    if args.command == 'calibrate':
        if args.reference_values is None or args.measured_values is None:
            print('You must provide reference_values and measured_values for now. A future release will guide you through the calibration.')
            return
        else:
            create_calibration_curve(**vars(args))   

    if __name__ == '__main__':
        main()