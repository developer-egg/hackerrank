def time_conversion(s):
    hour = int(s[0:2])
    minutes = s[3:5]
    seconds = s[6:8]
    AMorPM = s[8:10]

    if AMorPM == "PM" and hour != 12:
        hour += 12

    if AMorPM == "AM" and hour == 12:
        hour = 0

    # convert hour back to string
    hour = str(hour)

    if len(hour) == 1:
        hour = "0" + hour

    return f"{hour}:{minutes}:{seconds}"

    

print(time_conversion("12:45:54PM"))