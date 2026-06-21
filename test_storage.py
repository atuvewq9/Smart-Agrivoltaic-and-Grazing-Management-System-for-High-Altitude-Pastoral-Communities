from storage import get_animals, get_health_reports


print("Animals:")

for a in get_animals():
    print(a)


print("\nHealth:")

for h in get_health_reports():
    print(h)