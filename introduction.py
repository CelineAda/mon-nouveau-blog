volume = input()
volume = int (volume)
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for backaground music")
elif 40 <= volume < 60:
    print ("Pefect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume > 100:
    print ("A bit loud")
else:
    print ("My ears are hurting!")
