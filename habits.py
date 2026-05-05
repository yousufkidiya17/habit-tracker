"""Habit tracker"""
import json
from pathlib import Path

DATA = Path("habits.json")

def load():
    return json.loads(DATA.read_text()) if DATA.exists() else {}

def save(data):
    DATA.write_text(json.dumps(data, indent=2))
