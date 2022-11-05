import logging

logging.basicConfig(level=logging.INFO)

api_logger = logging.getLogger('api')

api_handler = logging.FileHandler('logs/api.log')

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
api_handler.setFormatter(formatter)

api_logger.addHandler(api_handler)
