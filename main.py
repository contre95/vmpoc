# The dirties of our componentes. The one that inejct all the dependencies.

from time import sleep
from storage import FakeStorgae, SQLite
from app import VulnTracker
from feeders import Tenable, SSMAgent


def main():
    store = SQLite("./vulns.db")
    # store = FakeStorgae("Fake")
    tenable = Tenable()
    ssm = SSMAgent()
    feeders = (ssm, tenable)
    tracker = VulnTracker(store, feeders)

    # You will then pass the tracker to whatever external thing will trigger it, API, Scheduler, Topics, etc.. for the sake of this example, we are going to trigger every 5 seconds here.
    while True:
        tracker.track()
        sleep(5)


if __name__ == "__main__":
    main()
