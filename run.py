"""
Starting point for BI/ETL processing.
To start ETL this file has to be executed with argument "--env".
Acceptable "--env" values are: dev, prod ...

Example:
    $ python3.7 run.py --env=dev
"""
import traceback
from datetime import datetime

from config import ENV
from utils import LOGGER

from src.first_etl_pipeline import first_etl_pipeline
from src.second_etl_pipeline import second_etl_pipeline
from src.do_on_fail import do_on_fail


def run() -> None:
    """
    Starting point of ETL
    Here we execute ETL steps one-by-one
    :return:
    """
    LOGGER.info('starting etl')
    LOGGER.info('step 1. specific script #1')
    first_etl_pipeline()
    LOGGER.info('step 2. specific script #2')
    second_etl_pipeline()
    LOGGER.info('etl completed')


if __name__ == '__main__':
    try:
        run()
    except Exception as etl_exception:
        # if any exception occurred during ETL - write error to file
        # or send notification if possible (for that create special function in /utils)
        with open(f"{ENV}_error_{datetime.now():%Y%m%d-%H%M}.log", "w") as f:
            f.write(str(etl_exception))
            f.write(traceback.format_exc())
        LOGGER.info("doing something on ETL fail")
        do_on_fail()
        LOGGER.error("etl completed with errors")
        raise etl_exception
