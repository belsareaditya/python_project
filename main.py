import logging
import logging.handlers
import requests
import datetime
import random

# --- Logger Setup ---
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

# Optional: Also show logs in the console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# --- Quotes List ---
quotes = [
    "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. – William James",
    "Do something today that your future self will thank you for.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it."
]

# --- Generate a Daily Quote ---
today = datetime.date.today()
random.seed(today.toordinal())  # Ensures same quote for the day
quote_of_the_day = random.choice(quotes)

if __name__ == "__main__":
    try:
        # Fetch weather for Nagpur, India
        r = requests.get('https://weather.talkpython.fm/api/weather/?city=Nagpur&country=IN')
        if r.status_code == 200:
            data = r.json()
            temperature = data["forecast"]["temp"]

            logger.info(f"Weather in Nagpur: {temperature}°C")
            logger.info(f"Quote of the Day: \"{quote_of_the_day}\"")
        else:
            logger.error(f"Failed to fetch weather data. Status code: {r.status_code}")
    except Exception as e:
        logger.exception(f"An error occurred: {e}")
