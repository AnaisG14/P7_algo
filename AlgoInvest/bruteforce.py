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
            list_actions.append((action[0], int(action[1])*100, int(action[2][:-2])/100))
    return list_actions

count = 0

def best_investment(amount_available, list_actions: list, selected_actions=[]):
    """ test all possibilities of investment in list_actions with a max amount and select the best"""
    global count
    count += 1
    # condition to recursive fonction
    if list_actions:
        price_to_compare1, selected_actions1 = best_investment(amount_available, list_actions[1:], selected_actions)
        action = list_actions[0]
        if action[1] <= amount_available:
            price_to_compare2, selected_actions2 = best_investment(amount_available-action[1],
                                                                   list_actions[1:], selected_actions + [action])
            if price_to_compare1 < price_to_compare2:
                return price_to_compare2, selected_actions2
        return price_to_compare1, selected_actions1
    else:
        return sum([action[2]*action[1] for action in selected_actions]), selected_actions


if __name__ == '__main__':
    start = time.time()
    actions = get_actions("actions.csv")
    benefice, selected_actions = best_investment(50000, actions)
    price = sum([action[1] for action in selected_actions])
    print(f"Vous dépensez {price} euros pour les actions suivantes:")
    for action in selected_actions:
        print(f"{action[0]}: profit = {action[1]*action[2]}")
    print(f"Bénéfices: {benefice/100}")
    end = time.time()
    print(f"temps d'execution: {end - start}")
    print(f"nombre d'utilisation de la fonction: {count}")

