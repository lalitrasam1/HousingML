import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
folderpath=os.path.join(os.getcwd(),'logs\\')
logs_path=os.path.join(os.getcwd(),'logs\\',LOG_FILE)
os.makedirs(folderpath,exist_ok=True)

print(logs_path)

LOG_FILE_PATH=os.path.join(logs_path)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

'''if __name__=="__main__":
    logging.info("Logging started")'''