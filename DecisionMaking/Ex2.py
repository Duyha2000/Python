color = input("Enter color: ")
match color:
    case "red":
        print("Color is red")
    case "green":
        print("Color is green")
    case "blue":
        print("Color is blue")
    case _:
        print("Color is not red, green or blue")
