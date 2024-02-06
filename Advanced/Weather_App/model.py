from dataclasses import dataclass
from datetime import datetime

@dataclass
class Weather:
    date: datetime
    details: dict
    temperature: str
    weather: list[dict]
    description: str

    def __str__(self):
        return f'{self.date:%H:%M} - {self.temperature}C - {self.description}'
