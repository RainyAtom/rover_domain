from simulators.rover_domain_simulator import RoverDomain
from teams.rover_team import RoverTeam
from policies.policy import RandomPolicy
from policies.policy import CCEA
from policies.policy import Evo_MLP
from rewards.g import GlobalReward
import yaml
import sys
import time

def EvaluateTeam(team, domain, reward, steps, flag):
    states = []
    for step in range(steps):
        # Get States from Rover Doman
        joint_state = domain.get_jointstate()

        if flag is True:
            # Store trajectories
            for i in joint_state['agents']:
                states.append(str(i) + ', ' + str(joint_state['agents'][i]['loc'][0]) + ', ' + str(joint_state['agents'][i]['loc'][1]) + ', ' + str(joint_state['agents'][i]['theta']))

        # Get the actions from the team
        actions = team.get_jointaction(joint_state)

        # Pass actions to domain to update
        domain.apply_actions(actions)

        # Update the joint state
        joint_state = domain.get_jointstate()
        reward.record_history(joint_state)

    # Compute the Global Reward
    reward_G = reward.calculate_reward()

    return team, domain, reward_G, states

def main(config_f):
    """
    """
    # Unique identifier for each run
    id = str(time.clock())

    # Read and store parameters from configuration file.
    if config_f is None:
        config_f = "config.yml"
    with open(config_f, 'r') as f:
        config = yaml.load(f)
    print()
    print(config_f)
    with open(id + '_global_reward.yml', 'a') as file:
        file.write(config_f + "\n")

    # Initialize the rover domain.
    domain = RoverDomain(
        config["Seed"],
        config["Initial POI Locations"],
        config["Initial Agent Positions"],
        config["Number of Agents"],
        config["Number of POIs"],
        config["World Width"],
        config["World Length"])

    # Store POI states in file
    joint_state = domain.get_jointstate()
    with open(id +'_poi_states.yml', 'w') as file:
        for i in joint_state['pois']:
            file.write(str(i) + ',' + str(joint_state['pois'][i]['loc']) + "\n")

    agent_policies = {}
    for i in range(config["Number of Agents"]):
        agent_policies["agent_"+str(i)] = Evo_MLP(8, 2)
    team = RoverTeam(agent_policies)

    # Initialize the reward function
    global_reward = GlobalReward(
        config["Coupling"],
        config["Observation Radius"],
        config["Minimum Distance"])

    # Boolean flag used to indicate when to save trajectories
    flag = False

    for generation in range(config["Epochs"]):
        if generation > 9989:
            flag = True

        team, domain, fitness, trajectories = EvaluateTeam(team, domain, global_reward, config["Steps"], flag)

        # Store trajectories in a file
        with open(id + '_agent_states.yml', 'a') as file:
            for x in trajectories:
                file.write(x + "\n")
        # Store the global reward in a file
        with open(id + '_global_reward.yml', 'a') as file:
            file.write(str(fitness['agent_0']) + "\n")
        print(fitness['agent_0'])

        # CCEA Evaluation
        CCEA(team, fitness)


if __name__ == '__main__':
    # When ran through command line and no specific file is indicated, use default configuration file
    if len(sys.argv) is 1:
        config_f = "config.yml"
    else:
        config_f = sys.argv[1]
    main(config_f)
