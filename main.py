class TrafficLight:
    def __init__(self, red, yellow, green, time_active, time):
        self.red = red
        self.yellow = yellow
        self.green = green
        self.time_active = time_active
        self.time = time


def read_traffic_light_data(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            values = line.split(',')
            light = TrafficLight(int(values[0]), int(values[1]), int(values[2]), int(values[3]), values[4])
            data.append(light)
    return data


def count_occurrences(data):
    red_count = 0
    yellow_count = 0
    green_count = 0
    for light in data:
        red_count += light.red
        yellow_count += light.yellow
        green_count += light.green
    return red_count, yellow_count, green_count


def calculate_total_time(data, color):
    total_time = 0
    for light in data:
        if getattr(light, color) == 1:
            total_time += light.time_active
    return total_time


def find_green_times(data):
    green_times = []
    for light in data:
        if light.green == 1:
            green_times.append(light.time)
    return green_times


def count_complete_cycles(data):
    cycle_count = 0
    state = None
    for light in data:
        current_state = (light.red, light.yellow, light.green)
        # new loop
        if state is None or (state == (0, 0, 1) and current_state == (1, 0, 0)):
            state = current_state
            continue
        # checking next loop step
        if state == (1, 0, 0) and current_state == (0, 1, 0):
            state = current_state
        elif state == (0, 1, 0) and current_state == (0, 0, 1):
            state = current_state
        elif state == (0, 0, 1) and current_state == (0, 1, 0):
            state = current_state
        elif state == (0, 1, 0) and current_state == (1, 0, 0):
            cycle_count += 1
            state = current_state

        else:
            state = None  # loop reset
    return cycle_count


def check_for_mistakes(data):
    mistake_count = 0
    for light in data:
        if (light.red + light.yellow + light.green) != 1:
            mistake_count += 1
    return mistake_count


# Main program starts here, converting .txt to OOP list
filename = "data.txt"
data = read_traffic_light_data(filename)

# 1.Find the number of red, yellow & green occurrences.
red_count, yellow_count, green_count = count_occurrences(data)
print("Red:", red_count)
print("Yellow:", yellow_count)
print("Green:", green_count)

# 2.Find how long each colour was active for.
red_time = calculate_total_time(data, "red")
yellow_time = calculate_total_time(data, "yellow")
green_time = calculate_total_time(data, "green")
print("Total time red:", red_time)
print("Total time yellow:", yellow_time)
print("Total time green:", green_time)

# 3.Find all times when Green was active (by time)
green_times = find_green_times(data)
print("Green times", green_times)

# 4.Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data
cycle_count = count_complete_cycles(data)
print("Cycle count:", cycle_count)

# 4.Find the number of complete cycles Red-Yellow-Green-Yellow-Red in the data
mistake_count = check_for_mistakes(data)
print("Mistake count:", mistake_count)
