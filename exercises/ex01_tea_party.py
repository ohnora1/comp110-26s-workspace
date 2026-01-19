"""Tea Party planning exercise with multiple small functions."""

__author__: str = "730671005"


# defining a main planner to bring all functions together
def main_planner(guests: int) -> None:
    """calling functions below to return all values in a concise way"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # need number of guests = people
    print("Tea bags: " + str(tea_bags(people=guests)) + "")
    print("Treats: " + str(treats(guests)) + "")
    # have to call upon tea_bags and treat_count for cost
    print(
        "Cost: "
        + str(cost(tea_count=(tea_bags(people=guests)), treat_count=(treats(guests))))
        + ""
    )


# defining the tea bag function
def tea_bags(people: int) -> int:
    """determining the number of tea bags needed based on guests"""
    return people * 2


# defining the treats function
def treats(people: int) -> int:
    """determining the number of treats needed based on # of guests"""
    # call to tea_bags function
    # multiply by 1.5 since we are calling # of tea bags
    # guests want 1.5 treats per tea bag
    return int(tea_bags(people) * (1.5))


# defining the cost function
def cost(tea_count: int, treat_count: int) -> float:
    """defining function to determine cost of the tea party"""
    # return of cost given number of tea bags and number of treats
    return float((tea_count * 0.50) + (treat_count * 0.75))


# actually makes the program run
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
