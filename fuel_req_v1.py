#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:26:25 2018

@author: kart38
"""

avg_lap_time = 0
avg_fuel_used = 0
race_duration = 0
extra_laps = 0
race_laps = 0
fuel_required = 0
race_type = ""
est_laps = True
# Variable go above here


def user_inquiry():
    global avg_lap_time, avg_fuel_used, race_duration, extra_laps
    avg_lap_time = float(input("What is your average lap time?\n"))
    avg_fuel_used = float(input("What is your fuel used per lap?\n"))
    race_type_inquiry()


def race_type_time():
    global race_duration, extra_laps, race_type
    race_type = "Timed"
    race_duration = float(input("How long is the race in minutes?\n"))
    extra_laps = float(input("How many extra laps to add for a buffer?\n"))
    fuel_required_time()


def race_type_lap():
    global race_laps, extra_laps, race_type
    race_type = "Laps"
    race_laps = float(input("How many laps long is the race?\n"))
    extra_laps = float(input("How many extra laps to add for a fuel buffer?\n"))
    fuel_required_lap()


def race_type_inquiry():
    type_of_race = input("(T)imed race or (L)ap race?\n")
    if type_of_race.lower() == "t" or type_of_race.lower() == "timed":
        race_type_time()
    elif type_of_race.lower() == "l" or type_of_race.lower() == "lap" or type_of_race.lower() == "laps":
        race_type_lap()
    else:
        print("Enter only either a 'T' or 'L' please.")
        race_type_inquiry()


def fuel_required_time():
    global fuel_required, race_laps
    race_length = race_duration * 60
    race_laps = race_length / avg_lap_time
    fuel_required = (race_laps + extra_laps) * avg_fuel_used


def fuel_required_lap():
    global fuel_required, race_duration
    race_duration = round((race_laps * avg_lap_time) / 60, 3)
    fuel_required = (race_laps + extra_laps) * avg_fuel_used

    
def print_variables():
    print("\n=== VARIABLES ===")
    print(race_type)
    print(avg_lap_time)
    print(avg_fuel_used)
    print(race_duration)
    print(extra_laps)
    print(race_laps)
    print(fuel_required)
    
    
def print_results():
    print("\n==== Race Information ====")
    print("Race Type:           {0}".format(race_type))
    print("Race Laps:           {0}".format(int(race_laps)))
    print("Race Duration:       {0}".format(round(race_duration, 2)))
    sample_laps_time()
    print("\n==== Fuel Information ====")
    print("Laps of Fuel:        {0}".format(int(race_laps + extra_laps)))
    print("Fuel Required:       {0}".format(round(fuel_required, 3)))
    sample_laps_fuel()
    
    
def sample_laps_time():
    if est_laps:
        print("Average Lap Time:    {0}".format(avg_lap_time))
        print("Sample Laps:         {0}".format("Time Estimated"))
    else:
        print("Average Lap Time:    {0}".format(avg_lap_time))
        print("Sample Laps:         {0}".format("No variable yet"))


def sample_laps_fuel():
    if est_laps:
        print("Average Fuel Used:   {0}".format(avg_fuel_used))
        print("Sample Laps:         {0}".format("Fuel Estimated"))
    else:
        print("Average Fuel Used:   {0}".format(avg_fuel_used))
        print("Sample Laps:         {0}".format("No variable yet"))


def main():
    user_inquiry()
    print_variables()
    print_results()

    
main()
