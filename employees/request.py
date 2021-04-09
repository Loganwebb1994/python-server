EMPLOYEES = [
  {
      "id": 1,
      "name": "Emma Beaton",
      "locationId": 3
    },
    {
      "id": 2,
      "name": "Sarah Parks",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Erick Bachman",
      "locationId": 2
    },
    {
      "id": 4,
      "name": "Bill Murray",
      "locationId": 2
    }
]


def get_all_employees():
  return EMPLOYEES

def get_single_employee(id):
  requested_employee = None

  for employee in EMPLOYEES:
    if employee["id"] == id:
      requested_employee = employee

  return requested_employee

def create_employee(employee):
    # Get the id value of the last animal in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee