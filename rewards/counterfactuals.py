from math import sqrt

def cf(self, agent, coupling = 1, consideration_radius = 10.0):
    """
    Implement counterfactual and return new state of the domain
    :param agent: agent considering the counterfactual
    :param coupling: the number of agents that must observe a POI before it is counted
    :param consideration_radius: the maximum distance an agent must search for POIs to place additional agents at
    """
    # Store copy of current domain state.
    old_domain =
    # Make copy of the domain to change
    new_domain =

    poi_considered = []

    # For every timestep of the domain, implement counterfactual
    for timestep in old_domain:
        poi_locations = poiSearch(agent, consideration_radius, timestep)
        num_pois = len(poi_locations)

        # Calculate D++ -1
        agent_diff =
        # Calculate D++ num_pois-1
        cf_diff = cf_D(poi_locations)

        if cf_diff <= agent_diff:
            #return agent_diff
            return old_domain
        else:
            for poi_loc in poi_locations and len(poi_considered) < coupling:
                # Calculate D++ 1
                cf_diff = cf_D(poi_loc)
                if cf_diff > agent_diff:
                    poi_considered.append(poi_loc)
            #return cf_D(poi_considered)

            return new_domain


def poiSearch(agent, consideration_radius, timestep):
    """
    Search for POIs within range of the agents and return list containing the location of each POI
    :param agent: agent searching for POIs around it
    :param consideration_radius: the maximum distance an agent must search for POIs to place additional agents at
    :param timestep: time at which to search for POIs
    """
    poi_locations = []

    # For every POI in this timestep, determine if it is within range of the agent
    for poi_id, poi_info in timestep['pois'].items():
        agent_loc =
        dist = distance(poi_info['loc'], agent_loc)
        # If the distance between the agent and poi is less than the consideration radius, store the pois
        if dist <= consideration_radius:
            poi_locations.append(poi_id)
    return poi_locations


# Function taken from g.py
@staticmethod
def distance(loc_1, loc_2):
    """ distance MOVE TO UTILITY CLASS
    L2 Norm of first two positions in loc_1 and loc_2. Unsafe.

    :returns: Euclidean distance between first two dimensions of input
    vectors.
    """
    square = lambda x: x ** 2
    return sqrt(square(loc_1[0] - loc_2[0]) + square(loc_1[1] - loc_2[1]))


def cf_D(poi_locations):
    """
    Calculate D++ with additional agents placed at specified POIs
    :param poi_locations: list of pois
    """