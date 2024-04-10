import logging
import os

os.makedirs("Logs", exist_ok=True)
LOG_FILE=os.path.join("Logs", "logging_info.log")



logging.basicConfig(
    filename=LOG_FILE,
    format="[ %(asctime)s ] - %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


if __name__=="__main__":
    logging.warning("Half-way through logging")
    logging.info("This is Info")
    
if __name__ == "__main__":
    logging.info("Logging Has started")