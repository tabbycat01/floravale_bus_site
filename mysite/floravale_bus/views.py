from django.shortcuts import render
from django.views.generic import TemplateView

from datetime import datetime, date, time, timedelta
import calendar
from datetime import date, datetime
from workalendar.asia import Singapore

# Create your views here.

class IndexView(TemplateView):
    template_name = 'floravale_bus/index.html'

def BoonLayTimingView(request):
    current_date = date.today()
    current_year = current_date.year
    cal = Singapore()
    holidays = cal.holidays(current_year)
    dict_of_public_holiday = {}
    for holiday in holidays:
        holiday_date = str(holiday[0])
        holiday_name = holiday[1]
        dict_of_public_holiday[holiday_date] = holiday_name.replace("shift", "")
    current_day = list(calendar.day_abbr)[current_date.weekday()]
    print("Day:", current_day)  #days are in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    everything_now = datetime.now()
    current_time = everything_now.strftime("%H:%M:%S")
    current_time_obj = datetime.strptime(current_time, "%H:%M:%S")
    print("Time:", current_time)
    if str(current_date) in dict_of_public_holiday:
        ans = "There is no bus service today due to "+ dict_of_public_holiday[str(current_date)] + "."
    else:
        if current_date.weekday() < 5:    #weekdays
            first_bus_to_bl_string = "06:20:00"
            last_bus_to_bl_string = "19:40:00"
            first_bus_to_bl_object = datetime.strptime("06:20:00", "%H:%M:%S")
            last_bus_to_bl_object = datetime.strptime("19:40:00", "%H:%M:%S")
            if current_time < first_bus_to_bl_string:
                time_to_first_bus_to_bl = first_bus_to_bl_object - current_time_obj
                time_to_first_bus_to_bl_string = str(time_to_first_bus_to_bl)
                if time_to_first_bus_to_bl_string[0] == "0":
                    time_to_first_bus_to_bl_string = time_to_first_bus_to_bl_string[2:]
                    ans = "First bus to Boon Lay has not started yet. First bus to Boon Lay begins in: "+ time_to_first_bus_to_bl_string[:2]+ " minutes" + "."
                else:
                    ans = "First bus to Boon Lay has not started yet. First bus to Boon Lay begins in "+ time_to_first_bus_to_bl_string[0]+ " hours "+ time_to_first_bus_to_bl_string[2:4]+ " minutes" + "."
            elif current_time > last_bus_to_bl_string:
                ans = "Last bus to Boon Lay has already departed."
            elif current_time == first_bus_to_bl_string:
                ans = "First bus to Boon Lay is departing now."
            elif current_time == last_bus_to_bl_string:
                ans = "Last bus to Boon Lay is departing now."
            else:   #current time is within operating hours
                bus_to_bl = first_bus_to_bl_string
                while current_time > bus_to_bl:
                    bus_to_bl_object = datetime.strptime(bus_to_bl, "%H:%M:%S") #convert from string to object so as to manipulate it with timedelta
                    if bus_to_bl < "10:15:00" or bus_to_bl >= "17:40:00":
                        time_interval = 20
                    else:
                        time_interval = 25
                    bus_to_bl_object += timedelta(minutes=time_interval)
                    bus_to_bl = datetime.strftime(bus_to_bl_object, "%H:%M:%S") #convert back from obj to string so as to compare with current time which is a string
                    if bus_to_bl > "09:00:00" and bus_to_bl < "10:15:00":
                        bus_to_bl = "10:15:00"
                    elif bus_to_bl > "12:45:00" and bus_to_bl < "14:20:00":
                        bus_to_bl = "14:20:00"
                    elif bus_to_bl > "16:25:00" and bus_to_bl < "17:40:00":
                        bus_to_bl = "17:40:00"
                if bus_to_bl == current_time and bus_to_bl == "09:00:00":
                    ans = "Bus to Boon Lay is departing now. Next bus is at 10.15am."
                elif bus_to_bl == current_time and bus_to_bl == "12:45:00":
                    ans = "Bus to Boon Lay is departing now. Next bus is at 2.20pm."
                elif bus_to_bl == current_time and bus_to_bl == "16:25:00":
                    ans = "Bus to Boon Lay is departing now. Next bus is at 5.40pm."
                else:
                    if bus_to_bl == current_time:
                        ans = "Bus to Boon Lay is departing now."
                print("Bus timing:", bus_to_bl)
                bus_to_bl_object = datetime.strptime(bus_to_bl, "%H:%M:%S")
                time_to_next_bus = bus_to_bl_object - current_time_obj
                time_to_next_bus_string = str(time_to_next_bus)
                if time_to_next_bus_string[0] == "0":
                    time_to_next_bus_string = time_to_next_bus_string[2:]
                    ans = "Time left till next bus to Boon Lay: "+ time_to_next_bus_string[:2]+ " minutes "+ time_to_next_bus_string[3:]+ " seconds."
                else:
                    ans = "Time left till next bus to Boon Lay: "+ time_to_next_bus_string[0]+ " hours "+ time_to_next_bus_string[2:4]+ " minutes "+ time_to_next_bus_string[5:]+ " seconds."
        elif current_date.weekday() == 5: #saturday
            first_bus_to_bl_string = "07:00:00"
            last_bus_to_bl_string = "16:50:00"
            first_bus_to_bl_object = datetime.strptime("07:00:00", "%H:%M:%S")
            last_bus_to_bl_object = datetime.strptime("16:50:00", "%H:%M:%S")
            if current_time < first_bus_to_bl_string:
                time_to_first_bus_to_bl = first_bus_to_bl_object - current_time_obj
                time_to_first_bus_to_bl_string = str(time_to_first_bus_to_bl)
                if time_to_first_bus_to_bl_string[0] == "0":
                    time_to_first_bus_to_bl_string = time_to_first_bus_to_bl_string[2:]
                    ans = "First bus to Boon Lay has not started yet. First bus to Boon Lay begins in: "+ time_to_first_bus_to_bl_string[:2]+ " minutes "+ time_to_first_bus_to_bl_string[3:]+ " seconds."
                else:
                    ans = "First bus to Boon Lay has not started yet. First bus to Boon Lay begins in "+ time_to_first_bus_to_bl_string[0]+ " hours "+ time_to_first_bus_to_bl_string[2:4]+ " minutes "+ time_to_first_bus_to_bl_string[5:]+ " seconds."
            elif current_time > last_bus_to_bl_string:
                ans = "Last bus to Boon Lay has already departed."
            elif current_time == first_bus_to_bl_string:
                ans = "First bus to Boon Lay is departing now."
            elif current_time == last_bus_to_bl_string:
                ans = "Last bus to Boon Lay is departing now."
            else:   #current time is within operating hours
                bus_to_bl = first_bus_to_bl_string
                while current_time > bus_to_bl:
                    bus_to_bl_object = datetime.strptime(bus_to_bl, "%H:%M:%S") #convert from string to object so as to manipulate it with timedelta
                    if bus_to_bl < "10:15:00":
                        time_interval = 20
                    else:
                        time_interval = 25
                    bus_to_bl_object += timedelta(minutes=time_interval)
                    bus_to_bl = datetime.strftime(bus_to_bl_object, "%H:%M:%S") #convert back from obj to string so as to compare with current time which is a string
                    if bus_to_bl > "09:00:00" and bus_to_bl < "10:15:00":
                        bus_to_bl = "10:15:00"
                    elif bus_to_bl > "12:45:00" and bus_to_bl < "14:20:00":
                        bus_to_bl = "14:20:00"
                if bus_to_bl == current_time and bus_to_bl == "09:00:00":
                    ans = "Bus to Boon Lay is departing now. Next bus is at 10.15am."
                elif bus_to_bl == current_time and bus_to_bl == "12:45:00":
                    ans = "Bus to Boon Lay is departing now. Next bus is at 2.20pm."
                else:
                    if bus_to_bl == current_time:
                        ans = "Bus to Boon Lay is departing now."
                print(bus_to_bl)
                bus_to_bl_object = datetime.strptime(bus_to_bl, "%H:%M:%S")
                time_to_next_bus = bus_to_bl_object - current_time_obj
                time_to_next_bus_string = str(time_to_next_bus)
                if time_to_next_bus_string[0] == "0":
                    time_to_next_bus_string = time_to_next_bus_string[2:]
                    ans = "Time left till next bus to Boon Lay: "+ time_to_next_bus_string[:2]+ " minutes "+ time_to_next_bus_string[3:]+ " seconds."
                else:
                    ans = "Time left till next bus to Boon Lay: "+ time_to_next_bus_string[0]+ " hours "+ time_to_next_bus_string[2:4]+ " minutes "+ time_to_next_bus_string[5:]+ " seconds."
        else:
            ans = "There is no bus service today."

    context = {'ans': ans}
    return render(request, 'floravale_bus/timing.html', context)

