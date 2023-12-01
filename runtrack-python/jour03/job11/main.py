
def time_to_text(num):
    hour = num // 60
    mins = num - (hour * 60)
    
    if hour == 0:
        print(f"{mins} minutes")
    elif hour == 1:
        print(f"{hour} heure et {mins} minute")
    else:
        print(f"{hour} heures et {mins} minutes")

time_to_text(71)   
time_to_text((5100)) 
time_to_text(358) 
time_to_text(59)   
