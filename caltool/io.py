from unittest.mock import DEFAULT
from .utils import * 
import json

# Default preferences
DEFAULT_CALIBRATION_DIR = Path().home() / 'caltool' / 'calibration_curves'
PREFS_FILE = Path().home() / 'caltool' / 'preferences.json'
DEFAULT_PREFS = dict(calibration_dir=str(DEFAULT_CALIBRATION_DIR),)

def __setup_prefs():
    if not DEFAULT_CALIBRATION_DIR.exists():
        print(f'Creating directory {DEFAULT_CALIBRATION_DIR}')
        DEFAULT_CALIBRATION_DIR.mkdir(parents=True)
    print(DEFAULT_PREFS)
    with open(PREFS_FILE,'w') as fd:
        json.dump(DEFAULT_PREFS,
                  fd,
                  sort_keys=True,
                  indent=4)
    print(f'Preferences file created at {PREFS_FILE}')

def __load_prefs():
    with open(PREFS_FILE,'r') as fd:
        prefs = json.load(fd)
    for k in DEFAULT_PREFS:
        if k not in prefs.keys():
            prefs[k] = DEFAULT_PREFS[k]
    return prefs

# Preferences

if not PREFS_FILE.exists():
    __setup_prefs()

preferences = __load_prefs()