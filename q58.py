import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set the minimum log level to INFO
    filename='application.log',  # Log messages will be saved to this file
    filemode='a',  # Append mode: new logs will be added to the file
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

def divide_numbers(a, b):
    """
    Divides two numbers and logs the process.
    """
    try:
        logging.info("Attempting to divide %s by %s", a, b)
        result = a / b
        logging.info("Division successful: %s / %s = %s", a, b, result)
        return result
    except ZeroDivisionError as e:
        logging.error("Error occurred: Division by zero")
        return None
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
        return None

# Main script logic
if __name__ == "__main__":
    # Test cases for logging
    divide_numbers(10, 2)  # Logs an INFO message
    divide_numbers(5, 0)   # Logs an ERROR message
    divide_numbers(15, 3)  # Logs an INFO message

    # Additional log messages
    logging.info("Script execution completed successfully.")
