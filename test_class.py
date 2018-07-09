from run_simulation import main
from simulators.rover_domain_simulator import RoverDomain


class TestClass(RoverDomain):
    def test_config(self):
        main("config.yml")

    def test_up(self):
        prev_loc = self.agents[0]['loc']
        dy = prev_loc[1] + 1
        actions = {'agents': {'loc': [prev_loc[0], dy]}}
        RoverDomain.apply_actions(self, actions)
        assert self.agents[0]['loc'][1] > prev_loc[1]

