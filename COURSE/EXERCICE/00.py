# Ecrire une fonction qui permet
# 	De prendre en parametre
# 		Une URL
# 		La methode HTTP
# 		Les paramètres supplémentaires
# 	Et retourne le type de format requis.
# 		A vous de voir si le format serait
# 			Un paramètre d'entrée ou non.
# 	Libre à chacun de soit implémenter:
# 		Une fonction
# 		Ou une classe

import requests


def requete(url="https://api.github.com/", methode="get", params=dict(), format="json"):
    response = None
    match methode:
        case "get":
            response = requests.get(url, params=params)
        case "post":
            response = requests.get(url, data=params)
        case "put":
            response = requests.put(url, data=params)
        case "patch":
            response = requests.patch(url, data=params)
        case "delete":
            response = requests.delete(url, data=params)           
            
    if format == "text":
        return response.text
    else:
        return response.json()
            
            
            
print(requete(url="https://api.github.com/", methode="get", format="json"))