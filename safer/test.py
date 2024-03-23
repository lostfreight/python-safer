# run with python3 -m safer.test

from .search import CompanySnapshot

print("Running...")
client = CompanySnapshot()

company = client.get_by_usdot_number(1597181)
print(company.to_json())
