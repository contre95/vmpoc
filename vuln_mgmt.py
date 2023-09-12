# We call this the domain layer, this layer should container all the bussiness logic. The core logic of what our application really does. The inner most layer that should not depend on any other layer

from abc import ABC, abstractmethod
from typing import TypeVar
import uuid



class Service():
    def __init__(self, name: str, owner: str) -> None:
        self.owner = owner
        self.name = name


class Vulnerability():
    def __init__(self, severity: str, service: Service, origin: str) -> None:
        self.id = uuid.uuid4()
        self.severity = severity
        self.service = service
        self.origin = origin


FeederType = TypeVar("FeederType", bound="Feeder")


class Feeder(ABC):
    @abstractmethod
    def getVulns(self) -> list[Vulnerability]:
        pass

    @abstractmethod
    def getVulnsByDate(self):
        pass


class Storage(ABC):
    @abstractmethod
    def store(self, vuln: Vulnerability):
        pass

    @abstractmethod
    def storeMultiple(self, vuln: list[Vulnerability]):
        pass
