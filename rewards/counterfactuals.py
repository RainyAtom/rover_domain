from math import sqrt

def cf(domain_state, agent, coupling = 1, consideration_radius = 10.0):
    """
    Implement counterfactual and return new state of the domain
    :param domain_state: current state of the domain
    :param agent: agent considering counterfactual agents
    :param coupling: the number of agents that must observe different POIs for max reward
    :param consideration_radius: the maximum distance from an agent POIs must be to have a counterfactual agent added
    :returns: domain state with counterfactual implemented
    """
    # Domain to implement counterfactual
    new_domain_state = domain_state
    # list of POIs in range of agent
    considered_poi = []

    # For every POI in the domain, determine if it is within range of the agent
    for poi_id, poi_info in domain_state['pois'].items():
        dist = distance(agent['loc'], poi_info['loc'])
        # If the distance between the agent and POI is within the consideration radius, store the POI
        if dist <= consideration_radius:
            considered_poi.append(poi_info)

    # list of POIs that with an additional agent increase reward
    cf_poi = []
    # Calculate D++ -1
    agent_diff =
    # Calculate D++ with additional agents placed at each of the POIs in range of the agent
    cf_diff =

    # Compare D++ evaluations to see if counterfactual agents improve reward
    if cf_diff <= agent_diff:
        return domain_state
    else:
        # for each POI in range of the agent, place an additional agent and check for reward improvement
        for poi_info in considered_poi and len(cf_poi) < coupling - 1:
            # Calculate D++ with additional agent placed at POI considered
            cf_diff =
            if cf_diff > agent_diff:
                cf_poi.append(poi_info)

    # create a new agent at each POI that improved reward
    for poi in cf_poi:
        new_domain_state['agents'].append({'loc': poi['loc'], 'theta': 0})

    return new_domain_state

# Function taken from g.py
def distance(loc_1, loc_2):
    """ distance MOVE TO UTILITY CLASS
    L2 Norm of first two positions in loc_1 and loc_2. Unsafe.
    :returns: Euclidean distance between first two dimensions of input
    vectors.
    """
    square = lambda x: x ** 2
    return sqrt(square(loc_1[0] - loc_2[0]) + square(loc_1[1] - loc_2[1]))