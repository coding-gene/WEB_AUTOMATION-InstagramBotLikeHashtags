from logic.instagram import Instagram
from logic.config import get_environment_variables
import logging
import time
import random

start_time = time.time()
logging.basicConfig(filename='logs.txt',
                    filemode='a',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.info('Početak izvršavanja zadatka.')
hashtags = 'datascience'  # ['datascience', 'dataengineering', 'pyspark', 'apachekafka']
# noinspection PyBroadException
try:
    envVar = get_environment_variables()
    instagram = Instagram(envVar.get('instagram'))

    instagram.open_browser()
    instagram.enter_credentials()
    instagram.find_hashtag(hashtag=hashtags)
    instagram.first_photo_by_hashtag()
    instagram.like_first_photo()
    instagram.continue_liking()
    instagram.close_last_photo()
except Exception:
    logging.exception('An error occurred during job performing:')
else:
    logging.info('Job ended.')
finally:
    # instagram.close_driver()
    logging.info(
        f'Job duration: {time.strftime("%H hours, %M minutes, %S seconds.", time.gmtime(time.time() - start_time))}\n')
