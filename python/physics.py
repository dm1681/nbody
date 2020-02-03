"""
This file will be used to define a lot of the physics to be modeled in the nbody simulations
"""
import logging
import numpy as np

from units import  CONST_G



def calc_position(bodies, dt, logger=None):
    if logger is None:
        logger = logging.getLogger(__name__)

    for body in bodies:
        body.position = body.position + body.velocity*dt

    return True


def calc_velocity(bodies, dt, logger=None):
    if logger is None:
        logger = logging.getLogger(__name__)
    
    for body in bodies:
        body.velocity = body.velocity + body.acceleration * dt

    return True

def calc_acceleration(bodies, logger=None):
    if logger is None:
        logger = logging.getLogger(__name__)

    for body in bodies:
        body.acceleration = body.net_gravity / body.mass
        logger.info(f"{body.name}'s acceleration = {body.acceleration}")

    return True


def net_gravity(bodies, logger=None):
    if logger is None:
        logger = logging.getLogger(__name__)

    for body in bodies:
        body.gravity_vectors = [force_gravity(body, other_body, body.rel_positions[idx]) for idx,other_body in enumerate(bodies)]
        body.gravity_vectors = np.nan_to_num(body.gravity_vectors)
        body.net_gravity = sum(body.gravity_vectors)
    return True




def force_gravity(body1, body2, rel_positions):
    """Takes two Body objects and returns the force of gravity between them
    
    Arguments:
        - body1 : Body object containing relevant properties
        - body2 : Body object containing relevant properties

    Returns
        - g : vector containing x, y, z components of gravity
    """
    r_mag = np.linalg.norm(rel_positions)
    F = (CONST_G * body1.mass * body2.mass / r_mag ** 3) * rel_positions
    
    return F


def relative_positions(bodies, logger=None):
    if logger is None:
        logger = logging.getLogger(__name__)

    for body in bodies:
        logger.info(f"Calculating relative positions for {body.name}")
        body.rel_positions = [other_body.position - body.position for other_body in bodies]

    return True

def orbital_speed(body):
    v = (CONST_G * body.mass * (2/body.position_mag - 1/body.semi_major_axis) ) ** (1/2) 
    return v


def system_net_force_check(bodies, logger=None):
    """
    This function must incorporate the uncerties defined in the constants used
    """

    if logger is None:
        logger = logging.getLogger(__name__)

    net_force = np.array([0.0, 0.0, 0.0])
    for body in bodies:
        logger.info(f'Adding {body.net_gravity}')
        net_force += body.net_gravity
    logger.info(f"System Net Force = {net_force}")
    if net_force[0] == 0 and net_force[1] == 0 and net_force[2] == 0:
        return True
    else:
        return False