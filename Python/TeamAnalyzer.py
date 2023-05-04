import sqlite3
import sys

# This helps with command-line parameters
connection = sqlite3.connect('../pokemon.sqlite')
cursor = connection.cursor()

# All the "against" column suffixes:
types = ["bug", "dark", "dragon", "electric", "fairy", "fight",
    "fire", "flying", "ghost", "grass", "ground", "ice", "normal",
    "poison", "psychic", "rock", "steel", "water"]

# Take six parameters on the command-line
if len(sys.argv) < 6:
    print("You must give me six Pokemon to analyze!")
    sys.exit()

team = []
for i, arg in enumerate(sys.argv):
    if i == 0:
        continue

# Analyze the pokemon whose pokedex_number is in "arg"

    #Getting the list of names
    name = "SELECT name FROM pokemon WHERE pokedex_number = " + arg
    p_name = cursor.execute(name).fetchone()
    n_name =(str(p_name)[1:-1])

    #Getting the list of types
    type12 = "SELECT type1, type2 FROM pokemon_types_view WHERE name = '" + p_name[0] + "'"
    tp = cursor.execute(type12).fetchall()
    p_tp = tp[0]
    type1 = p_tp[0]
    type2 = p_tp[1]
     #Get the list of against values
    against_values = """SELECT against_bug, against_dark, against_dragon, against_electric,against_fairy,
                      against_fight,against_fire, against_flying, against_ghost, against_grass, against_ground,
                      against_ice, against_normal, against_poison, against_psychic,against_rock, against_steel,
                     against_water FROM pokemon_types_battle_view WHERE type1name = '""" + type1 + "' AND type2name = '" + type2 + "'"
    ag = cursor.execute(against_values).fetchall()
    # You will need to write the SQL, extract the results, and compare
    # Remember to look at those "against_NNN" column values; greater than 1
    # means the Pokemon is strong against that type, and less than 1 means
    # the Pokemon is weak against that type

    # Put the strong_against and weak_against list and evaluate them

    strong_against = []
    weak_against = []
    type_dict = dict(enumerate(types))

    for i in range(len(ag[0])):
        if ag[0][i] > 1.0:
            strong_against.append(type_dict[i])
        elif ag[0][i] < 1.0:
            weak_against.append(type_dict[i])

    print(f"{n_name} ({type1} {type2}) is strong against {strong_against} but weak against {weak_against}")


#answer = input("Would you like to save this team? (Y)es or (N)o: ")

#if answer.upper() == "Y" or answer.upper() == "YES":
#       teamName = input("Enter the team name: ")

    #Write the pokemon team to the "teams" table
#print("Saving " + teamName + " ...")
#else:
#print("Bye for now!")

