import numpy as np

__all__ = ['mod_Euler', 'leapfrog_kdk', 'leapfrog_dkd', 'RungeKutta_4']

def mod_Euler(q, v, m, f, step_size):
    """ modified Euler

    Parameters
    ----------
    q : (N,3) array_like
        Initial coordinates, main variables
    v : (N,3) array_like
        Initial velocities, auxiliary variables
    m : (N,) array_like
        Mass
    f : callable
        Force
    step_size : scalar, float
        Size of each time step

    Returns
    -------
    q, v : (N,3) array_like
        New coordinates and velocities after integration
    """

    q = q + step_size*v # whole-step drift
    v = v + step_size*f(q, m) # whole-step kick

    return q, v

def leapfrog_kdk(q, v, m, f, step_size):
    """ "kick-drift-kick" leapfrog

    Parameters
    ----------
    q : (N,3) array_like
        Initial coordinates, main variables
    v : (N,3) array_like
        Initial velocities, auxiliary variables
    m : (N,) array_like
        Mass
    f : callable
        Force
    step_size : scalar, float
        Size of each time step

    Returns
    -------
    q, v : (N,3) array_like
        New coordinates and velocities after integration
    """

    v = v + (0.5*step_size)*f(q, m) # half-step kick 
    q = q + step_size*v # whole-step drift
    v += (0.5*step_size)*f(q, m)

    return q, v

def leapfrog_dkd(q, v, m, f, step_size):
    """ "drift-kick-drift" leapfrog

    Parameters
    ----------
    q : (N,3) array_like
        Initial coordinates, main variables
    v : (N,3) array_like
        Initial velocities, auxiliary variables
    m : (N,) array_like
        Mass
    f : callable
        Force
    step_size : scalar, float
        Size of each time step

    Returns
    -------
    q, v : (N,3) array_like
        New coordinates and velocities after integration
    """

    q = q + (0.5*step_size)*v # half-step drift 
    v = v + step_size*f(q, m) # whole-step kick
    q += (0.5*step_size)*v # half-step drift 

    return q, v

def RungeKutta_4(q, v, m, f, step_size):
    """ Runge-Kutta (4th-order)

    Parameters
    ----------
    q : (N,3) array_like
        Initial coordinates, main variables
    v : (N,3) array_like
        Initial velocities, auxiliary variables
    m : (N,) array_like
        Mass
    f : callable
        Force
    step_size : scalar, float
        Size of each time step

    Returns
    -------
    q, v : (N,3) array_like
        New coordinates and velocities after integration
    """

    w = np.array([q,v])
    k1 = step_size*f(w, m)
    k2 = step_size*f(w+0.5*k1, m)
    k3 = step_size*f(w+0.5*k2, m)
    k4 = step_size*f(w+k3, m)
    w += (k1 + 2.*k2 + 2.*k3 + k4)/6.

    return w
