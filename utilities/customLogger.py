import logging

class LogGen:
    def loggen(self):
        logging.basicConfig(filename="C:\Users\Rahul\PycharmProjects\Ecommerce\Logs",
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m%d%y %I:%M:%S %P'
                            )
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger




