print()

favorable_outcomes = int(input("How many favorable outcomes of first event? "))
possible_outcomes = int(input("How many possible outcomes of first event? "))

first_decimal = favorable_outcomes / possible_outcomes
percent = first_decimal * 100
print(f"The probability is {percent:.2f}%.\n")

favorable_outcomes = int(input("How many favorable outcomes of second event? "))
possible_outcomes = int(input("How many possible outcomes of second event? "))

second_decimal = favorable_outcomes / possible_outcomes
percent = second_decimal * 100
print(f"The probability is {percent:.2f}%.\n")

and_decimal = first_decimal * second_decimal
percent = and_decimal * 100
print(f"Both: {percent:.2f}%")

or_decimal = first_decimal + second_decimal
percent = or_decimal * 100
print(f"Either (both cannot happen): {percent:.2f}%")

or_overlap_decimal = or_decimal - and_decimal
percent = or_overlap_decimal * 100
print(f"Either (both can happen): {percent:.2f}%.")
