"""
ETL Module for specific needs
"""
from config import ETL_CONFIG
from config import TABLES_TO_LOAD
from utils import LOGGER


def second_etl_pipeline() -> None:
    """
    Specific ETL script #2
    :return:
    """
    LOGGER.info('starting specific script #2')
