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