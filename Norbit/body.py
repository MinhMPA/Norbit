class Body():
    """
    Class of bodies or particles in Simulations.
    
    Parameters
    ----------
    mass : float
            Mass of the body. If units=True, an Astropy Quantity (M_sun).
    position : (3,)
            Initial position. If units=True, an Astropy Quantity (AU).
    velocity : (3,)
            Initial velocity. If units=True, an Astropy Quantity (AU/day) 
    name : string
            Name
    units : bool, optional
            Whether quantities should be pure numbers (unitless) or Astropy Quantities (with astrophyiscal units associated) 
    """

    def __init__(self,mass,position,velocity,name=None, units=False):
        self.name= name
        self.units = units
        if self.units:
            self.mass = mass.astrophys
            self.position = position.astrophys.value
            self.velocity = velocity.astrophys.value
        else:
            self.mass = mass
            self.position = position
            self.velocity = velocity

    def return_name(self):
        return self.name
