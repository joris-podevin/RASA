# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

"""

class ActionSchedule(Action):

     def name(self) -> Text:
         return "action_schedule"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
           room = tracker.get_slot('room')
           res = requests.get('http://10.104.22.124:8085/cours/getBySalle/c138')
           res.text
           testJson = json.loads(res.text)
           jsonList = []
           cpt=0
           while (cpt<len(testJson)):
                      matiere = testJson[cpt]["matiere"]	
                      jsonList.append(matiere)
                      print(jsonList)
                      cpt+=1
           cpt=0
           reponse = "les prochains cours sont : "
           while(cpt<len(jsonList)):
                      reponse += jsonList[cpt]
                      reponse += ", "
                      print (reponse)
                      cpt+=1
           reponse +=  room
           dispatcher.utter_message(text=reponse)
	
           return []

"""


class ActionSchedule(Action):

     def name(self) -> Text:
         return "action_schedule"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
           section = tracker.get_slot('section')
           groupe = tracker.get_slot('group')
           requete = "http://10.104.22.124:8085/cours/getCours/"+groupe+"/"+section+"/"+"2023-11-16T08:00:00"
           print (requete)
           res = requests.get(requete)
           res.text
           jsonRequest = json.loads(res.text)
           jsonList=[]
           cpt = 0
           reponse = "les cours d'aujourd'hui sont : "
           while (cpt<len(jsonRequest)):
                      reponse += jsonRequest[cpt]["matiere"]
                      reponse += " de "
                      debut = jsonRequest[cpt]["dateDebut"]
                      fin = jsonRequest[cpt]["dateFin"]
                      reponse += debut[11:13] + " heure " + debut[14:16] + " a " + fin[11:13] + " heure " + fin[14:16]
                      reponse += " en salle " + jsonRequest[cpt]["salle"]
                      reponse+=" "
                      cpt+=1
           dispatcher.utter_message(text=reponse)
	
           return []



class ActionRoom(Action):

     def name(self) -> Text:
         return "action_room"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

           dispatcher.utter_message(text="/EXAMPLE/ la salle est libre")
	
           return []

class ActionAllRooms(Action):

     def name(self) -> Text:
         return "action_all_rooms"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

           dispatcher.utter_message(text="/EXAMPLE/ les salles A B C sont libres")
	
           return []
           
           
           
class ActionContact(Action):

     def name(self) -> Text:
         return "action_contact"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

           dispatcher.utter_message(text="/EXAMPLE/ message bien pris en compte")
	
           return []
