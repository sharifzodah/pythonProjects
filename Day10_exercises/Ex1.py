try:
    total_value = float(input("Enter total value you have: "))
    value = float(input("Enter value you want to spend: "))

    percentage = value / total_value * 100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run program again.")
except ZeroDivisionError:
    print("Values cannot be zero")
