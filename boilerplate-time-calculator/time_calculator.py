def add_time(start, duration, day=False):
    
    days_index = {
      "monday": 0, 
      "tuesday": 1, 
      "wednesday": 2, 
      "thursday": 3, 
      "friday": 4, 
      "saturday": 5, 
      "sunday": 6}

    days_array = [
      "Monday", 
      "Tuesday", 
      "Wednesday", 
      "Thursday", 
      "Friday", 
      "Saturday", 
      "Sunday"]

    duration_tuple = duration.partition(":")
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])
    
    start_tuple = start.partition(":")
    start_minutes_tuple = start_tuple[2].partition(" ")
    start_hours = int(start_tuple[0])
    start_minutes = int(start_minutes_tuple[0])
    am_pm = start_minutes_tuple[2]
    am_pm_flip = {"AM": "PM", "PM": "AM"}

    ammount_of_days = int(duration_hours / 24)
    
    end_minutes = start_minutes + duration_minutes
    if(end_minutes >= 60):
      start_hours += 1
      end_minutes = end_minutes % 60
    ammount_am_pm_flips = int((start_hours + duration_hours) / 12)
    end_hours = (start_hours + duration_hours) % 12

    if(not(end_minutes > 9)): 
      end_minutes ="0" + str(end_minutes)

    if(end_hours == 0):
      end_hours = 12
  
    if(am_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
      ammount_of_days += 1

    if(ammount_am_pm_flips % 2 == 1):
      am_pm = am_pm_flip[am_pm]
    
    Time = str(end_hours) + ":" + str(end_minutes) + " " + am_pm 
    if(day):
      day = day.lower()
      index = int((days_index[day]) + ammount_of_days) % 7
      new_day = days_array[index]
      Time += ", " + new_day

    if(ammount_of_days == 1):
      return Time + " " + "(next day)"
    elif(ammount_of_days > 1):
      return Time + " (" + str(ammount_of_days) + " days later)" 
    return Time