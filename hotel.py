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


def front_desk():
    status = input("Are you checking in or checking out? Please type 'in' or 'out'.")
    status = status.lower()
    return status

def check_in():
    floor = int(input("What floor would you like? Enter a number between 1 and 13:"))
    room = int(input("What room number would you like? Enter a number between " + str((floor * 100)+1) + " and " + str((floor * 100)+99) + ":"))
    if room < int((floor * 100) + 1) and room > int((floor * 100) + 99):
        room = int(input("Sorry that wasn't in the correct range. Enter a number between " + str((floor * 100)+1) + " and " + str((floor * 100)+99) + ":"))
    else:
        occupants = int(input("How many guests?"))
        guests = input
    
def check_out():
    floor = int(input("Which floor were you on? Enter number between 1 and 13:"))
    room = int(input("What room number would you like? Enter number between " + str((floor * 100)+1) + " and " + str((floor * 100)+99) + ":"))

if front_desk() == 'in':
    check_in()
else:
    check_out()