import logging
from datetime import datetime


logging.basicConfig(
    filename='logfile.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d'
)

current_date = datetime.now().strftime('%Y-%m-%d')
logging.info(f" дата: {current_date}")
