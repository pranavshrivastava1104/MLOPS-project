import logging 
import os
from time import strftime 

from from_root import from_root
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_dir='logs'

logs_path=os.path.join(from_root,log_dir,LOG_FILE)

os.makedirs(log_dir)

logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

