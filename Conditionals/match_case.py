# YouTube Video Link: https://youtu.be/au8DpI4rr_I

blood_group = input("Enter blood group(A/B/AB/O): ")
match blood_group:
    case "A":
        print("Group A can donate blood to A and AB")
    case "B":
        print("Group B can donate blood to B and AB")
    case "AB":
        print("Group AB can donate to other AB’s but can receive from all others.")
    case "O":
        print("Group O can donate red blood cells to anybody. It’s the universal donor.")
    case _:
        print("Not a valid blood group")

# The pipe symbol | or "or" can be used to combine multiple conditions if the code following them are same.

error_code = int(input("Error code: "))
match error_code:
    case 400 | 401 | 402:
        print("Bad Request")
    case _:
        print("Processing")

marks = int(input("Enter marks: "))
match marks:
    case marks if marks < 0 or marks > 100:
        print("Not a valid marks")
    case marks if marks > 80:
        print("A")
    case marks if marks > 60:
        print("B")
    case marks if marks > 40:
        print("C")
    case _:
        print("Fail")