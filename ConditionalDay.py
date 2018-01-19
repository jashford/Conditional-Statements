def day():
    print "You've just started your day..."
    print "Do you go to school or do you stay home?"
    answer = raw_input("Type school or home and hit 'Enter'.").upper()
    if answer == "school" or answer == "0":
        print "You have five classes to go to today and it will give you a lot of homework!"
    elif answer == "home" or answer == "1":
        print "You're going to fall behind in your classes... you're not really sick"
    else:
        print "You didn't pick either of the options. Try again."
        day()

day()
