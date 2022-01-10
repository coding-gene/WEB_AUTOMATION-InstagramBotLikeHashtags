from logic.instagram import Instagram
from logic.config import get_environment_variables
import logging
import time

start_time = time.time()
# noinspection PyBroadException
try:
    pocetak = time.time()
    logging.basicConfig(filename='logs.txt',
                        filemode='a',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S')
    logging.info('Početak izvršavanja zadatka.')

    envVar = get_environment_variables()
    instagram = Instagram(envVar.get('instagram'))

    open_browser = instagram.open_browser()

except Exception:
    logging.exception('An error occurred during job performing:')
else:
    logging.info('Job ended.')
finally:
    logging.info(
        f'Job duration: {time.strftime("%H hours, %M minutes, %S seconds.", time.gmtime(time.time() - start_time))}\n')
