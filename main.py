"""
This script will do some of the physics in the other scripts

"""

import numpy as np
import matplotlib.pyplot as plt


from body import Body
import physics
from units import CONST_M_EARTH, CONST_M_SUN, CONST_AU, CONST_DAY_SECS


from default_logger import get_logger


def main():

    logger = get_logger(__name__)


    print("Earth + Sun")
    body1 = Body(id='a', mass=1,   position=[0,0,0], v0=[0,0,0],  color='yellow' ,  logger=logger)
    body2 = Body(id='b', mass=1,   position=[1,0,0], v0=[0,10,0], color='blue', logger=logger)
    # body3 = Body(id='c', mass=1*CONST_M_EARTH, position=[-1*CONST_AU, 0,          0], v0=[0,0,0],             color='blue',  logger=logger)

    bodies = [body1, body2]

    # calculate relative positions between all the bodies
    # relpos_success = physics.relative_positions(bodies, logger=logger)
    # net_gravity_success = physics.net_gravity(bodies, logger=logger)
    # calc_acceleration_success = physics.calc_acceleration(bodies, logger=logger)
    # net_force_success = system_net_force_check(bodies, logger=logger)

    dt = 86400
    t0 = 0
    tf = dt * 300
    times = np.arange(t0, tf+1, dt)

    fig,ax = plt.subplots(1,1)
    fig.set_size_inches(8,5)

    for t in times:
        relpos_success            = physics.relative_positions(bodies, logger=logger)
        net_gravity_success       = physics.net_gravity(bodies, logger=logger)
        calc_acceleration_success = physics.calc_acceleration(bodies, logger=logger)
        calc_velocity_success     = physics.calc_velocity(bodies, dt, logger=logger)
        calv_position_success     = physics.calc_position(bodies, dt, logger=logger)
    
        for body in bodies:
            ax.scatter(body.position[0], body.position[1], label=body.name, color=body.color)


    
    fig.savefig("./fig.png")








if __name__ == "__main__":
    main()
