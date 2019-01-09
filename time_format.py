def format_race_time(time_input):  # Function to format race time
  h, m = divmod(time_input, 60)
  s = ((m - int(m)) * 60)
  h = str(int(h))

  # Prints out hours if race time is 60 minutes or more
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

  # Omits printing hours since race time is under 60 minutes
  # Race time is rounded purely to minutes only because if calculating race time
  # I wanted to be able to see 'exact' time
  else:
    if int(m) < 10:
        m = ("0{0}".format(int(m)))
    else:
        m = ("{0}".format(int(m)))
    if s < 10:
        s = (":0{0}".format(int(s)))
    else:
        s = (":{0}".format(int(s)))
    if str(s) == ":00":
        return str(m) + " minutes"
    else:
        return str((int(round(float(time_input), 0)))) + " minutes"


def format_lap_time(time_input):  # Function specifically to format lap times
    m, s = divmod(time_input, 60)
    if int(m) == 0:

            # If lap is under 1 min, return seconds rounded to 3 places (ss.xxx)
            return str(round(s, 3))
    if float(s) < 10.0 and int(m) != 0:
        
        # This exsists because I don't know how to make the 0 appear without forcing it
        # Returns mm:0s.xxx
        return str(int(m)) + ":0" + str(round(s, 3))
    else:

        # This is the other side of the last line
        # Returns mm:ss.xxx
        return str(int(m)) + ":" + str(round(s, 3))


if __name__ == '__main__':  # Exsists purely for my testing purposes
    print("--- Race Times ---")
    print(format_race_time(20))
    print(format_race_time(49.7))
    print(format_race_time(60.2))
    print(format_race_time(328.9))
    print(format_race_time(1295.97))
    print("--- Lap Times ---")
    print(format_lap_time(619.936))
    print(format_lap_time(123.456))
    print(format_lap_time(82.456))
    print(format_lap_time(48.876))