def FloravaleTimingView(request):
    current_date = date.today()
    current_year = current_date.year
    cal = Singapore()
    holidays = cal.holidays(current_year)
    dict_of_public_holiday = {}
    for holiday in holidays:
        holiday_date = str(holiday[0])
        holiday_name = holiday[1]
        dict_of_public_holiday[holiday_date] = holiday_name.replace("shift", "")
    current_day = list(calendar.day_abbr)[current_date.weekday()]
    print("Day:", current_day)  #days are in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    everything_now = datetime.now()
    current_time = everything_now.strftime("%H:%M:%S")
    current_time_obj = datetime.strptime(current_time, "%H:%M:%S")
    print("Time:", current_time)
    if str(current_date) in dict_of_public_holiday:
        ans = "There is no bus service today due to "+ dict_of_public_holiday[str(current_date)] + "."
    else:
        if current_date.weekday() < 5:    #weekdays
            first_bus_to_fv_string = "06:30:00"
            last_bus_to_fv_string = "19:50:00"
            first_bus_to_fv_object = datetime.strptime("06:30:00", "%H:%M:%S")
            last_bus_to_fv_object = datetime.strptime("19:50:00", "%H:%M:%S")
            if current_time < first_bus_to_fv_string:
                time_to_first_bus_to_fv = first_bus_to_fv_object - current_time_obj
                time_to_first_bus_to_fv_string = str(time_to_first_bus_to_fv)
                if time_to_first_bus_to_fv_string[0] == "0":
                    time_to_first_bus_to_fv_string = time_to_first_bus_to_fv_string[2:]
                    ans = "First bus to Floravale has not started yet. First bus to Floravale begins in: "+ time_to_first_bus_to_fv_string[:2]+ " minutes "+ time_to_first_bus_to_fv_string[3:]+ " seconds."
                else:
                    ans = "First bus to Floravale has not started yet. First bus to Floravale begins in", time_to_first_bus_to_fv_string[0]+ " hours "+ time_to_first_bus_to_fv_string[2:4]+ " minutes "+ time_to_first_bus_to_fv_string[5:]+ " seconds."
            elif current_time > last_bus_to_fv_string:
                ans = "Last bus to Floravale has already departed."
            elif current_time == first_bus_to_fv_string:
                ans = "First bus to Floravale is departing now."
            elif current_time == last_bus_to_fv_string:
                ans = "Last bus to Floravale is departing now."
            else:   #current time is within operating hours
                bus_to_fv = first_bus_to_fv_string
                while current_time > bus_to_fv:
                    bus_to_fv_object = datetime.strptime(bus_to_fv, "%H:%M:%S") #convert from string to object so as to manipulate it with timedelta
                    if bus_to_fv < "10:00:00" or bus_to_fv >= "17:30:00":
                        time_interval = 20
                    else:
                        time_interval = 25
                    bus_to_fv_object += timedelta(minutes=time_interval)
                    bus_to_fv = datetime.strftime(bus_to_fv_object, "%H:%M:%S") #convert back from obj to string so as to compare with current time which is a string
                    if bus_to_fv > "08:50:00" and bus_to_fv < "10:00:00":
                        bus_to_fv = "10:00:00"
                    elif bus_to_fv > "12:30:00" and bus_to_fv < "14:05:00":
                        bus_to_fv = "14:05:00"
                    elif bus_to_fv > "16:10:00" and bus_to_fv < "17:30:00":
                        bus_to_fv = "17:30:00"
                if bus_to_fv == current_time and bus_to_fv == "08:50:00":
                    ans = "Bus to Floravale is departing now. Next bus is at 10.00am."
                elif bus_to_fv == current_time and bus_to_fv == "12:30:00":
                    ans = "Bus to Floravale is departing now. Next bus is at 2.05pm."
                elif bus_to_fv == current_time and bus_to_fv == "16:10:00":
                    ans = "Bus to Floravale is departing now. Next bus is at 5.30pm."
                else:
                    if bus_to_fv == current_time:
                        ans = "Bus to Floravale is departing now."
                print("Bus timing:", bus_to_fv)
                bus_to_fv_object = datetime.strptime(bus_to_fv, "%H:%M:%S")
                time_to_next_bus = bus_to_fv_object - current_time_obj
                time_to_next_bus_string = str(time_to_next_bus)
                if time_to_next_bus_string[0] == "0":
                    time_to_next_bus_string = time_to_next_bus_string[2:]
                    ans = "Time to next bus: "+ time_to_next_bus_string[:2]+ " minutes "+ time_to_next_bus_string[3:]+ " seconds."
                else:
                    ans = "Time to next bus: "+ time_to_next_bus_string[0]+ " hours "+ time_to_next_bus_string[2:4]+ " minutes "+ time_to_next_bus_string[5:]+ " seconds."
        elif current_date.weekday() == 5: #saturday
            first_bus_to_fv_string = "07:10:00"
            last_bus_to_fv_string = "16:35:00"
            first_bus_to_fv_object = datetime.strptime("07:10:00", "%H:%M:%S")
            last_bus_to_fv_object = datetime.strptime("16:35:00", "%H:%M:%S")
            if current_time < first_bus_to_fv_string:
                time_to_first_bus_to_fv = first_bus_to_fv_object - current_time_obj
                time_to_first_bus_to_fv_string = str(time_to_first_bus_to_fv)
                if time_to_first_bus_to_fv_string[0] == "0":
                    time_to_first_bus_to_fv_string = time_to_first_bus_to_fv_string[2:]
                    ans = "First bus to Floravale has not started yet. First bus to Boon Lay begins in: "+ time_to_first_bus_to_fv_string[:2]+ " minutes "+ time_to_first_bus_to_fv_string[3:]+ " seconds."
                else:
                    ans = "First bus to Floravale has not started yet. First bus to Boon Lay begins in: "+ time_to_first_bus_to_fv_string[0]+ " hours "+ time_to_first_bus_to_fv_string[2:4]+ " minutes "+ time_to_first_bus_to_fv_string[5:]+ " seconds."
            elif current_time > last_bus_to_fv_string:
                ans = "Last bus to Floravale has already departed."
            elif current_time == first_bus_to_fv_string:
                ans = "First bus to Floravale is departing now."
            elif current_time == last_bus_to_fv_string:
                ans = "Last bus to Floravale is departing now."
            else:   #current time is within operating hours
                bus_to_fv = first_bus_to_fv_string
                while current_time > bus_to_fv:
                    bus_to_fv_object = datetime.strptime(bus_to_fv, "%H:%M:%S") #convert from string to object so as to manipulate it with timedelta
                    if bus_to_fv < "10:00:00":
                        time_interval = 20
                    else:
                        time_interval = 25
                    bus_to_fv_object += timedelta(minutes=time_interval)
                    bus_to_fv = datetime.strftime(bus_to_fv_object, "%H:%M:%S") #convert back from obj to string so as to compare with current time which is a string
                    if bus_to_fv > "08:50:00" and bus_to_fv < "10:00:00":
                        bus_to_fv = "10:00:00"
                    elif bus_to_fv > "12:30:00" and bus_to_fv < "14:05:00":
                        bus_to_fv = "14:05:00"
                if bus_to_fv == current_time and bus_to_fv == "08:50:00":
                    ans = "Bus to Floravale is departing now. Next bus is at 10.00am."
                elif bus_to_fv == current_time and bus_to_fv == "12:30:00":
                    ans = "Bus to Floravale is departing now. Next bus is at 2.05pm."
                else:
                    if bus_to_fv == current_time:
                        ans = "Bus to Floravale is departing now."
                print(bus_to_fv)
                bus_to_fv_object = datetime.strptime(bus_to_fv, "%H:%M:%S")
                time_to_next_bus = bus_to_fv_object - current_time_obj
                time_to_next_bus_string = str(time_to_next_bus)
                if time_to_next_bus_string[0] == "0":
                    time_to_next_bus_string = time_to_next_bus_string[2:]
                    ans = "Time to next bus: "+ time_to_next_bus_string[:2]+ " minutes "+ time_to_next_bus_string[3:]+ " seconds."
                else:
                    ans = "Time to next bus: "+ time_to_next_bus_string[0]+ " hours "+ time_to_next_bus_string[2:4]+ " minutes "+ time_to_next_bus_string[5:]+ " seconds."
        else:
            ans = "There is no bus service today."

    context = {'ans': ans}
    return render(request, 'floravale_bus/timing.html', context)

class TimetableView(TemplateView):
    template_name = 'floravale_bus/timetable.html'