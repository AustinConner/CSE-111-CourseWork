import math

def main():
    cans = [
        # Name, Radius(centimeters), Height(centimeters), Cost(USD)
        ["#1 Picnic",	6.83, 10.16, 0.28],
        ["#1 Tall", 7.78, 11.91, 0.43],
        ["#2", 8.73, 11.59, 0.45],
        ["#2.5", 10.32, 11.91, 0.61],
        ["#3 Cylinder", 10.79, 17.78, 0.86],
        ["#5", 13.02, 14.29, 0.83],
        ["#6Z", 5.40, 8.89, 0.22],
        ["#8Z short", 6.83, 7.62, 0.26],
        ["#10", 15.72, 17.78, 1.53],
        ["#211", 6.83, 12.38, 0.34],
        ["#300", 7.62, 11.27, 0.38],
        ["#303", 8.10, 11.11, 0.42]
    ]

    computed_list = []

    for list in cans:
        # easy variables
        name = list[0]
        radius = list[1]
        height = list[2]
        cost = list[3]

        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        effeciency = compute_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, cost)

        # Add values to list
        list = [name, effeciency, cost_efficiency]
        computed_list.append(list)
        # print(f"{name} {effeciency:.2f} {cost_efficiency:.2f}")

    # Print the new list
    max_cost_eff = 0
    for i in computed_list:
        name = computed_list[0]
        effeciency = computed_list[1]
        cost_efficiency[2]

        if cost_efficiency < 0:
            max_cost_eff = cos

def compute_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    # print(volume)
    return volume

def compute_surface_area(radius, height):
    surface_area = (2 * math.pi * radius) * (radius + height)
    return surface_area
    

def compute_efficiency(volume, surface_area):
    efficiency = volume / surface_area
    return efficiency

def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()