# This is part of our Interface adapter layers. And here we only have feeders which are Gateways to external applications

from vuln_mgmt import Feeder, Service, Vulnerability


class Tenable(Feeder):
    #
    # def __init__(self) -> None:
    #     self.name = "Tenable"

    def getVulns(self) -> list[Vulnerability]:
        print(f'Getting all vulns from {self.name()}')
        v1 = Vulnerability("LOW", Service("SIEM", "Infrasec"), self.name())
        v2 = Vulnerability("HIGH", Service(
            "Rubidium", "Payments"), self.name())
        v3 = Vulnerability("CRITICAL", Service("Teleport", "PLE"), self.name())
        return [v1, v2, v3]

    def getVulnsByDate(self, date: str):
        print(f'Getting vulns from {self.name()} for date {date}')

    def name(self):
        return "Tenable"


class SSMAgent(Feeder):
    #
    # def __init__(self) -> None:
    #     self.name = "SSMAgent"

    def getVulns(self) -> list[Vulnerability]:
        print(f'Getting all vulns from {self.name()}')
        v1 = Vulnerability("LOW", Service("SIEM", "Infrasec"), self.name())
        v2 = Vulnerability("HIGH", Service(
            "Rubidium", "Payments"), self.name())
        v3 = Vulnerability("CRITICAL", Service("Teleport", "PLE"), self.name())
        return [v1, v2, v3]

    def getVulnsByDate(self, date: str):
        print(f'Getting vulns from {self.name()} for date {date}')

    def name(self):
        return "SSM Agent"
