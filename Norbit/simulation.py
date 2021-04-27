import sys
import time
from tqdm.auto import tqdm
import numpy as np
from .integrators import *

class OrbitSimulation():
    """
    Initialize a simulation of orbits of celestial bodies, each defined by Body(). 

    Parameters
    ----------
    bodies : list
                List of bodies defined by Body()
    units : bool
            Whether quantities are unitless or Astropy Quantities in astrophysical units
    """

    def __init__(self,bodies,units=False):  
        self.units = units
        self.bodies = bodies
        self.N_bodies = len(self.bodies)
        self.N_dim = 6.0 
        self.m_bodies = np.array([body.mass for body in self.bodies])
        self.q_bodies = np.array([body.position for body in self.bodies])
        self.q_history = [self.q_bodies]
        self.v_bodies = np.array([body.velocity for body in self.bodies])
        self.v_history = [self.v_bodies]
        self.name_bodies = [body.return_name() for body in self.bodies]

    def specify_Hamiltonian(self,Hamiltonian_eqs):
        """
        Method that specifies the Hamiltonian equation of motion for the N-body system.
        For gravitational-only N-body simulations, this method is force evaluation.

        Parameters
        ----------
        Hamiltonian_eqs : callable
                        Hamiltonian equations of motion
        """
        self.Hamiltonian_eqs = Hamiltonian_eqs

    def run(self,T,epsilon,integrator=leapfrog_kdk):
        """
        Method which runs the simulation on a given set of bodies.

        Parameters
        ----------
        T : float
            Total time to evolve the system. Unitless quantity if units=False.
        epsilon : float
                  Size of timestep (should always be in the same unit with T). Unitless quantity if units=False.
        integrator : callable, optional
                     The integrator scheme. Default to the "kick-drift-kick" leapfrog.
                        
        Returns
        ----------
            None, but leaves two attributes that can be accessed via
            'simulation.q_history' and 'simulation.v_history' which contain all the history of positions and velocities, respectively.
        """
        if not hasattr(self,'Hamiltonian_eqs'):
                raise AttributeError('You might want to specify Hamiltonian equations of motion.')
        if self.units:
            T = T.astrophysics.value
            epsilon = epsilon.astrophysics.value

        N_steps = np.uint(T/epsilon)
        for step in tqdm(range(N_steps), total=N_steps):
            self.q_bodies, self.v_bodies = integrator(self.q_bodies, self.v_bodies, self.m_bodies, self.Hamiltonian_eqs, epsilon)
            self.q_history.append(self.q_bodies)
            self.v_history.append(self.v_bodies)
        self.q_history = np.array(self.q_history)
        self.v_history = np.array(self.v_history)
