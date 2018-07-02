from math import sqrt

# Assumes that given domain state is at a specified time step and specific agent id and location is given
def cf(domain_state, agent, coupling = 1, consideration_radius = 10.0):
    """
    Implement counterfactual and return new state of the domain
    :param domain_state: current state of the domain
    :param agent: agent considering counterfactual agents
    :param coupling: the number of agents that must observe POIs before it is counted
    :param consideration_radius: the maximum distance from an agent POIs must be to have a counterfactual agent added
    :returns: domain state with counterfactual implemented
    """
    # Copy of domain to be modified
    new_domain_state = domain_state

    poi_considered = []
    poi_locations = poi_search(domain_state, agent, consideration_radius)

    # Calculate D++ -1
    agent_diff =
    # Calculate D++ len(poi_locations)-1
    cf_diff = cf_d(domain_state, poi_locations)

    if cf_diff <= agent_diff:
        return domain_state
    else:
        # for each poi in range of the agent, place an additional agent and check for an increase in reward
        for poi_loc in poi_locations and len(poi_considered) < coupling - 1:
            # Calculate D++ 1
            cf_diff = cf_d(domain_state, poi_loc)
            if cf_diff > agent_diff:
                poi_considered.append(poi_loc)

    # place agents at considered pois in new domain
    for considered_poi in poi_considered:
        new_domain_state = add_agent(new_domain_state, considered_poi)
    return new_domain_state


def poi_search(domain_state, agent, consideration_radius):
    """
    Search for POIs within range of the agents and return list containing the location of each POI
    :param domain_state: current state of the domain
    :param agent: agent searching for POIs around it
    :param consideration_radius: the maximum distance an agent must search for POIs to place additional agents at
    :returns: list of poi locations
    """
    poi_locations = []
    agent_loc = agent

    # could do it as shown below or tap into agents sensors and search radius from there
    # For every POI, determine if it is within range of the agent
    for poi_loc in domain_state:
        dist = distance(agent_loc, poi_loc)

        # If the distance between the agent and poi is less than the consideration radius, store the POI location
        if dist <= consideration_radius:
            poi_locations.append(poi_loc)

    return poi_locations


# Function taken from g.py
def distance(loc_1, loc_2):
    """ distance MOVE TO UTILITY CLASS
    L2 Norm of first two positions in loc_1 and loc_2. Unsafe.

    :returns: Euclidean distance between first two dimensions of input
    vectors.
    """
    square = lambda x: x ** 2

    return sqrt(square(loc_1[0] - loc_2[0]) + square(loc_1[1] - loc_2[1]))


def cf_d(domain_state, poi_locations):
    """
    Calculate D++ with additional agents placed at specified POIs
    :param domain_state: domain to modify
    :param poi_locations: pois to place additional agents at
    :returns:
    """
    d_eval =

    return d_eval


def add_agent(domain_state, poi_location):
    """
    Modify agent domain to contain an additional agent at indicated location
    :param domain_state: domain state to modify
    :param poi_location: location to place additional agent
    :returns: modified domain state
    """

    return domain_state