# Dictionary to identify which letters are touching each other
dictionary = {
    'a' : ['a','b','c','e'],
    'b' : ['a','b','c','d'],
    'c' : ['a','b','c','d','e','f'],
    'd' : ['f','d','c','b'],
    'e' : ['a','e','c','f'],
    'f' : ['e','f','c','d']
     }


#Main function
def find_touching_blocks(dict):
    #instanciating object to return
    colors = {
        "red" : [], 
        "green" : [],
        "blue" : [],
        "yellow" : []
        }
    
    #Loop through the dictionary.
        #The logic behind this is that if two letters both don't touch a singular letter, they must be touching, so if this happens, it will send it to the alternating color.  If the length is equal to the dictionary then it touches everything, it requires its own color.  The remmaining shape will also receive its own color.
    for key in dict:
        if 'a' not in dict[key]:

            if len(colors["green"]) > 0:
                colors["blue"].append(key)            
            else:
                colors["green"].append(key)

        elif 'd' not in dict[key]:

            if len(colors["blue"]) > 0:
                colors["green"].append(key) 
            else: 
                colors["blue"].append(key)

        elif len(dict[key]) == len(dict):
            colors["red"].append(key)

        else:
            colors["yellow"].append(key)

    return colors
    
find_touching_blocks(dictionary)