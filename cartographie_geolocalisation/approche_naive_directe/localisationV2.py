# SNT seconde
# Thème Cartographie et localisation
#  
# Utilisation d'un fichier de coordonnées GPS
#
#(C) Stéphane Colomban 2019  (CC : by - nc - sa)

# coordonnées GPS de Paris et Marseille récupérées sur https://www.gps-longitude-latitude.net
# Fichier .csv des coordonnées des villes de France récupéré sur : https://sql.sh/736-base-donnees-villes-francaises



from tkinter import *
import csv 

#Création de l'objet Ville
class Ville:
    def __init__(self,nom,lat,lon):
        self.nom = nom
        self.lat = lat
        self.lon = lon
        
    
    def affiche(self):
        R=4
        canevas.create_oval(xx(self.lon)-R, yy(self.lat)-R, xx(self.lon)+R, yy(self.lat)+R, outline='blue', fill='blue')
        


#Deux villes de référence nécessaires aux calculs:
# latitudes et ordonnées écran
latMarseille = 43.2965
yMarseille = 657
latParis = 48.8566
yParis = 255

# longitudes et abscisses écran
lonMarseille = 5.3698
xMarseille = 585
lonParis = 2.3522
xParis = 416

# Remplissage de la liste des villes à partir du fichier .csv
villes=[]
with open("villes3.csv","r") as csvfile:
    fich = csv.reader(csvfile, delimiter=';', quotechar='"')
    
    for row in fich:
        if (eval(row[2])>20000): # on ne garde que les villes de plus de 20000 habitants
            villes.append( Ville(row[1], eval(row[5].replace(',','.')) , eval(row[4].replace(',','.')))  )
            
             


afficheCoordo=False
afficheVilles=False

def yy(lat):
    """ donne les coord écran en fonction des coord GPS"""
    return yMarseille + (yParis - yMarseille) / (latParis - latMarseille) * (lat - latMarseille)
        
def xx(lon):
    """ donne les coord écran en fonction des coord GPS"""
    return xMarseille + (xParis - xMarseille) / (lonParis - lonMarseille) * (lon - lonMarseille)


def latitude(y):
    """ donne les coord GPS en fonction des coord écran"""
    lat = latMarseille + (latParis - latMarseille) /  (yParis - yMarseille) * (y - yMarseille)
    return (int(lat * 1000) / 1000.)

def longitude(x):
    """ donne les coord GPS en fonction des coord écran"""
    lon = lonMarseille + (lonParis - lonMarseille) / (xParis - xMarseille) * (x - xMarseille)
    return (int(lon * 1000) / 1000.)



######################## INTERFACE GRAPHIQUE ################################################""

def actionBouton1():
    """ Actions du bouton 1"""
    global afficheVilles
    afficheVilles = not afficheVilles
   

def actionBouton2():
    """ Actions du bouton 2"""
    global afficheCoordo
    afficheCoordo = not afficheCoordo

def motion(event):
    """ Evénements liés à la souris """
    x=event.x
    y=event.y
    if (afficheCoordo):
        canevas.delete(ALL)
        canevas.create_image(5,85,anchor=NW, image=img)
        canevas.create_line(0,y,760,y,fill='blue')
        canevas.create_line(x,40,x,780,fill='red')
        canevas.create_text(850,200, text="latitude ="+ str(latitude(y)),fill='blue')
        canevas.create_text(850,250, text="longitude ="+ str(longitude(x)),fill='red')
        
    if (afficheVilles):
        R=5
        for no in range(len(villes)):
            villes[no].affiche();
     

##################################### 
# Création de l'interface graphique #
##################################### 
# Création de la fenêtre principale 
root = Tk()
root.title('Cartographie - SNT 2019')


# Création d'un widget Canvas (zone graphique contenant le fond de carte)
LARGEUR = 950
HAUTEUR = 800
canevas = Canvas(root, width = LARGEUR, height = HAUTEUR, bg ='white')
img = PhotoImage(file="fond_FRANCE.png")
canevas.create_image(5,85,anchor=NW, image=img)
canevas.pack(padx =5, pady =5)



# Création d'un widget Button (bouton 1)
bouton1 = Button(root, text ='Bouton1 : Affichage des villes principales', command = actionBouton1)
bouton1.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton 2)
bouton2 = Button(root, text ='Bouton2 : Affichage des coordonnées GPS', command = actionBouton2)
bouton2.pack(side = LEFT, padx = 5, pady = 5)


# Mise à jour de l'interface
root.bind('<Motion>', motion)
root.mainloop()