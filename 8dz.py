import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="sims_logs.log",
    filemode="w",
    format="We have next logging message:%(asctime)s:%(levelname)s - %(message)s"
)


logging.debug("Debug Info")
logging.info("Character woke up")
logging.info("Character has good mood today")
logging.info("Character go for a walk")
try:
    logging.info("Character find the secret object!")
    result = 1 / 0
except Exception as e:
    logging.error(f"Game Error: {e}")

logging.warning("Warning character energy is low!!!")
logging.error("Error message")
logging.critical("Critical message")

def divide(x,y):
    try:
        result = x/y
        logging.info(f"Division result {result}")
        return result
    except ZeroDivisionError as e:
        logging.error(f"Division error{e}")

