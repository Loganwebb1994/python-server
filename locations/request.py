LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "666 Emory Drive"
    },
    {
      "name": "Nashville East",
      "address": "123 puppy way",
      "id": 3
    },
    {
      "name": "Nashville West",
      "address": "1234 Puppy Way",
      "id": 4
    }
  ]

def get_all_locations():
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location

def create_location(location):
    # Get the id value of the last animal in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    location["id"] = new_id

    # Add the animal dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location

def delete_location(id):
    # Initial -1 value for location index, in case one isn't found
    location_index = -1

    # Iterate the locationS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)