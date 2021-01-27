def add_time(start, duration, day=False):

    # Start Time
    startsplit = start.split(" ")
    start_split2 = startsplit[0].split(":")

    start_hours = int(start_split2[0])
    start_minutes = int(start_split2[1])
    start_am_pm = startsplit[1]

    if start_am_pm == "PM":
        start_hours += 12

    start_time_in_minutes = (int(start_hours*60)) + start_minutes


    #Duration

    duration_split = duration.split(":")
    duration_hours = int(duration_split[0])
    duration_minutes = int(duration_split[1])
    duration_in_minutes = int(duration_hours * 60) + duration_minutes

    # Calc days

    full_minutes = start_time_in_minutes + duration_in_minutes

    # Cal Time

    am_pm = ""

    minutes = int(full_minutes%60)

    hours = int(full_minutes%1440/60)


    if hours > 12:
        hours -= 12
        am_pm = "PM"
    elif hours == 12:
        am_pm = "PM"
    elif hours == 0:
        hours = 12
        am_pm = "AM"
    else:
        am_pm = "AM"


    minutes = '{:02}'.format(minutes)

    print(minutes)
    

    num_of_days = full_minutes//1440

    if num_of_days == 1:
        days_passed = " (next day)"
    elif num_of_days > 1:
        days_passed = " (" + str(num_of_days) + " days later)"
    else:
        days_passed = ""


    # Cal Day of the week

    if day:
        day = day.title()

        days = {"Monday": 1,
        "Tuesday": 2,
        "Wednesday" : 3,
        "Thursday" : 4,
        "Friday": 5,
        "Saturday" : 6,
        "Sunday": 7}

        if day in days:
           final_day = days[day] + num_of_days
           if final_day > 7:
               final_day = final_day%7
               
        for key in days:
            if days[key] == final_day:
                output_day = key

        new_time = str(str(hours) + ":" + str(minutes) + " " + am_pm + ", " + output_day + days_passed)
    
    else:
        new_time = str(str(hours) + ":" + str(minutes) + " " + am_pm + days_passed)

    print(new_time)

    return new_time