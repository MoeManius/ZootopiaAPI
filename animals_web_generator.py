import json
import requests

# Define the API URL and the API key for authentication.
API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "LbD4Qz8+n3gfj9EewEpOeQ==CEMXLav2jdtFYlXA"


def fetch_animal_data(animal_name):
    """Fetches animal data from the API based on the provided animal name."""
    headers = {"X-Api-Key": API_KEY}  # Set the API key in the headers for authentication.
    params = {"name": animal_name}  # Include the required 'name' parameter.
    response = requests.get(API_URL, headers=headers, params=params)  # Send a GET request to the API with parameters.

    # Check if the API response is successful.
    if response.status_code == 200:
        return response.json()  # Parse and return the JSON data.
    else:
        # Print an error message and exit if the API call fails.
        print(f"Error: Unable to fetch data from API. Status code: {response.status_code}")
        exit(1)


def read_template(file_path):
    """Reads the HTML template file."""
    with open(file_path, "r") as handle:  # Open the file in read mode.
        return handle.read()  # Return the file content as a string.


def serialize_animal(animal):
    """Serializes a single animal object into an HTML list item."""
    output = '<li class="cards__item">\n'  # Start the list item HTML.
    output += f'  <div class="card__title">{animal.get("name", "Unknown")}</div>\n'  # Add the animal's name.
    output += '  <p class="card__text">\n'  # Start the paragraph for details.
    output += '    <ul class="animal-details">\n'  # Start the details list.

    # Extract characteristics from the animal data.
    characteristics = animal.get('characteristics', {})

    # Add the diet to the HTML if available.
    diet = characteristics.get('diet')
    if diet:
        output += f'      <li class="animal-detail"><strong>Diet:</strong> {diet}</li>\n'

    # Add the locations to the HTML if available.
    locations = animal.get('locations')
    if locations:
        output += f'      <li class="animal-detail"><strong>Location:</strong> {", ".join(locations)}</li>\n'

    # Add the type to the HTML if available.
    animal_type = characteristics.get('type')
    if animal_type:
        output += f'      <li class="animal-detail"><strong>Type:</strong> {animal_type}</li>\n'

    # Add the lifespan to the HTML if available.
    lifespan = characteristics.get('lifespan')
    if lifespan:
        output += f'      <li class="animal-detail"><strong>Lifespan:</strong> {lifespan}</li>\n'

    # Add the weight to the HTML if available.
    weight = characteristics.get('weight')
    if weight:
        output += f'      <li class="animal-detail"><strong>Weight:</strong> {weight}</li>\n'

    # Add the length to the HTML if available.
    length = characteristics.get('length')
    if length:
        output += f'      <li class="animal-detail"><strong>Length:</strong> {length}</li>\n'

    output += '    </ul>\n'  # Close the details list.
    output += '  </p>\n'  # Close the paragraph.
    output += '</li>\n'  # Close the list item.

    return output  # Return the serialized HTML for the animal.


def generate_animal_info(data):
    """Generates a string with the animal data in HTML format."""
    # Iterate over each animal and serialize it into HTML, then join the results into a single string.
    return ''.join(serialize_animal(animal) for animal in data)


def create_html(template, animal_info):
    """Replaces the placeholder in the template with the animal info."""
    # Replace the placeholder with the generated animal info HTML.
    return template.replace('__REPLACE_ANIMALS_INFO__', animal_info)


def write_html(file_path, content):
    """Writes the content to a new HTML file."""
    with open(file_path, "w") as handle:  # Open the file in write mode.
        handle.write(content)  # Write the content to the file.


def main():
    # Ask the user for an animal name to search for.
    animal_name = input("Enter the name of the animal to fetch information: ")

    # Fetch the animal data from the API based on the user's input.
    animals_data = fetch_animal_data(animal_name)

    # Read the HTML template file.
    template = read_template('animals_template.html')

    # Generate animal info string in HTML format.
    animal_info = generate_animal_info(animals_data)

    # Create the new HTML content by inserting the animal info into the template.
    new_html_content = create_html(template, animal_info)

    # Write the new HTML content to a file.
    write_html('animals.html', new_html_content)

    # Notify the user that the HTML file has been generated.
    print("HTML file generated with data from the API.")


if __name__ == "__main__":
    main()  # Execute the main function.
