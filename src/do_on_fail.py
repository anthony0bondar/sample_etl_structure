"""
Do when ETL failed
"""
from config import ETL_CONFIG
from config import TABLES_TO_LOAD
from utils import LOGGER


def do_on_fail() -> None:
    """
    Do on failure script
    :return:
    """
    LOGGER.info('start do-on-fail')
    # cleaning staging area, etc
