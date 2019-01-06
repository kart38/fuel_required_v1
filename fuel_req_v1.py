#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:26:25 2018

@author: kart38
"""
import time_format

avg_lap_time = 0
avg_fuel_used = 0
race_duration = 0
extra_laps = 0
race_laps = 0
fuel_required = 0
race_type = ""
est_laps = True
fuel_tank_cap = 0
# Variables go above here


def user_inquiry():  # Function that asks the user for basic info
    global avg_lap_time, avg_fuel_used, race_duration, extra_laps, fuel_tank_cap
    avg_lap_time = float(input("What is your average lap time?\n"))
    avg_fuel_used = float(input("What is your fuel used per lap?\n"))
    fuel_tank_cap = int(input("How much fuel is allowed in full fuel tank?\n"))
    race_type_inquiry()


def is_pit_required():  # Basic function, decides if pitting will be required
    if fuel_required - fuel_tank_cap > 0:
        return True
    else:
        return False


def race_type_time():  # Function that asks questions about a 'Timed Race'
    global race_duration, extra_laps, race_type
    race_type = "Timed"
    race_duration = float(input("How long is the race in minutes?\n"))
    extra_laps = float(input("How many extra laps to add for a buffer?\n"))
    fuel_required_time()


def race_type_lap():  # Function that asks question about a 'Lap Race'
    global race_laps, extra_laps, race_type
    race_type = "Laps"
    race_laps = float(input("How many laps long is the race?\n"))
    extra_laps = float(input("How many extra laps to add for a fuel buffer?\n"))
    fuel_required_lap()


def race_type_inquiry():  # Function that asks if the race will be timed or by laps
    type_of_race = input("(T)imed race or (L)ap race?\n")
    if type_of_race.lower() == "t" or type_of_race.lower() == "timed":
        race_type_time()
    elif type_of_race.lower() == "l" or type_of_race.lower() == "lap" or type_of_race.lower() == "laps":
        race_type_lap()
    else:
        print("Enter only either a 'T' or 'L' please.")
        race_type_inquiry()


def fuel_required_time():  # Calculates the amount of fuel required for a timed race
    global fuel_required, race_laps
    race_length = race_duration * 60
    race_laps = race_length / avg_lap_time
    fuel_required = (race_laps + extra_laps) * avg_fuel_used


def fuel_required_lap():  # Calculates the amount of fuel required for a lap race
    global fuel_required, race_duration
    race_duration = round((race_laps * avg_lap_time) / 60, 3)
    fuel_required = (race_laps + extra_laps) * avg_fuel_used

    
def race_time(time_input):
  h, m = divmod(time_input, 60)
  s = ((m - int(m)) * 60)
  h = str(int(h))
  if int(time_input) >= 60:
    if int(m) < 10:
        m = (":0{0}".format(int(m)))
    else:
        m = (":{0}".format(int(m)))
    if s < 10:
        s = (":0{0}".format(round(s, 3)))
    else:
        s = (":{0}".format(round(s, 3)))
    return (h + m + s)
  else:
    if int(m) < 10:
        m = ("0{0}".format(int(m)))
    else:
        m = ("{0}".format(int(m)))
    if s < 10:
        s = (":0{0}".format(round(s, 3)))
    else:
        s = (":{0}".format(round(s, 3)))
    if s == ":00":
        return str(m) + " minutes"
    else:
        return (m + s)


def print_variables():  # Does what it says, prints all variables for 'debugging'
    print("\n=== VARIABLES ===")
    print(race_type)
    print(avg_lap_time)
    print(avg_fuel_used)
    print(race_duration)
    print(extra_laps)
    print(race_laps)
    print(fuel_required)
    print(fuel_tank_cap)
    if is_pit_required():
        print(fuel_required - fuel_tank_cap)
    
    
def print_results():  # The results that will print out at conclusion of questioning
    print("\n==== Race Information ====")
    print("Race Type:           {0}".format(race_type))
    print("Race Laps:           {0}".format(int(race_laps)))
    print("Race Duration:       {0}".format(time_format.format_race_time(race_duration)))
    sample_laps_time()
    print("\n==== Fuel Information ====")
    print("Laps of Fuel:        {0}".format(int(race_laps + extra_laps)))
    sample_laps_fuel()
    print("Fuel Required:       {0}".format(round(fuel_required, 3)))
    if is_pit_required():
        print("Fuel to Add:         {0}".format(round(fuel_required - fuel_tank_cap, 3)))
        print("Opening Stint Laps:  {0}".format(int(fuel_tank_cap / avg_fuel_used)))
        print("Closing Stint Laps:  {0}".format(int(race_laps + extra_laps) - int(fuel_tank_cap / avg_fuel_used)))
    
    
def sample_laps_time():  # Function that prints average lap time and whether it was estimated or how many laps were averaged
    if est_laps:
        print("Average Lap Time:    {0}".format(time_format.format_lap_time(avg_lap_time)))
        print("Sample Laps:         {0}".format("Time Estimated"))
    else:
        print("Average Lap Time:    {0}".format(time_format.format_lap_time(avg_lap_time)))
        print("Sample Laps:         {0}".format("No variable yet"))


def sample_laps_fuel():  # Function that prints average fuel used and whether it was estimated or how many laps were averaged
    if est_laps:
        print("Average Fuel Used:   {0}".format(avg_fuel_used))
        print("Sample Laps:         {0}".format("Fuel Estimated"))
    else:
        print("Average Fuel Used:   {0}".format(avg_fuel_used))
        print("Sample Laps:         {0}".format("No variable yet"))


def main():
    user_inquiry()
    # print_variables()
    print_results()

if __name__ == '__main__':    
    main()
