"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        Alien.total_aliens_created += 1
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

    def hit(self):
        self.health -= 1
        return self.health

    def is_alive(self):
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        return self.x_coordinate, self.y_coordinate

    def collision_detection(self, other):
        pass

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(positions):
    return [Alien(x_coordinate,y_coordinate) for x_coordinate,y_coordinate in positions]

alien_start_positions = [(4,7),(-1,0)]
aliens = new_aliens_collection(alien_start_positions)

print(aliens)
for alien in aliens:
    print(alien.x_coordinate, alien.y_coordinate)
