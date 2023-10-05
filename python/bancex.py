import csv
import random

admin_password = "9761"
data = "base.csv"
# dictionary
clients = {}
comptes = {}
clientscomptes = {}

# fonction lambda
gener_compte_num = lambda client_number: f"{client_number}{random.randint(10, 99)}"

# fonction
def ajouter_compte(MPC, SoldeC):
    client_number = len(clients) + 1
    account_number = gener_compte_num(client_number)
    clients[account_number] = MPC
    comptes[account_number] = SoldeC
    clientscomptes[account_number] = client_number
    print(f"Client créé avec succès. Numero de compte : {account_number}, Numero de client : {client_number}, Code secret : {MPC}")

def supprimer_compte(numC):
    if numC in clients:
        del clients[numC]
        del comptes[numC]
        del clientscomptes[numC]
        print(f"Client avec numero de compte {numC} supprimé avec succès.")
    else:
        print("Client non trouvé.")

def modifie_motdepass(account_number, old_password, new_password):
    if account_number in clients:
        if clients[account_number] == old_password:
            clients[account_number] = new_password
            print("Mot de passe modifié avec succès.")
        else:
            print("Ancien mot de passe incorrect.")
    else:
        print("Client non trouvé.")

def afficher_sold(account_number):
    if account_number in comptes:
        print(f"Solde du compte : {comptes[account_number]}")
    else:
        print("Client non trouvé.")

def deposer_solde(account_number, amount):
    if account_number in comptes:
        comptes[account_number] += amount
        print("Dépôt réussi.")
    else:
        print("Client non trouvé.")

def retirer_solde(account_number, amount):
    if account_number in comptes:
        if comptes[account_number] >= amount:
            comptes[account_number] -= amount
            print("Retrait réussi.")
        else:
            print("Solde insuffisant.")
    else:
        print("Client non trouvé.")

def sauvegarder_donnees():
    with open(data, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Numero de compte", "Code secret", "Solde du compte", "Numero de client"])
        for account_number in clients:
            writer.writerow([account_number, clients[account_number], comptes[account_number], clientscomptes[account_number]])
    print("Données sauvegardées avec succès.")

# Function to load client data from a CSV file
def charger_donnees():
    try:
        with open(data, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                account_number = row["Numero de compte"]
                MPC = row["Code secret"]
                SoldeC = float(row["Solde du compte"])
                clients[account_number] = MPC
                comptes[account_number] = SoldeC
                clientscomptes[account_number] = int(row["Numero de client"])
    except FileNotFoundError:
        pass

                


charger_donnees()

while True:
    print("\nMenu principal:")
    print("1. Admin")
    print("2. Client")
    print("3. Quitter")
    choice = input("Entrez votre choix : ")

    if choice == "1":
        admin_password_input = input("Entrez votre mot de passe: ")
        if admin_password_input == admin_password:
            while True:
                print("\nMenu Admin:")
                print("1. Ajouter un compte")
                print("2. Supprimer un compte")
                print("3. Déconnexion")
                admin_choice = input("Entrez votre choix : ")
                if admin_choice == "1":
                    MPC = input("Entrez le code secret du nouveau client : ")
                    SoldeC = float(input("Entrez le solde initial du nouveau client : "))
                    ajouter_compte(MPC, SoldeC)
                elif admin_choice == "2":
                    numC = input("Entrez le numero de compte du client : ")
                    supprimer_compte(numC)
                elif admin_choice == "3":
                    sauvegarder_donnees()
                    break
                else:
                    print("Choix invalide.")
        else:
            print("Mot de passe administrateur incorrect.")
    elif choice == "2":
        print("\nConnexion Client:")
        account_number = input("Entrez votre numero de compte : ")
        password = input("Entrez votre code secret : ")
        if account_number in clients and clients[account_number] == password:
            print("Connexion réussie.")
            while True:
                print("\nMenu Client:")
                print("1. Modifier le mot de passe")
                print("2. Afficher le solde")
                print("3. Déposer de l'argent")
                print("4. Retirer de l'argent")
                print("5. Déconnexion")
                client_choice = input("Entrez votre choix : ")
                if client_choice == "1":
                    old_password_input = input("Entrez votre ancien mot de passe : ")
                    if old_password_input != clients[account_number]:
                        print("Ancien mot de passe incorrect.")
                        continue
                    new_password = input("Entrez votre nouveau mot de passe : ")
                    modifie_motdepass(account_number, password, new_password)
                elif client_choice == "2":
                    afficher_sold(account_number)
                elif client_choice == "3":
                    amount = float(input("Entrez le montant à déposer : "))
                    deposer_solde(account_number, amount)
                elif client_choice == "4":
                    amount = float(input("Entrez le montant à retirer : "))
                    retirer_solde(account_number, amount)
                elif client_choice == "5":
                    sauvegarder_donnees()
                    break
                else:
                    print("Choix invalide.")
        else:
            print("Numero de compte ou mot de passe incorrect.")
    elif choice == "3":
        sauvegarder_donnees()
        break
    else:
        print("Choix invalide. Veuillez choisir 1, 2 ou 3.")
