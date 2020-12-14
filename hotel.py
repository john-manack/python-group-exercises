hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

# Import PrettyPrint
import pprint
pp = pprint.PrettyPrinter(indent = 4)

#Functions Defined Below

def check_in():
    while True:
      floor = int(input("What floor would you like? Enter a number between 1 and 13:"))
      if floor <= 13:
        break
      else:
        print("Sorry that wasn't in the correct range. Please try again.")
    room_min = (floor * 100) + 1
    room_max = (floor * 100) + 99
    while True:
      room = int(input("What room number would you like? Enter a number between " + str(room_min) + " and " + str(room_max) + ":"))
      while room < int(room_min) or room > int(room_max):
        room = int(input("Sorry that wasn't in the correct range. Enter a number between " + str(room_min) + " and " + str(room_max) + ":"))
      if (str(floor)) in hotel:
        if (str(room)) in hotel[str(floor)]:
          print("This room is taken! Please suggest another room.")
        else:
          print("It looks like this room is available! Let's get a little more information.")
          break
      else:
        print("It looks like this room is available! Let's get a little more information.")
        break
    while True:
      occupants = int(input("How many guests? "))
      if occupants >= 1 and occupants <= 6:
        break
      else:
        print("Apologies - we allow a maximum of 6 guests per room. \n Please enter a number between 1 and 6.")
    guests = []
    guest_count = 1
    while guest_count <= occupants:
      guests.append(input("Please enter guest name (%d of %d):" % (guest_count, occupants)))
      guest_count += 1
    if (str(floor)) in hotel:
      hotel[str(floor)][str(room)] = guests
    else:
      hotel[str(floor)] = {}
      hotel[str(floor)][str(room)] = guests
    print("You're all checked in! Please enjoy your stay. Current checked-in guests include:")
    pp.pprint(hotel)
    
def check_out():
    while True:
      floor = int(input("Which floor were you on? Enter number between 1 and 13:"))
      if floor <= 13 and floor >= 1:
        if str(floor) in hotel:
          break
        else:
          print("This floor is vacant! Please try again.")
      else:
        print("Sorry that wasn't in the correct range. Please try again.")
    room_min = (floor * 100) + 1
    room_max = (floor * 100) + 99
    while True:
      room = int(input("Which room were you staying in? Enter a number between " + str(room_min) + " and " + str(room_max) + ":"))
      while room < int(room_min) or room > int(room_max):
        room = int(input("Sorry that wasn't in the correct range. Enter a number between " + str(room_min) + " and " + str(room_max) + ":"))
      if (str(room)) in hotel[str(floor)]:
        print("Perfect! You're all checked out. Current checked-in guests include:")
        break
      else:
        print("This room is vacant! Please try again.")
    del hotel[str(floor)][str(room)]
    pp.pprint(hotel)

#Run Program

while True:
  in_or_out = input("Welcome to the front desk! Please type one of the following options: \n 'in' for check-in \n 'out' for check-out \n 'list' for guest list \n 'quit' to close the program \n Type your selection here: ")
  in_or_out = in_or_out.lower()
  if in_or_out == 'in':
    check_in()
  elif in_or_out == 'out':
    check_out()
  elif in_or_out == 'list':
    pp.pprint(hotel)
  elif in_or_out == 'quit':
    break
  else:
    print("I'm sorry. I didn't understand your entry.")