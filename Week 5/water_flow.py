def water_column_height(tower_height, tank_height):
    """Calculates and returns the height of a column of water from a tower height and a tank wall height. 
    """
    water_column_height = tower_height + (3 * tank_height / 4)
    return water_column_height

def pressure_gain_from_water_height(height):
    """Calculating pressure caused by Earth's gravity
    """
    water_density = 998.2 # kilogram / meter^3
    gravity_acceleration = 9.80665 # meter / second^2

    pressure = (water_density * gravity_acceleration * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculates and returns the water pressure lost because of the friction between the water and the walls of a pipe that it flows through.
    """
    lost_pressure = (-friction_factor * pipe_length * 998.2 * fluid_velocity ** 2) / (2000 * pipe_diameter)
    return lost_pressure
