# SNT seconde
# Thème Cartographie et localisation
#  
# Utilisation d'un fichier de coordonnées GPS
#
#(C) Stéphane Colomban 2019  (CC : by - nc - sa)

# coordonnées GPS de Paris et Marseille récupérées sur https://www.gps-longitude-latitude.net
# Fichier .csv des coordonnées des villes de France récupéré sur : https://sql.sh/736-base-donnees-villes-francaises



from tkinter import *


afficheCoordo=True



######################## INTERFACE GRAPHIQUE ################################################""


def motion(event):
    """ Evénements liés à la souris """
    x=event.x
    y=event.y
    if (afficheCoordo):
        canevas.delete(ALL)
        canevas.create_image(10,85,anchor=NW, image=img)
        canevas.create_line(0,y,850,y,fill='blue')
        canevas.create_line(x,40,x,800,fill='red')
        canevas.create_text(850,200, text="abscisse  x ="+ str(x),fill='blue')
        canevas.create_text(850,230, text="ordonnée  y ="+ str(y),fill='red')

        


 
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