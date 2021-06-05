# Task 17: Import the modules csv, tui and visual
import tui
import csv
import visual

dict_planets = {"Planets": [], "Non Planets": []}
planets_gravity = {"Low Gravity": [], "Medium Gravity": [], "High Gravity": []}
orbits = {}

options = set()

def retrieval_of_entity():
    global records
    tui.started("Retrieval of an entity")
    entity = None
    name = tui.entity_name()
    for i in records:
        if i['eName'] == name:
            entity = i
            break
    if entity is not None:
        tui.list_entity(entity, [])
    else:
        tui.error("Entity was not found")
    tui.completed("Retrieval of an entity")


def entity_details():
    global records
    tui.started("Retrieval of entity details")
    entity_name, column = tui.entity_details()
    entity = None
    for i in records:
        if i['eName'] == entity:
            entity = i
            break
    if entity is not None:
        tui.list_entity(entity, column)
    else:
        tui.error("Entity is not found")
    tui.completed("Retrieval of entity details")


def categorize_entity_by_type():
    global planets
    global records
    tui.started("Categorise entity by type")
    planets = {"Planets": [], "Non-planets": []}
    for e in records:
        if e['isPlanet'] == 'TRUE':
            planets['Planets'] += [e]
        else:
            planets['Non-planets'] += [e]
    tui.completed("Categorise entity by type")


def sum_by_orbit():
    global orbits
    tui.started("Summarising entities by orbit")
    entities = tui.orbits()

    for i in records:
        if i['orbits'] == entities:
            if i['orbits'] not in orbits:
                orbits[i['orbits']] = {"Small": [], "Large": []}
            radius = float(i['meanRadius'])

            if radius < 100:
                orbits[i['orbits']]['Small'] += [i]

            else:
                orbits[i['orbits']]['Large'] += [i]
    tui.completed("Summarising entities by orbit")


def cat_by_gravity():
    global planets_gravity
    global records

    tui.started("Categorizing entities by gravity")
    limits = tui.gravity_range()
    upper_limit = limits[0]
    lower_limit = limits[1]
    gravity = {"Low": [], "Medium": [], "High": []}

    for i in records:

        z = i['gravity']
        if z > upper_limit:
            planets_gravity['High'] += [i['gravity']]

        elif z < lower_limit:
            planets_gravity['Low'] += [i['gravity']]

        else:
            planets_gravity['Medium'] += [i['gravity']]
    tui.completed("Categorizing entities by gravity")

    return gravity


# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.
records = []


