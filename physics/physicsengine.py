import rebound
class PhysicsEngine:
    def __init__(self):
        self.sim = rebound.Simulation()
        
        self.sim.collision = "direct" #mode of collision
        self.sim.collision_resolve = "merge" #how collision is dealt with

        self.planets = [] # list of planets in the simulation

    def add_planet(self, planet, x=0, y=0, vx=0, vy=0):
        # adding planet to the simulation
        particle = self.sim.add(
            m=planet.mass,
            x=x, y=y,
            vx=vx, vy=vy,
            r=planet.radius
        )

        # linking planet to the particle in the simulation
        planet.rebound_particle = particle
        self.planets.append(planet)

    def step(self, dt):
        self.sim.integrate(self.sim.t + dt)

    def get_planet_positions(self):
        positions = {}
        for planet in self.planets:
            p = planet.rebound_particle
            positions[planet.name] = (p.x, p.y)
        return positions
    
    def get_planet_velocities(self):
        velocities = {}
        for planet in self.planets:
            p = planet.rebound_particle
            velocities[planet.name] = (p.vx, p.vy)
        return velocities
    
    def get_planet_masses(self):
        masses = {}
        for planet in self.planets:
            p = planet.rebound_particle
            masses[planet.name] = p.m
        return masses
    
    def __synch_planets(self):
        for planet in self.planets:
            if (not planet.exists) : 
                self.sim.remove(planet.rebound_particle)
    
