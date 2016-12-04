def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called "houses" that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army"
            ])

    """

    with open(filename) as cohort_data:

        # initialize house list
        house_list = []

        # add to house list
        for line in cohort_data:
            student = line.strip().split('|')
            if student[2]:
                house_list.append(student[2])

        #   list comprehension way
        #house_list = [line.strip().split('|')[2] for line in cohort_data if line.strip().split('|')[2]]

    # create unique set of houses from house list
    houses = set(house_list)

    # Code goes here

    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort, skipping instructors.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name. Put ghosts into a separate list entitled "ghosts".
    Returns a list of these lists.

        ex. fall_15 = ["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ""Hermione Granger", ... ]
        ex. all_students = [["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ...],
        ["Lee Jordan", "Andrew Kirke", "Neville Longbottom", ...],
        ["Cormac McLaggen", "Parvati Patil", "Jimmy Peakes", ...], 
        ["Euan Abercrombie", "Katie Bell", "Lavender Brown", ...]]

    """
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    with open(filename) as cohort_data:

        for line in cohort_data:
            person = line.strip().split("|")
            full_name = "%s %s" % (person[0], person[1])
            cohort = person[-1]

            if cohort == "G": 
                ghosts.append(full_name)
            elif cohort != "I":
                if cohort == "Winter 2016":
                    winter_16.append(full_name)
                elif cohort == "Fall 2015":
                    fall_15.append(full_name)
                elif cohort == "Spring 2016":
                    spring_16.append(full_name)
                else:
                    summer_16.append(full_name)

    # summer_16.sort()
    # spring_16.sort()
    # fall_15.sort()
    # ghosts.sort()
    all_students = [sorted(winter_16), sorted(spring_16), sorted(summer_16), sorted(fall_15), sorted(ghosts)]

    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.


    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort ghosts into a list called "ghosts"
    and instructors into a list called "instructors".
    Return all lists in one list of lists.

        ex. gryffindor = ["Abercrombie", "Bell", "..." ]
        ex. ghosts = ["Baron", "Friar", "..."]
        ex. all_students = [ hufflepuff,
                    gryffindor,
                    ravenclaw,
                    slytherin,
                    dumbledores_army,
                    ghosts,
                    instructors
        ]

    """
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    ravenclaw = []
    ghosts = []
    instructors = []

    with open(filename) as cohort_data:

            for line in cohort_data:
                person = line.strip().split("|")
                last_name = person[1]
                house = person[2]
                cohort = person[-1]

                if cohort == "G":
                    ghosts.append(last_name)
                elif cohort == "I":
                    instructors.append(last_name)
                else:
                    if house == "Hufflepuff":
                        hufflepuff.append(last_name)
                    elif house == "Gryffindor":
                        gryffindor.append(last_name)
                    elif house == "Ravenclaw":
                        ravenclaw.append(last_name)
                    elif house == "Slytherin":
                        slytherin.append(last_name)
                    else:
                        dumbledores_army.append(last_name)



    all_students = [sorted(ghosts), sorted(instructors), sorted(hufflepuff), sorted(gryffindor), sorted(ravenclaw), sorted(slytherin)]
    

    return all_students


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. student_list = [
                ("Euan Abercrombie", "Gryffindor", "McGonagall", "Summer 2016"),
                ("Katie Bell", "Gryffindor", "McGonagall", "Summer 2016"),
                # ...
            ]
    """

    student_list = []

    # Code goes here

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name from the command line, returns that
    student's cohort, or returns "Student not found." when appropriate. """

    # Code goes here

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student last names that have duplicates.

    Iterates over the data to find any last names that exist across all cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Weasley"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and when given a name, print a statement of everyone in their house in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function
    that, when given a student's first and last name, print students that are in both
    that student's cohort and that student"s house.

    ex: Choose a student: Hermione Granger
        Hermione Granger was in house Gryffindor in the Fall 2015
        cohort.
        The following students are also in their house:
        Seamus Finnigan
        Angelina Johnson
        Harry Potter
        Ron Weasley
        Oliver Wood


    """

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!

print unique_houses("cohort_data.txt")
print sort_by_cohort("cohort_data.txt")
print students_by_house("cohort_data.txt")
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
