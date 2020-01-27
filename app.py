import dash
import dash_html_components as html
import dash_core_components as dcc

import plotly.graph_objects as go
import numpy as np
import logging


import physics
from body import Body
from default_logger import get_logger
from units import CONST_M_EARTH, CONST_M_SUN, CONST_AU, CONST_DAY_SECS,CONST_EARTH_MEAN_ORBIT_VELOCITY

logger = get_logger(__name__)
logger.setLevel(logging.CRITICAL)

body1 = Body(id='a', mass=1*CONST_M_SUN,     position=[0,0,0],          v0=[0,0,0],     color='yellow' ,  logger=logger)
body2 = Body(id='b', mass=1*CONST_M_EARTH,   position=[1*CONST_AU,0,0], v0=[0,29780,0], color='blue',     logger=logger)
body3 = Body(id='c', mass=0.107*CONST_M_EARTH,   position=[1.524*CONST_AU,0,0], v0=[0,0.808*CONST_EARTH_MEAN_ORBIT_VELOCITY,0], color='red',     logger=logger)
body4 = Body(id='d', mass=317.83*CONST_M_EARTH,   position=[5.204*CONST_AU,0,0], v0=[0,0.439*CONST_EARTH_MEAN_ORBIT_VELOCITY,0], color='orange',     logger=logger)


bodies = [body1, body2, body3, body4]

dt = 86400
t0 = 0
tf = 3.154e+7 * 11.862
times = np.arange(t0, tf+1, dt)
# times = np.linspace(t0, tf, 1e4)

x_body1 = np.array([])
y_body1 = np.array([])

x_body2 = np.array([])
y_body2 = np.array([])

x_body3 = np.array([])
y_body3 = np.array([])

x_body4 = np.array([])
y_body4 = np.array([])

for idx,t in enumerate(times):
    x_body1 = np.append(x_body1, body1.position[0])
    y_body1 = np.append(y_body1, body1.position[1])
    
    x_body2 = np.append(x_body2, body2.position[0])
    y_body2 = np.append(y_body2, body2.position[1])
    
    x_body3 = np.append(x_body3, body3.position[0])
    y_body3 = np.append(y_body3, body3.position[1])
    
    x_body4 = np.append(x_body4, body4.position[0])
    y_body4 = np.append(y_body4, body4.position[1])

    relpos_success = physics.relative_positions(bodies, logger=logger)
    net_gravity_success = physics.net_gravity(bodies, logger=logger)
    calc_acceleration_success = physics.calc_acceleration(bodies, logger=logger)
    calc_velocity_success = physics.calc_velocity(bodies, dt, logger=logger)
    calv_position_success = physics.calc_position(bodies, dt, logger=logger)
    print(f"{(idx/len(times))*100}%", end='\r')



xm = np.min(x_body4) - np.min(x_body4) * 0.5
xM = np.max(x_body4) + np.max(x_body4) * 0.5
ym = np.min(y_body4) - np.min(y_body4) * 0.5
yM = np.max(y_body4) + np.max(y_body4) * 0.5



# downsampled values
xx_body2 = x_body2[::10]
yy_body2 = y_body2[::10]

xx_body1 = x_body1[::10]
yy_body1 = y_body1[::10]

xx_body3 = x_body3[::10]
yy_body3 = y_body3[::10]

xx_body4 = x_body4[::10]
yy_body4 = y_body4[::10]


N = len(xx_body2)
# Create figure


fig = go.Figure(
    data=[
          
          # Earth
          go.Scatter(x=x_body2, y=y_body2,
                     mode="lines",
                     line=dict(width=2, color="blue")),
          go.Scatter(x=x_body2, y=y_body2,
                     mode="lines",
                     line=dict(width=2, color="blue")),

          # Sun
          go.Scatter(x=x_body1, y=y_body1,
                     mode="lines",
                     line=dict(width=2, color="yellow")),
          go.Scatter(x=x_body1, y=y_body1,
                     mode="lines",
                     line=dict(width=2, color="yellow")),

        #   # Mars
          go.Scatter(x=x_body3, y=y_body3,
                     mode="lines",
                     line=dict(width=2, color="red")),
          go.Scatter(x=x_body3, y=y_body3,
                     mode="lines",
                     line=dict(width=2, color="red")),
                     
        #   # Jupiter
          go.Scatter(x=x_body4, y=y_body4,
                     mode="lines",
                     line=dict(width=2, color="orange")),
          go.Scatter(x=x_body4, y=y_body4,
                     mode="lines",
                     line=dict(width=2, color="orange")),
                     
                     
                    
                     ],
    layout=go.Layout(
        xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
        yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
        title_text="Kinematic Generation of a Planar Curve", hovermode="closest",
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])]),
    frames=[go.Frame(
        data=[
            # Earth
            go.Scatter(
                x=[xx_body2[k]],
                y=[yy_body2[k]],
                mode="markers",
                marker=dict(color="blue", size=10)
            ),

            # Sun
            go.Scatter(
                x=[xx_body1[k]],
                y=[yy_body1[k]],
                mode="lines+markers",
                marker=dict(color='yellow', size=50)
            ),
            
            # Mars
            go.Scatter(
                x=[xx_body3[k]],
                y=[yy_body3[k]],
                mode="lines+markers",
                marker=dict(color='red', size=8)
            ),

            # Jupiter
            go.Scatter(
                x=[xx_body4[k]],
                y=[yy_body4[k]],
                mode="lines+markers",
                marker=dict(color='orange', size=20)
            ),
        ]
    )

        for k in range(N)
    ]
)

fig.show()
