def day_of_week():
    day = input("Enter a day of the week: ").lower()

    match day:
        case "monday":
            print("Start of the work week!")
        case "tuesday":
            print("It's Tuesday, keep going!")
        case "wednesday":
            print("We're halfway there!")
        case "thursday":
            print("Almost the weekend!")
        case "friday":
            print("Last day of the work week!")
        case "saturday":
            print("Enjoy your weekend!")
        case "sunday":
            print("Prepare for the upcoming week!")
        case _:
            print("That's not a valid day of the week.")

if __name__ == "__main__":
    day_of_week()
