# SNT seconde
# Thème Cartographie et localisation
#  
# Utilisation d'un fichier de coordonnées GPS
#
#(C) Stéphane Colomban 2019  (CC : by - nc - sa)

# coordonnées GPS de Paris et Marseille récupérées sur https://www.gps-longitude-latitude.net
# Fichier .csv des coordonnées des villes de France récupéré sur : https://sql.sh/736-base-donnees-villes-francaises



from tkinter import *



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



afficheCoordo=True

## Calcul des coordonnées GPS à l'aide des coodonnées (x;y)
## Compléter les lignes latitudes = ...... et longitudes = ......
def g(y):
    """ donne les coord GPS en fonction des coord écran"""
    latitude = 0
    #Corrigé :     latitude = latMarseille + (latParis - latMarseille) /  (yParis - yMarseille) * (y - yMarseille)
    return (int(latitude * 1000) / 1000.)

def f(x):
    """ donne les coord GPS en fonction des coord écran"""
    longitude = 0
    #Corrigé : longitude = lonMarseille + (lonParis - lonMarseille) / (xParis - xMarseille) * (x - xMarseille)
    return (int(longitude * 1000) / 1000.)



######################## INTERFACE GRAPHIQUE ################################################""


def motion(event):
    """ Evénements liés à la souris """
    x=event.x
    y=event.y
    if (afficheCoordo):
        canevas.delete(ALL)
        canevas.create_image(10,85,anchor=NW, image=img)
        canevas.create_line(0,y,760,y,fill='blue')
        canevas.create_line(x,40,x,780,fill='red')
        canevas.create_text(850,200, text="x ="+ str(x),fill='red')
        canevas.create_text(850,230, text="y ="+ str(y),fill='blue')
        canevas.create_text(850,300, text="longitude ="+ str(f(x)),fill='red')
        canevas.create_text(850,330, text="latitude ="+ str(g(y)),fill='blue')
     

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




# Mise à jour de l'interface
root.bind('<Motion>', motion)
root.mainloop()