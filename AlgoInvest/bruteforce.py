import time


def get_actions(file):
    """ Open and read the file with data.
    Save each line of data in a tuple and add the tuple in a list
    """
    with open(file, "r") as f:
        content = f.readlines()
        del content[0]
        list_actions = []
        for i in range(len(content)):
            action = content[i].split(",")
            list_actions.append((action[0], int(round(float(action[1])*100, 2)), float(action[2][:-1])/100))
    return list_actions


def best_investment(amount_available, list_actions: list, selected_actions=[]):
    """ test all possibilities of investment in list_actions with a max amount and select the best"""
    global count
    count += 1
    # condition to recursive function
    if list_actions:
        benefit1, selected_actions1 = best_investment(amount_available, list_actions[1:], selected_actions)
        action = list_actions[0]
        if action[1] <= amount_available:
            benefit2, selected_actions2 = best_investment(amount_available-action[1],
                                                          list_actions[1:], selected_actions + [action])
            if benefit1 < benefit2:
                return benefit2, selected_actions2
        return benefit1, selected_actions1
    else:
        return sum([action[2]*action[1] for action in selected_actions]), selected_actions


if __name__ == '__main__':
    count = 0
    start = time.time()
    actions = get_actions("actions.csv")
    # actions = get_actions("dataset1_Python+P7-1.csv")
    benefit, selected_actions = best_investment(50000, actions)
    price = sum([action[1] for action in selected_actions])
    print(f"Cost = {price} euros. \n List actions:")
    for action in selected_actions:
        print(f"{action[0]}: profit = {action[1]*action[2]}")
    print(f"Benefit: {benefit/100}")
    end = time.time()
    print(f"time: {end - start}")
    print(f"number of use of function: {count}")
