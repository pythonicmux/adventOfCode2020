# ranges: field => set of valid ranges of integers
ranges = {}
# possible_fields: contains all possible fields for each of the slots.
possible_fields = []

with open('day16.txt', 'r') as f:
    lines = f.readlines()

line_idx = 0

# Get the ranges of values for each field and put it in a set containing the ranges.
while lines[line_idx] != '\n':
    line = lines[line_idx]
    min1 = int(line.split(':')[1].split()[0].split('-')[0])
    max1 = int(line.split(':')[1].split()[0].split('-')[1])
    min2 = int(line.split(':')[1].split()[2].split('-')[0])
    max2 = int(line.split(':')[1].split()[2].split('-')[1])
    valid_values = range(min1, max1+1) + range(min2, max2+1)
    ranges[line.split(":")[0]] = set(valid_values)
    line_idx += 1

print(line_idx, len(ranges.keys()))

# At first, each slot can be any field. We'll eliminate possible fields as
# we look through the valid tickets.
for i in range(line_idx):
    possible_fields.append(set(ranges.keys()))

# Look through the remaining tickets. An invalid ticket is one that
# has all three values not in any of the ranges of the fields. We simply
# need to check that a value in the ticket is not in any field to know
# that it's invalid.
#
# A ticket with all valid numbers is a valid ticket. Given that the
# tickets all have the same ordering of numbers, we can look at which
# ranges each number doesn't belong in to eliminate potential fields
# that don't fit this ticket (and therefore all tickets') configurations.
while line_idx < len(lines):
    line = lines[line_idx]

    if line != '\n' and line.strip()[-1] != ':':
        nums = map(lambda x:int(x), line.split(','))
        # Check to see if the ticket is valid.
        ticket_valid = True
        for n in nums:
            number_valid = False
            for k in ranges:
                if n in ranges[k]:
                    number_valid = True
            if number_valid == False:
                ticket_valid = False
                break

        # If we have a valid ticket then check which potential
        # fields it can't have.
        if ticket_valid == True:
            for i in range(len(nums)):
                eliminated_fields = []
                for field in possible_fields[i]:
                    if nums[i] not in ranges[field]:
                        eliminated_fields.append(field)
                for field in eliminated_fields:
                    possible_fields[i].remove(field)


    line_idx += 1

print(possible_fields)

# Now that we've got all possible field configurations, we can find out the true
# configuration by eliminating possibilities and finding out which one is assigned to
# which slot. We look for the position with only one possibility and then eliminate it
# from all the others. We only need to do this n times, where n is the number of fields.

# This is the set of slots we've confirmed - we don't need to repeat eliminating this field
# from other slots.
fixed = set()
for i in range(len(ranges.keys())):

    # Find a new slot with only one possible field.
    confirmed_slot = -1
    for idx in range(len(possible_fields)):
        slot = possible_fields[idx]
        if(len(slot) == 1 and idx not in fixed):
            confirmed_slot = idx
            break

    if(confirmed_slot == -1):
        print("Could not find a confirmed slot.")
        print(possible_fields)
        break

    # Mark this slot as confirmed.
    fixed.add(confirmed_slot)

    # Remove the slot's value from all other fields.
    val = list(possible_fields[confirmed_slot])[0]
    for idx in range(len(possible_fields)):
        if idx != confirmed_slot and val in possible_fields[idx]:
            possible_fields[idx].remove(val)

print(possible_fields)

# Print the answer based on the deduced fields.
# Get the quotient of the values of all "departure*" fields.

# Get the values of your ticket.
your_ticket_line = 0
for i in range(len(lines)):
    l = lines[i]
    if l.startswith("your ticket:"):
        your_ticket_line = i+1
        break
your_ticket = map(lambda x:int(x), lines[your_ticket_line].split(','))

# Get the desired quotient.
quotient = 1
for i in range(len(your_ticket)):
    if(list(possible_fields[i])[0].startswith('departure')):
        quotient *= your_ticket[i]

print(quotient)

