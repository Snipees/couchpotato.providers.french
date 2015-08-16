from .main import cpasbien
from couchpotato.core.logger import CPLog

log = CPLog(__name__)

def autoload():
    log.debug('load success')
    return cpasbien()

config = [{
    'name': 'cpasbien',
    'groups': [
        {
            'tab': 'searcher',
            'list': 'torrent_providers',
            'name': 'CPasBien',
            'description': 'See <a href="http://www.cpasbien.pw/">CPasBien</a>',
            'icon': 'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABHNCSVQICAgIfAhkiAAAAgZJREFUOI2lkj9oE2EYxn93l/Quf440gXg4lBoEMd2MDuLSkk0R6hCnuqjUoR0c7FDo4Ca0CDo7uRRBqEMDXSLUUqRDiZM1NMEI1VKTlDZpUppccvc5nJp/KooPfMPH+z3P+zzv+8F/Quq8XIVEEOY0kASIzpoLlBKUV+CuCblfCjyF/P3V1Qi6jrCs7k4eD/X1dS5NTy9tQaJD2MFDkA23W8UwQFGQRJcB0DS0cBg/DPY4a0OVZcHeHihKf1ifD6pVfGD/VmBAUeDwEGQZLAskCVQV6nVYW+M4lSLQo9stoKpQLoNtO2QhYHsbkkmOczm+AP5eBy/BfwRDn8GHJLkpFp3utRpkMpDLwckJvlCIM9Uqg6YZeAAj58E1CVlXCaaigcCjsWhU8Xq9UCo5lisVx4FhODFkGbdpMtlqXa4IsVUHYkLcVlbg3ddGo3AzErl2emLCGaCmwcAAuL4ntCxoNpFsG8O2odlkXojF17CgAK2PsJna2Xk/ViyOh0dHXWhaewaW1T6mSb5a5V6rtbAMU4D5c18FyCzu7i5fyWZvDMfjOh4PNBpd5A/5vLheq93ZhMc/eF0Lr0NhaX8/eS6djo/EYqfQdUekUuHNxsZR4uDg1id40f9J+qE/CwTeitlZIWZmxKtQqOSFi39D7IQy5/c/fxIMpoGhfyUDMAwXzsL4n958A9jfxsJ8X4WQAAAAAElFTkSuQmCC',
            'wizard': True,
            'options': [
                {
                    'name': 'enabled',
                    'type': 'enabler',
                    'default': False,
                },
                        {
                    'name': 'seed_ratio',
                    'label': 'Seed ratio',
                    'type': 'float',
                    'default': 1,
                    'description': 'Will not be (re)moved until this seed ratio is met.',
                },
                {
                    'name': 'seed_time',
                    'label': 'Seed time',
                    'type': 'int',
                    'default': 40,
                    'description': 'Will not be (re)moved until this seed time (in hours) is met.',
                },
                {
                    'name': 'extra_score',
                    'advanced': True,
                    'label': 'Extra Score',
                    'type': 'int',
                    'default': 10,
                    'description': 'Starting score for each release found via this provider.',
                }
            ],
        },
    ],
}]
