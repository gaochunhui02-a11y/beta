print("Tomorrow Study Scheduler")
print("------------------------")

# Convert a time like 14:30 into minutes
def time_to_minutes(time):
    parts = time.split(":")
    hour = int(parts[0])
    minute = int(parts[1])

    return hour * 60 + minute


# Convert minutes back into a time like 14:30
def minutes_to_time(minutes):
    hour = minutes // 60
    minute = minutes % 60

    return str(hour).zfill(2) + ":" + str(minute).zfill(2)


wake_time = input("What time will you wake up? (Example 08:00): ")
sleep_time = input("What time will you stop studying? (Example 22:00): ")

wake = time_to_minutes(wake_time)
sleep = time_to_minutes(sleep_time)


# -------------------------
# Classes
# -------------------------

classes = []

class_count = int(input("\nHow many classes do you have tomorrow? "))

for i in range(class_count):
    print("\nClass", i + 1)

    name = input("Class name: ")
    start = input("Start time (Example 10:00): ")
    end = input("End time (Example 11:30): ")

    classes.append([
        time_to_minutes(start),
        time_to_minutes(end),
        name
    ])


# Put classes in time order
classes.sort()


# -------------------------
# Study subjects
# -------------------------

subjects = []

subject_count = int(input("\nHow many subjects do you need to study? "))

for i in range(subject_count):
    print("\nSubject", i + 1)

    name = input("Subject name: ")
    minutes = int(input("How many minutes do you want to study? "))

    subjects.append([name, minutes])


# -------------------------
# Make the schedule
# -------------------------

schedule = []

current_time = wake
subject_index = 0


for school_class in classes:

    class_start = school_class[0]
    class_end = school_class[1]
    class_name = school_class[2]

    # Use the free time before class for studying
    while subject_index < len(subjects) and current_time < class_start:

        subject_name = subjects[subject_index][0]
        study_minutes = subjects[subject_index][1]

        free_minutes = class_start - current_time

        # Study the whole subject if it fits
        if study_minutes <= free_minutes:

            schedule.append([
                current_time,
                current_time + study_minutes,
                "Study: " + subject_name
            ])

            current_time = current_time + study_minutes
            subject_index = subject_index + 1

        # Study part of it if it does not fit
        else:

            schedule.append([
                current_time,
                class_start,
                "Study: " + subject_name
            ])

            subjects[subject_index][1] = study_minutes - free_minutes
            current_time = class_start

    # Add the class
    schedule.append([
        class_start,
        class_end,
        "Class: " + class_name
    ])

    current_time = class_end


# -------------------------
# Study after last class
# -------------------------

while subject_index < len(subjects) and current_time < sleep:

    subject_name = subjects[subject_index][0]
    study_minutes = subjects[subject_index][1]

    available_time = sleep - current_time

    if study_minutes <= available_time:

        schedule.append([
            current_time,
            current_time + study_minutes,
            "Study: " + subject_name
        ])

        current_time = current_time + study_minutes
        subject_index = subject_index + 1

    else:

        schedule.append([
            current_time,
            sleep,
            "Study: " + subject_name
        ])

        subjects[subject_index][1] = study_minutes - available_time
        current_time = sleep


# -------------------------
# Show schedule
# -------------------------

print("\n")
print("YOUR SCHEDULE FOR TOMORROW")
print("--------------------------")

for item in schedule:

    start = minutes_to_time(item[0])
    end = minutes_to_time(item[1])
    name = item[2]

    print(start, "-", end, "|", name)


# Check for unfinished studying
if subject_index < len(subjects):

    print("\nYou do not have enough time for everything.")

    print("\nStill left:")

    for i in range(subject_index, len(subjects)):
        print(subjects[i][0], "-", subjects[i][1], "minutes")

else:
    print("\nEverything fits into your day!")