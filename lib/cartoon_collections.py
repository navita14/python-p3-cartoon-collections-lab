def roll_call_dwarves(dwarves):
    for idx, name in enumerate(dwarves, start = 1):
        print(f"{idx}. {name}")

def summon_captain_planet(planeteer_calls):
    new_list = []
    for name in planeteer_calls:
        new_list.append(name.capitalize() + "!")
    return new_list

def long_planeteer_calls(calls):
    if len(calls) > 4:
        return True
    else:
        return False

def find_the_cheese(snacks):
    cheese_list = ("cheddar", "gouda","camembert")
    for cheese in snacks:
        if cheese in cheese_list:
            return cheese
    return None

