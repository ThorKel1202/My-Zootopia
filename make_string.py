import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def make_string():
    animals_data = load_data("animals_data.json")
    output = ''
    for animal in animals_data:
        output += '<li class="cards__item">'
        name_value = animal.get("name")
        if name_value:
            output += f"\nName: {name_value}<br/>\n"
        
        diet_value = animal.get("characteristics", {}).get("diet", "")
        if diet_value:
            output += f"Diet: {diet_value}<br/>\n"
        
        locations_value = animal.get("locations", [])
        if locations_value:
            output += f"Location: {locations_value[0]}<br/>\n"
        
        type_value = animal.get("characteristics", {}).get("type", "")
        if type_value:
            output += f"Type: {type_value}<br/>\n"
        output += '</li>\n'
            
    return output
            
print(make_string())