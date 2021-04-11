CUSTOMERS = [
    {
      "email": "loganwebb1994@gmail.com",
      "name": "Logan Webb",
      "id": 1
    },
    {
      "email": "bobo123@bobo.com",
      "name": "Bo Bo",
      "id": 2
    },
    {
      "email": "cooter@dumdum.com",
      "name": "Cooter Brown",
      "id": 3
    },
    {
      "email": "dorfyboi69@norfdorf.com",
      "name": "Dorf McDonald",
      "id": 4
    }
  ]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    # Initial -1 value for animal index, in case one isn't found
    customer_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the animal. Store the current index.
            customer_index = index

    # If the animal was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)