def run():

    # Task 19: Call the function welcome of the module tui.
    # This will display our welcome message when the program is executed.
    tui.welcome()

    while True:
        # Task 20: Using the appropriate function in the module tui, display a menu of options
        # for the different operations that can be performed on the data.
        # Assign the selected option to a suitable local variable
        menu_opt = tui.menu()


        # Task 21: Check if the user selected the option for loading data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has started.
        # - Load the data (see below).
        # - Use the appropriate function in the module tu§i to display a message to indicate that the data loading
        # operation has completed.
        #
        # To load the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve a file path for the CSV data file.  You
        # should appropriately handle the case where this is None.
        # - Read each line from the CSV file and add it to the list 'records'. You should appropriately handle the case
        # where the file cannot be found
        if menu_opt == 1:
            global records
            tui.started("Load Data")
            path = tui.source_data_path()
            if path is None:
                tui.error("No file selected")
                continue
            try:
                file = open(path, "r")
                records = csv.DictReader(file)
            except FileNotFoundError as _:
                tui.error("File not found")
                continue
            tui.completed("Load Data")

        # Task 22: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to display a menu of options for processing the data.
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an entity then
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process
        #       has started.
        #       - Use the appropriate function in the module tui to retrieve the entity name
        #       - Find the record for the specified entity in records.  You should appropriately handle the case
        #       where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve an entity's details then
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve the entity details
        #       - Find the record for the specified entity details in records.  You should appropriately handle the
        #       case where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their type then
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has started.
        #       - Iterate through each record in records and assemble a dictionary containing a list of planets
        #       and a list of non-planets.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their gravity then
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve a gravity range
        #       - Iterate through each record in records and assemble a dictionary containing lists of entities
        #       grouped into low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has completed.
        #
        #   - If the user selected the option to generate an orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       started.
        #       - Use the appropriate function in the module tui to retrieve a list of orbited planets.
        #       - Iterate through each record in records and find entities that orbit a planet in the list of
        #       orbited planets.  Assemble the found entities into a nested dictionary such that each entity can be
        #       accessed as follows:
        #           name_of_dict[planet_orbited][category]
        #       where category is "small" if the mean radius of the entity is below 100 and "large" otherwise.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       completed.
        if menu_opt == 2:
            tui.started("Processing Data")
            process_type = tui.process_type()
            if process_type is None:
                continue

            elif process_type == 1:
                retrieval_of_entity()

            elif process_type == 2:
                entity_details()

            elif process_type == 3:
                categorize_entity_by_type()

            elif process_type == 4:
                cat_by_gravity()

            elif process_type == 5:
                sum_by_orbit()

            tui.completed("Processing Data")



        # Task 23: Check if the user selected the option for visualising data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the data visualisation operation
        # has started.
        # - Visualise the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data visualisation
        # operation has completed.
        #
        # To visualise the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve the type of visualisation to display.
        # - Check what option has been selected
        #
        #   - if the user selected the option to visualise the entity type then
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing a list of planets and a list of
        #       non-planets.
        #       - Use the appropriate function in the module visual to display a pie chart for the number of planets
        #       and non-planets
        #       - Use the appropriate function in the module tui to indicate that the entity type visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the entity gravity then
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to display a bar chart for the gravities
        #       - Use the appropriate function in the module tui to indicate that the entity gravity visualisation
        #       process has completed.
        #
        #   - if the user selected the option to visualise the orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a nested dictionary of orbiting planets.
        #       - Use the appropriate function in the module visual to display subplots for the orbits
        #       - Use the appropriate function in the module tui to indicate that the orbit summary visualisation
        #       process has completed.
        #
        #   - if the user selected the option to animate the planet gravities then
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to animate the gravity.
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has completed.
        if menu_opt == 3:
            tui.started("Data Visualisation")
            visual_opts = tui.visualise()
            if visual_opts is None:
                tui.error("No such option")

            elif visual_opts == 1:
                tui.started("Visualize Entities by type")
                categorize_entity_by_type()
                visual.entities_pie(planets)
                tui.completed("Entities by type")

            elif visual_opts == 2:
                tui.started("Visualize entities by gravity")
                dict = cat_by_gravity()
                print(dict)
                visual.entities_bar(dict)
                tui.completed("Visualize entities by gravity")

            elif visual_opts == 3:
                orbited = {}
                print(orbited)
                tui.started("Visualize orbit summary")
                sum_by_orbit()
                visual.orbits(orbited)
                tui.completed("Visualize orbit summary")

            elif visual_opts == 4:
                tui.started("Animate planet gravities")
                cat_by_gravity()
                visual.gravity_animation(planets_gravity)
                tui.completed("Animate planet gravities")
            tui.completed("Data Visualisation")



        # Task 28: Check if the user selected the option for saving data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the save data operation has started.
        # - Save the data (see below)
        # - Use the appropriate function in the module tui to indicate that the save data operation has completed.
        #
        # To save the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create an AbstractWriter class with abstract methods and a concrete
        # Writer class that inherits from the AbstractWriter class.  You should then use this to write the records to
        # a JSON file using in the following order: all the planets in alphabetical order followed by non-planets 
        # in alphabetical order.
        # TODO: Your code here

        # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
        # break out of the loop
        if menu_opt == 5:
            tui.completed("The program")
            break
        # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
        # display an error message
        if menu_opt == None:
            tui.error("Invalid option. Please try again.")

if __name__ == "__main__":
    run()