import json
import os
import random
import requests
from datetime import datetime

USED_FILE = "used_quotes.json"
LOG_FILE = "status.log"
CITY = "Nagpur"
COUNTRY = "IN"
WEATHER_API = f"https://weather.talkpython.fm/api/weather/?city={CITY}&country={COUNTRY}"

QUOTES = [
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

def load_used():
    if not os.path.exists(USED_FILE):
        return []
    try:
        with open(USED_FILE, "r", encoding="utf8") as f:
            return json.load(f)
    except Exception:
        return []

def save_used(used):
    with open(USED_FILE, "w", encoding="utf8") as f:
        json.dump(used, f, ensure_ascii=False, indent=2)

def pick_quote():
    used = load_used()
    unused = [q for q in QUOTES if q not in used]
    if not unused:
        used = []        # reset when all used
        unused = QUOTES.copy()
    choice = random.choice(unused)
    used.append(choice)
    save_used(used)
    return choice

def fetch_weather():
    try:
        r = requests.get(WEATHER_API, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data.get("forecast", {}).get("temp", "N/A")
    except Exception:
        return "N/A"

def write_log(text):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{ts} - {text}\n"
    with open(LOG_FILE, "a", encoding="utf8") as f:
        f.write(line)
    print(text)

if __name__ == "__main__":
    quote = pick_quote()
    temp = fetch_weather()
    write_log(f"Weather in {CITY}: {temp}°C")
    write_log(f"Quote of the run: \"{quote}\"")
