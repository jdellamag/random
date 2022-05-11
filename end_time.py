# Program that calculates what time something ends, based on what time it started

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hours_conv_to_mins = hour * 60
start_mins = hours_conv_to_mins + mins
runtime = start_mins + dura

endhour = (runtime // 60) % 24
endmin = runtime % 60

print(endhour,":",endmin)
print("end sequence")

print(endhour,":",endmin)

print("test commit")
print("second commit test")
print("final test for commit stuff")
