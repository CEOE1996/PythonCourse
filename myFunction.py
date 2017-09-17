def MinutesToHours(minutes, seconds = 0):
    hours = minutes / 60 + seconds / 3600
    return hours

print(MinutesToHours(70, 300))
print(MinutesToHours(70))

help(1);
