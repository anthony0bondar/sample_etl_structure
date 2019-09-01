"""
The argument that is passed to `python3.7 run.py --env=ARGUMENT`
is parsed here and that how script defines which config to use,
because we may have several, one for each environment
"""
import argparse

import os
import yaml


parser = argparse.ArgumentParser()
parser.add_argument('--env', help='set environment variable')
args = parser.parse_args()

try:
    ENV = args.env.lower()
    # Add your new config_name to the IF's list below
    if ENV not in ('dev', 'prod'):
        raise Exception("Acceptable --env values are: dev, prod")
except AttributeError:
    raise AttributeError("Script should be runned with '--env=ENV_VARIABLE' argument")

config_dir = os.path.dirname(__file__)

if ENV == 'dev':
    application_config_file = os.path.join(config_dir, os.path.join('dev', 'config.yaml'))
    tables_to_load = os.path.join(config_dir, os.path.join('dev', 'tables_to_load.yaml'))
    with open(application_config_file, 'r', encoding='utf-8') as stream:
        ETL_CONFIG = yaml.safe_load(stream)
    with open(tables_to_load, 'r', encoding='utf-8') as stream:
        TABLES_TO_LOAD = yaml.safe_load(stream)
    project_abs_path = os.path.dirname(os.path.dirname(__file__))

elif ENV == 'prod':
    application_config_file = os.path.join(config_dir, os.path.join('prod', 'config.yaml'))
    tables_to_load = os.path.join(config_dir, os.path.join('prod', 'tables_to_load.yaml'))
    with open(application_config_file, 'r', encoding='utf-8') as stream:
        ETL_CONFIG = yaml.safe_load(stream)
    with open(tables_to_load, 'r', encoding='utf-8') as stream:
        TABLES_TO_LOAD = yaml.safe_load(stream)
    project_abs_path = os.path.dirname(os.path.dirname(__file__))

# elif ENV == 'your_new_config':
#     application_config_file = os.path.join(config_dir, os.path.join('your_new_config', 'config.yaml'))
#     tables_to_load = os.path.join(config_dir, os.path.join('your_new_config', 'tables_to_load.yaml'))
#     with open(application_config_file, 'r', encoding='utf-8') as stream:
#         ETL_CONFIG = yaml.safe_load(stream)
#     with open(tables_to_load, 'r', encoding='utf-8') as stream:
#         TABLES_TO_LOAD = yaml.safe_load(stream)
#     project_abs_path = os.path.dirname(os.path.dirname(__file__))

else:
    raise Exception("System Environment Variable 'ENV' has unacceptable value."
                    "Acceptable 'ENV' values are: 'dev', 'prod'")

__all__ = ['ETL_CONFIG', 'TABLES_TO_LOAD', 'project_abs_path']
