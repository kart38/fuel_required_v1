#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:26:25 2018

@author: kart38
"""
import time_format
import individual_laps

# TODO Use script for some races and see if it is working as intended

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


def enter_laps():
    global est_laps

    print("Enter individual laps and fuel or estimated?")
    ans = int(input("1. Individual laps\n" +
        "2. Estimated laps\n" +
        "Choose 1 or 2: "))
    est_laps = ans == 2


def user_inquiry():
    global avg_fuel_used, avg_lap_time
    enter_laps()
    if est_laps:
        est_laps_inquiry()
    else:
        indv_laps()
    global fuel_tank_cap
    fuel_tank_cap = int(input("How much fuel is allowed in full fuel tank?\n"))

    # Runs function to get info on type of race being run
    race_type_inquiry()


def indv_laps():
    global avg_fuel_used, avg_lap_time
    individual_laps.add_lap_to_dict()
    avg_lap_time = individual_laps.average_lap_times()
    avg_fuel_used = individual_laps.average_fuel_used()


def est_laps_inquiry():  # Gets basic info from user then moves script to next function
    global avg_lap_time, avg_fuel_used
    
    avg_lap_time = float(input("What is your average lap time?\n"))
    avg_fuel_used = float(input("What is your fuel used per lap?\n"))


def race_type_inquiry():  # Asks user which type of race this will be
    type_of_race = input("(T)imed race or (L)ap race?\n")

    #  Runs race_type_time because user chose 'timed'
    if type_of_race.lower() == "t" or type_of_race.lower() == "timed":
        race_type_time()

    # Runs race_type_lap because user chose 'lap'
    elif type_of_race.lower() == "l" or type_of_race.lower() == "lap" or type_of_race.lower() == "laps":
        race_type_lap()

    # Reminds user to use only 't' or 'l' to choose a race type
    else:
        print("Enter only either a 'T' or 'L' please.")
        race_type_inquiry()


def race_type_time():  # Contains questions about the time limited race, runs function
    global race_duration, extra_laps, race_type, est_laps

    race_type = "Timed"
    race_duration = float(input("How long is the race in minutes?\n"))
    extra_laps = float(input("How many extra laps to add for a buffer?\n"))

    # Runs function to figure fuel for time limited race
    fuel_required_time()


def race_type_lap():  # Contains questions about the lap limited race, runs function
    global race_laps, extra_laps, race_type

    race_type = "Laps"
    race_laps = float(input("How many laps long is the race?\n"))
    extra_laps = float(input("How many extra laps to add for a fuel buffer?\n"))

    # Runs function to figure required fuel for race
    fuel_required_lap()


def fuel_required_time(): # Fuel calculation for timed races
    global fuel_required, race_laps, avg_lap_time

    # Converts race_duration to seconds to make working with lap_time easier
    race_length = race_duration * 60

    # Calculates race laps based on average lap time
    race_laps = race_length / avg_lap_time

    # Calculates the fuel required for the race plus extra laps
    fuel_required = (race_laps + extra_laps) * avg_fuel_used


def fuel_required_lap():  # Fuel calculation for lap limited races
    global fuel_required, race_duration

    # Number of minutes it will take to run the race
    race_duration = round((race_laps * avg_lap_time) / 60, 3)
    
    # Calculates the amount of fuel required to run the race + the extra laps
    fuel_required = (race_laps + extra_laps) * avg_fuel_used


def is_pit_required():  # Function to decide if a pit stop is required
    if fuel_required - fuel_tank_cap > 0:
        return True
    else:
        return False


def print_variables():  # Prints the variables just for 'debugging'
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
    
    
def print_results():  # Shows the calculated data as well as certain entered data
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
    
    
def sample_laps_time():  # prints certain text depending on whether fuel was entered or estimated
    if est_laps:
        print("Average Lap Time:    {0}".format(time_format.format_lap_time(avg_lap_time)))
        print("Sample Laps:         {0}".format("Time Estimated"))
    else:
        print("Average Lap Time:    {0}".format(time_format.format_lap_time(avg_lap_time)))
        print("Sample Laps:         {0} Laps".format(individual_laps.lap_count()))


def sample_laps_fuel():  # prints certain text depending on whether laps were entered or estimated
    if est_laps:
        print("Average Fuel Used:   {0}".format(avg_fuel_used))
        print("Sample Laps:         {0}".format("Fuel Estimated"))
    else:
        print("Average Fuel Used:   {0}".format(round(avg_fuel_used, 3)))
        print("Sample Laps:         {0} Laps".format(individual_laps.lap_count()))


def main():
    user_inquiry()
    # print_variables()
    print_results()

if __name__ == '__main__':    
    main()
