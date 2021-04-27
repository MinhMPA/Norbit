import numpy as np

# mass
m_Sun = 1.00000597682 
m_Jupyter = 9.54786104043E-4
m_Saturn = 2.85583733151E-4
m_Uranus = 4.37273164546E-5
m_Neptune = 5.17759138449E-5
m_Pluto = 1./(1.3E8)
mass = np.array([m_Sun, m_Jupyter, m_Saturn, m_Uranus, m_Neptune, m_Pluto])

# initial position
q0_Sun = np.array([0.,0.,0.])
q0_Jupyter = np.array([-3.5023653, -3.8169847, -1.5507963])
q0_Saturn = np.array([9.0755314, -3.0458353, -1.6483708])
q0_Uranus = np.array([8.3101420, -16.2901086, -7.2521278])
q0_Neptune = np.array([11.4707666, -25.7294829, -10.8169456])
q0_Pluto = np.array([-15.5387357, -25.2225594, -3.1902382])
q0 = np.array([q0_Sun, q0_Jupyter, q0_Saturn, q0_Uranus, q0_Neptune, q0_Pluto])

# initial velocity
v0_Sun = np.array([0.,0.,0.])
v0_Jupyter = np.array([0.00565429, -0.00412490, -0.00190589])
v0_Saturn = np.array([0.00168318, 0.00483525, 0.00192462])
v0_Uranus = np.array([0.00354178, 0.00137102, 0.00055029])
v0_Neptune = np.array([0.00288930, 0.00114527, 0.00039677])
v0_Pluto = np.array([0.00276725, -0.00170702, -0.00136504])
v0 = np.array([v0_Sun, v0_Jupyter, v0_Saturn, v0_Uranus, v0_Neptune, v0_Pluto])
