from typing import List
# https://adventofcode.com/2022/day/1


# Get user input
print("Please provide input, two blank rows will exit input mode.")
input_rows: List[str] = []
while True:
    input_rows.append(input())
    
    # Break the loop once we see 2 blank lines
    if not any(input_rows[-2:]):
        input_rows.pop()
        break


# Tally up the values for each elf
elf_calorie_totals: List[int] = []  # The index is the elf number zero indexed
elf_snacks = []
for input_row in input_rows:
    # If we have a calorie number on this input row the add it to our snacks stack
    if input_row:
        elf_snacks.append(int(input_row))
    else:
        # It's blank so let's wrap things up for this elf and get ready for the next one!
        elf_calorie_totals.append(sum(elf_snacks))
        elf_snacks = []


# Find the greediest elf!
greediest_elf_index = 0
for elf_index, elf_calories in enumerate(elf_calorie_totals):
    if elf_calories >= elf_calorie_totals[greediest_elf_index]:
        greediest_elf_index = elf_index

# Produce report
print(f"We have {len(elf_calorie_totals)} elves carrying {sum(elf_calorie_totals)} calories.")
print(f"The greediest elf is {greediest_elf_index} who's carrying {elf_calorie_totals[greediest_elf_index]} calories!")
