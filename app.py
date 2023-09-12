# This is our Application layer, which we can also consider as part of our domain. Here live our use cases.

from vuln_mgmt import Feeder, Storage, Vulnerability


class VulnTracker():

    def __init__(self, storage: Storage, feeders: tuple[Feeder, ...]):
        self.storage = storage
        self.feeders = feeders  # Dependency injection

    def track(self):
        vulns: list[Vulnerability] = []
        for feeder in self.feeders:
            feederVulns = feeder.getVulns()
            vulns.extend(feederVulns)
        self.storage.storeMultiple(vulns)
