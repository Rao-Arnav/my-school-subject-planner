# MY SCHOOL SUBJECT PLANNER
# Using Tuples and Sets

print("=" * 45)
print("          MY SCHOOL SUBJECT PLANNER")
print("=" * 45)

# PART 1: READ THE STUDENT CARD TUPLE
student = ("Maya", 9, "B")

print("\nPART 1: STUDENT DETAILS")
print("-----------------------")
print("Student:", student[0])
print("Grade and section:", (student[1], student[2]))


# PART 2: CONVERT TIMETABLES INTO SETS
monday_timetable = ("Art", "English", "Maths", "Science", "English")
tuesday_timetable = ("Computing", "English", "History", "Maths", "Music")

monday = set(monday_timetable)
tuesday = set(tuesday_timetable)

print("\nPART 2: TIMETABLE SETS")
print("----------------------")
print("Monday:", monday)
print("Tuesday:", tuesday)


# PART 3: CHANGE THE SETS SAFELY
monday.add("Geography")
monday.discard("Science")

tuesday.add("Music")
tuesday.discard("Computing")

print("\nPART 3: UPDATED TIMETABLES")
print("--------------------------")
print("Monday:", sorted(monday))
print("Tuesday:", sorted(tuesday))


# PART 4: COMPARE THE TWO DAYS
print("\nPART 4: TIMETABLE COMPARISON")
print("----------------------------")

both_days = monday.intersection(tuesday)
either_day = monday.union(tuesday)
only_monday = monday.difference(tuesday)
exactly_one_day = monday.symmetric_difference(tuesday)

print("Subjects on both days:", sorted(both_days))
print("Subjects on either day:", sorted(either_day))
print("Only on Monday:", sorted(only_monday))
print("On exactly one day:", sorted(exactly_one_day))


print("\n" + "=" * 45)
print("       SUBJECT PLANNER COMPLETED!")
print("=" * 45)