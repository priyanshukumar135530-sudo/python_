# write a program to generate arithmetic exception and log the exception in system


import logging


logging.basicConfig(
    filename='error_log.txt',   
    level=logging.ERROR,        
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    a = 10
    b = 0
    result = a / b   

except Exception as e:
    print("An error occurred:", e)
    logging.error("Exception occurred", exc_info=True)