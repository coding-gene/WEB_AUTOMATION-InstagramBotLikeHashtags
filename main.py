from logic.instagram import Instagram
from logic.config import get_environment_variables
import logging
import time

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
    logging.exception('Dogodila se greška sljedećeg sadržaja:')
else:
    logging.info('Uspješno izvršen zadatak.')
finally:
    logging.info(f'Obrada trajala: {time.strftime("%H sati, %M minuta i %S sekundi.", time.gmtime(time.time() - pocetak))}\n')