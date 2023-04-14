class Car:
    """Creat a car object with collision detect mechanism."""

    # The co-ordinate system is followed in the following definitions.
    # even the speeds can be negative to indicate left / down / -z movememnt
    # All formulae are based on clasical physics.

    def __init__(self, make, model, year):
        """Initialise a car object with specified make , model and year."""
        self.make = make
        self.model = model
        self.year = year
        self.speed_x = 0
        self.speed_y = 0
        self.speed_z = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def accelearte_x(self, speed_increment):
        """Increase the speed of the car by the given amount."""
        self.speed_x += speed_increment

    def accelearte_y(self, speed_increment):
        """Increase the speed of the car by the given amount."""
        self.speed_y += speed_increment

    def accelearte_z(self, speed_increment):
        """Increase the speed of the car by the given amount."""
        self.speed_z += speed_increment

    def brake_x(self, speed_decrement):
        """Decrease the speed of the car by the given amount."""
        self.speed_x -= speed_decrement

    def brake_y(self, speed_decrement):
        """Decrease the speed of the car by the given amount."""
        self.speed_y -= speed_decrement

    def brake_z(self, speed_decrement):
        """Decrease the speed of the car by the given amount."""
        self.speed_z -= speed_decrement

    def move(self):
        """Update the co-ordinates of the car."""
        # Update the position according to the speed in each direction.
        self.x += self.speed_x
        self.y += self.speed_y
        self.z += self.speed_z

    def detect_collision(self, car2):
        """Detect collision with another car."""
        # Collision is defined as both the cars being at the same point
        if (self.x == car2.x and self.y == car2.y and self.z == car2.z):
            return True

        return False

    def time_to_collision(self, car2):
        """Calculate the time till a possible collision."""
        # analyse all the directions independently
        x_true = False
        y_true = False
        z_true = False

        time_x = 0
        time_y = 0
        time_z = 0

        # Along the x direction
        if self.speed_x == 0:
            # if the co-ordinates are not the same they'll never be the same
            if self.x != car2.x:
                return False
            x_true = True

        else:
            # Check if the rel vel is zero
            if abs(self.speed_x - car2.speed_x) == 0:
                if self.x != car2.x:
                    return False
                x_true = True
            else:
                time_x = abs(self.x - car2.x)/abs(self.speed_x - car2.speed_x)

        # Along the y direction
        if self.speed_y == 0:
            # if the co-ordinates are not the same they'll never be the same
            if self.y != car2.y:
                return False
            y_true = True
        else:
            # Check if the rel vel is zero
            if abs(self.speed_y - car2.speed_y) == 0:
                if self.y != car2.y:
                    return False
                y_true = True
            else:
                time_y = abs(self.y - car2.y)/abs(self.speed_y - car2.speed_y)

        # Along the z direction
        if self.speed_z == 0:
            # if the co-ordinates are not the same they'll never be the same
            if self.z != car2.z:
                return False
            z_true = True
        else:
            # Check if the rel vel is zero
            if abs(self.speed_z - car2.speed_z) == 0:
                if self.z != car2.z:
                    return False
                z_true = True
            else:
                time_z = abs(self.z - car2.z)/abs(self.speed_z - car2.speed_z)

        if time_x == time_y == time_z:
            return time_x
        if time_x == time_y and z_true:
            return time_x
        if time_z == time_y and x_true:
            return time_z
        if time_x == time_z and y_true:
            return time_x
        if x_true and y_true:
            return time_z
        if y_true and z_true:
            return time_x
        if z_true and x_true:
            return time_z

        return False


if __name__ == "__main__":
    car1 = Car("Honda", "Admire", 2012)

    car2 = Car("Ford", "Aspire", 2011)
    car2.x = 100

    car1.accelearte_x(10)
    car2.accelearte_x(-10)

    car1.move()
    car2.move()
    print(car1.detect_collision(car2))
    print(car1.time_to_collision(car2))

    car1.move()
    car2.move()
    print(car1.detect_collision(car2))
    print(car1.time_to_collision(car2))

    car1.move()
    car2.move()
    print(car1.detect_collision(car2))
    print(car1.time_to_collision(car2))

    car1.move()
    car2.move()
    print(car1.detect_collision(car2))
    print(car1.time_to_collision(car2))

    car1.move()
    car2.move()
    print(car1.detect_collision(car2))
    print(car1.time_to_collision(car2))
