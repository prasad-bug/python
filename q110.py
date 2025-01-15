import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, 
                    format='%(levelname)s:%(message)s')

# Log messages
logging.debug("This is a debug message.")
logging.info("This is an info message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")

print("Messages logged to app.log")
