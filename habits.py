"""Habit tracker"""
import json
import sys
from pathlib import Path
from datetime import date

DATA = Path("habits.json")

def load():
    return json.loads(DATA.read_text()) if DATA.exists() else {}

def save(data):
    DATA.write_text(json.dumps(data, indent=2))

def add(name):
    data = load()
    data.setdefault(name, [])
    save(data)
    print(f"habit added: {name}")

def check(name):
    data = load()
    days = data.setdefault(name, [])
    today = date.today().isoformat()
    if today not in days:
        days.append(today)
        save(data)
    print(f"checked {name} today")

def streak(name):
    data = load()
    days = data.get(name, [])
    n = 0
    for d in sorted(days, reverse=True):
        if d == date.today().isoformat():
            n += 1
        else:
            break
    print(f"{name} streak: {n}")

if __name__ == "__main__":
    cmd, name = sys.argv[1], sys.argv[2]
    {"add": add, "check": check, "streak": streak}[cmd](name)
