# Be Santa

present_list = []

present_list.append(input("What would you like for Christmas?"))

# want_present = True
# while want_present == True:
#    adl_gifts = input("Anything else? (y/n)?")
#    adl_gifts = adl_gifts.lower
#    if adl_gifts == "y":
#        new_prez = input("What else would you like?")
#        present_list.append(new_prez)


naughty_nice = input("Have you been good or bad this year?")

naughty_nice = naughty_nice.lower()

if naughty_nice == "good":
    print("You've been good this year! You'll receive %s for Christmas!" % present_list[0])
else:
    print("Sorry... You've been bad. Have fun with your lump of coal!")