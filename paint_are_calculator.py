from math import ceil

height = int(input("Enter height of the wall: "))
width = int(input("Enter width of the wall: "))
coverage = 5

def can_count_calculator(height, width, coverage):
    cans_needed = ceil((height * width) / coverage)
    print(f"You'll need {cans_needed} of paint.")

can_count_calculator(height = height, width = width, coverage = coverage)