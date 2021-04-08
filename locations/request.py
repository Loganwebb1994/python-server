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