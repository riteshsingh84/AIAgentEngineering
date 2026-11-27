from datetime import datetime

# Utility functions for date/time, dice rolling, and password generation

def get_current_time():
    """Return the current date and time."""

    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")