# animals_web_generator.py
import data_fetcher


def read_template(file_path):
    with open(file_path, "r") as handle:
        return handle.read()


def serialize_animal(animal):
    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal.get("name", "Unknown")}</div>\n'
    output += '  <p class="card__text">\n'
    output += '    <ul class="animal-details">\n'

    characteristics = animal.get('characteristics', {})

    diet = characteristics.get('diet')
    if diet:
        output += f'      <li class="animal-detail"><strong>Diet:</strong> {diet}</li>\n'

    locations = animal.get('locations')
    if locations:
        output += f'      <li class="animal-detail"><strong>Location:</strong> {", ".join(locations)}</li>\n'

    animal_type = characteristics.get('type')
    if animal_type:
        output += f'      <li class="animal-detail"><strong>Type:</strong> {animal_type}</li>\n'

    lifespan = characteristics.get('lifespan')
    if lifespan:
        output += f'      <li class="animal-detail"><strong>Lifespan:</strong> {lifespan}</li>\n'

    weight = characteristics.get('weight')
    if weight:
        output += f'      <li class="animal-detail"><strong>Weight:</strong> {weight}</li>\n'

    length = characteristics.get('length')
    if length:
        output += f'      <li class="animal-detail"><strong>Length:</strong> {length}</li>\n'

    output += '    </ul>\n'
    output += '  </p>\n'
    output += '</li>\n'

    return output


def generate_animal_info(data):
    return ''.join(serialize_animal(animal) for animal in data)


def create_html(template, animal_info):
    return template.replace('__REPLACE_ANIMALS_INFO__', animal_info)


def write_html(file_path, content):
    with open(file_path, "w") as handle:
        handle.write(content)


def main():
    # Ask for animal name
    animal_name = input("Please enter an animal: ").strip()

    # Fetch from API (via data_fetcher)
    animals_data = data_fetcher.fetch_data(animal_name)

    # Read HTML template
    template = read_template('animals_template.html')

    if animals_data:
        animal_info = generate_animal_info(animals_data)
    else:
        animal_info = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

    # Create HTML & save
    new_html_content = create_html(template, animal_info)
    write_html('animals.html', new_html_content)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
