def degree(hour, minutes):
    deg =  ((30 * hour + 0.5 * minutes - 6 * minutes)**2)**0.5
    
    if deg == 180:
        print("Straight line")
    
    if deg < 180:
        print(deg)
    
    if deg > 180:
        deg = 360 - deg
        print(deg)


def main():
    hour = 0
    minutes = 0

    hour = int(input("What time is it?\nHour : "))
    if hour >= 0 and hour < 24 : 
        minutes = int(input("Minutes : "))
    
        if hour > 11 :
            hour -= 12
        
        if minutes >= 0 or minutes < 60:
            degree(hour, minutes)  

if __name__ == "__main__":
    main()