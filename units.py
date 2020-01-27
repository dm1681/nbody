"""
Here we define units and constants that are neefded in other functions

Everything is in SI Base Units


"""
#
# CONSTANTS
#
CONST_G                         = 6.67430e-11  # m^3 kg^-1 s^-2
CONST_M_EARTH                   = 5.9722e24    # kg
CONST_M_SUN                     = 1.9885e30    # kg
CONST_AU                        = 149597870700 # m
CONST_DAY_SECS                  = 86400        # s
CONST_EARTH_MEAN_ORBIT_VELOCITY = 29780 # m/s
#
# CONVERSIONS
#
def au2m(au):
    return au * 149597870700 

def m2au(m):
    return m/149597870700 

def earthMass2kg(earthMass):
    return earthMass * 5.9722e24

def kg2earthMass(kg):
    return kg / 5.9722e24