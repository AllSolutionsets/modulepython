# Module des taches
def ajouter_tache():
    taches=[]
    print("#####Entrer vos taches####################")
    dt=input("Entrer la date\n")
    ecrire_fichier(dt)

    while True:
        
        tache=input("Entrer la tache\n")
       
        if tache=="q":
            break
        elif tache=="n":
            dt=input("Entrer la date\n")
            ecrire_fichier(dt)
        
        else:
            ecrire_fichier(tache)
            taches.append(tache)
            print("#Taches ajouté avec succès\n")
         
    return taches


def ecrire_fichier(element):
     with open("taches.txt","a") as f:
                f.write(f"{element}\n")


def afficher_tache(taches):
    for i, tache in enumerate(taches,10):
        print(f"{i}. {tache}")
