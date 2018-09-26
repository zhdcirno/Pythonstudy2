import logging
LOG_FORMAT = "%(asctime)s=====%(levelname)s++++++%(message)s"
logging.basicConfig(filename="myx.log", level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("This is a debug log")
logging.info("this is a info log")
logging.warning("this is a warning log")
logging.error("this is a error log")
logging.critical("this is a critical log")