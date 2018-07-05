from simulators.rover_domain_simulator import RoverDomain

class TestClass(RoverDomain):
    def test_up(self):
        prev_loc = self.agents[0]['loc']
        dy = prev_loc[]
        actions = {'agents':[ , ]}
        RoverDomain.apply_actions(self, actions)
        assert  ['loc'][1] >



