from physics.solarsystem import SolarSystem

class GameRules:
    def __init__(self, physics):
        self.physics = physics
        # self.planets = planets
        self.game_over = False
        self.win = False

    # Handling collisions manually
    def check_collisions(self):
        for i in range(2, len(self.physics.planets)):
                p1 = self.physics.planets[1] # player is always at index 1
                p2 = self.physics.planets[i]
                
                if p1.exists and p2.exists:
                    dx = p1.rebound_particle.x - p2.rebound_particle.x
                    dy = p1.rebound_particle.y - p2.rebound_particle.y

                    distance = (dx**2 + dy**2)**0.5     #d = sqrt(dx^2 + dy^2)

                    if distance < (p1.radius + p2.radius):
                        # Collision detected, remove the smaller planet
                        if p1.mass < p2.mass:
                            p1.exists = False
                            
                        else:
                            p2.exists = False

    def update(self, solsys):
        # checking if player still exists
        player_exists = any(p.is_player for p in self.physics.planets)
        # checking if sun still exists
        sun_exists = any(p.type == "sun" for p in self.physics.planets)

        if not player_exists:
            print("Earth got eaten! You lose!")
            self.game_over = True

        if not sun_exists:
            print("You win!")
            self.win = True
            self.game_over = True