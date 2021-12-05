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


def best_investment(amount_available, list_actions: list, selected_actions=[]):
    """ selected the best investment in list_actions with a max amount """
    # trier la liste d'action de la plus chère à la moins chère
    list_actions.sort(key=lambda action: action[1], reverse=True)

    # création d'une matrice sous forme d'une liste de (j = len(list_actions)+1) listes.
    # chaque sous liste sera de longueur i = amount_available+1.
    # si l'action est ajoutée, on ajoute la valeur de l'action à la sous-liste sinon on ajoute 0
    matrice = []
    for j in range(len(list_actions)+1):
        matrice.append([])

    # remplissage de la 1ère ligne pour si aucune action:
    for i in range(amount_available+1):
        matrice[0].append(0)

    # 2è ligne et suivante:
    # boucle sur la liste d'actions
    j = 0
    for action in list_actions:
        j += 1
        # boucle sur les valeurs à tester
        for i in range(amount_available+1):
            # vérifier si la valeur de l'action  est supérieure à la valeur test et mettre 0
            if action[1] > i:
                matrice[j].append(0)
            else:
                # vérifier s'il y a déjà une action dans le portefeuille, si non ajouter la valeur de l'action
                if matrice[j-1][i] == 0:
                    matrice[j].append(action[2]*action[1])
                else:
                    # vérifier s'il est possible d'ajouter l'action et comparer avec les actions déjà présentes
                    matrice[j].append(max((action[2]*action[1])+(matrice[j-1][i-action[1]]), matrice[j-1][i]))

    # lecture de la matrice pour retrouver les élémnets sélectionnés
    # boucle depuis la dernière action testée jusqu'à ce que le montant disponible soit de 0
    i = amount_available
    while i:
        j = len(list_actions)
        for action in list_actions[::-1]:
            test1 = matrice[j][i]
            test2 = matrice[j-1][i]

            if matrice[j][i] <= matrice[j - 1][i]:
                # ne pas sélectionner l'action
                j -= 1      # passer à l'action précédente
            else:
                selected_actions.append(action)     # ajouter l'action
                j -= 1      # passer à l'action précédente
                i -= action[1]      # soustraire le prix de l'action au montant disponible
        i = 0
    return matrice[-1][-1], selected_actions


if __name__ == '__main__':
    start = time.time()
    # actions = get_actions("actions.csv")
    actions = get_actions("dataset1_Python+P7-1.csv")
    benefice, selected_actions = best_investment(50000, actions)
    price = 0
    for action in selected_actions:
        price += action[1]
    print(f"Vous dépensez {price} euros pour les actions suivantes:")
    for action in selected_actions:
        print(f"{action[0]}: profit = {action[1]*action[2]}")
    print(f"Bénéfices: {benefice/100}")
    end = time.time()
    print(f"temps d'execution: {end - start}")


