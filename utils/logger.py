import os
import logging
from config import ENV
from config import ETL_CONFIG
from config import project_abs_path

logging.basicConfig(filename=os.path.join(project_abs_path, ENV+'_log.log'), level=logging.DEBUG, format='%(levelname)-1s [%(asctime)s]  %(message)s')
LOGGER = logging.getLogger("ETL")
level = logging.getLevelName(ETL_CONFIG['logging_level'])
LOGGER.setLevel(level)

__all__ = ['LOGGER']
