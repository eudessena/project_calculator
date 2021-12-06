match user:
    case User(admin=False, region=Region.EUROPE):
        print("European customer")
    case User(admin=False):
        print("Other customer")
    case User(admin=True):
        print("Admin user")
    case _:
        print("Error: Not a user!")