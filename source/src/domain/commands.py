from dataclasses import dataclass
from datetime import date
from abc import ABC


class Command(ABC):
    pass


@dataclass
class SendTemperatureData(Command):
    datetime: date
    person_id: str
    temperature: float


@dataclass
class SendHumidityData(Command):
    datetime: date
    person_id: str
    humidity: float


@dataclass
class GetActiveThreadsNumber(Command):
    pass
