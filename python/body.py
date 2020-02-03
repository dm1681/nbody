"""
The purpose of this script is to create a class that defines all the methods/properties of an astrnomical body in an nbody system
"""

import logging
import numpy as np


class Body():
    def __init__(self, id, mass, position, v0=None, color=None, logger=None):
        """Starting definition of a body. 

        Arguments:
            - id : identifiable string specific to the body
            - mass : mass of the body [kg]
            - position : vector containing x,y,z coordinates [m]

        """
        self.id = id
        self.name = f"Body-{id.upper()}"
        self.color = color
        if logger is None:
            logger = logging.getLogger(self.name)
        self.logger = logger

        # some properties
        self.mass = mass
        self.position = np.array(position)
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]

        self.velocity = np.array(v0)
        self.v_x = v0[0]
        self.v_y = v0[1]
        self.v_z = v0[2]

        self.position_mag = (self.x ** 2 + self.y**2 + self.z**2)**(1/2)


        self.rel_positions = None
        self.gravity_vectors = None
        self.net_gravity = None
        self.logger.info(f"{self.name} initiated.")

