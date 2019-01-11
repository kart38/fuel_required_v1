lap_info = {}
lap_times = []  # Probably doesn't need to be global
indv_avg_lap_time = 0
fuel_used = []
indv_avg_fuel_used = 0  # Probably doesn't need to be global

# lap_info [x] = {"lap_time": y, "fuel_used": z}

def add_lap():
  x = int(input("Lap number: "))
  y = float(input("Lap time: "))
  z = float(input("Fuel used: "))
  lap_info[x] = {"lap_time": y, "fuel_used": z}
  return lap_info


def add_lap_to_dict():
  quit = 0
  while quit != "q":
    add_lap()
    quit = input("\nPress 'q' to quit.\n")
    quit = quit.lower()


def show_laps():
  print("\n-------------------")
  for i in lap_info:
    print("Lap Number: {0}".format(i))
    print("Lap Time:   {0}".format(lap_info[i]["lap_time"]))
    print("Fuel Used:  {0}".format(lap_info[i]["fuel_used"]))
    print("---------")


def average_lap_times():
  global indv_avg_lap_time
  for i in lap_info:
    lap_times.append(lap_info[i]["lap_time"])
  indv_avg_lap_time = sum(lap_times) / len(lap_times)
  return indv_avg_lap_time


def average_fuel_used():
  global indv_avg_fuel_used
  for i in lap_info:
    fuel_used.append(lap_info[i]["fuel_used"])
  indv_avg_fuel_used = sum(fuel_used) / len(fuel_used)
  return indv_avg_fuel_used


def show_averages():
  print("Average lap time:  {0}".format(indv_avg_lap_time))
  print("Average fuel used: {0}".format(indv_avg_fuel_used))


def lap_count():
  return len(lap_info)
  

if __name__ == '__main__':
    add_lap_to_dict()
    show_laps()
    average_lap_times()
    average_fuel_used()
    show_averages()
