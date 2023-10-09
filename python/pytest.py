class Produit:
    def __init__(self,reference,designation,prix_achat,prix_vente):
        self.reference = reference
        self.designation = designation
        self.prix_achat = prix_achat
        self.prix_vente = prix_vente
        self.stock_quantite = 0
        self.nombre_explaires = 0

    def get_nombre_produit(self):
        return self.quantite_explaires
    
    def afficher_information(self):
        print(f"Reference: {self.reference}")
        print(f"Designation: {self.designation}")
        print(f"Prix d'achat: {self.prix_achat}")
        print(f"Prix de vente: {self.prix_vente}")
        print(f"Quantite: {self.stock_quantite}")

    def modifier_prix_achat(self,nouveau_prix_vente):
        self.prix_achat = nouveau_prix_vente

    def modifier_prix_vente(self,nouveau_prix_vente):
        self.prix_vente = nouveau_prix_vente

    def ajouter_stock(self,quantite):
        self.stock_quantite += quantite
        self.nombre_explaires += quantite

    def retirer_stock(self,quantite):
        if self.stock_quantite >= quantite:
            self.stock_quantite -= quantite
            self.nombre_explaires -= quantite
        else:
            print("Quantite insuffisante en stock.")

class Commande:
    def __init__(self,date_creation):
        self.date_creation = date_creation
        self.produits_commandes = []

    def ajouter_produit(self,produit,quantite):
        self.produits_commandes.append((produit,quantite))

    def afficher_commande(self):
        print(f"Date de creation: {self.date_creation}")
        print("Produits commandes:")
        for produit,quantite in self.produits_commandes:
            print(f"Produit: {produit.reference} - Quantite: {quantite}")

produit1 = Produit("REF1","Produit 1",100,150)
produit2 = Produit("REF2","Produit 2",200,250)

commande1 = Commande("01/01/2021")
commande1.ajouter_produit(produit1,10)
commande1.ajouter_produit(produit2,5)

produit1.afficher_information()
commande1.afficher_commande()