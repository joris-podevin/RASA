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
from datetime import datetime
import re
#import feedparser

IPAddress = "10.104.21.124"

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
           requete = "http://"+IPAddress+":8085/cours/getCours/"+groupe+"/"+section+"/"+"2023-11-16T08:00:00"
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


class ActionAllRooms(Action):

     def name(self) -> Text:
         return "action_all_rooms"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

           now = datetime.now().time()
           time = now.strftime("%H:%M:%S")
           print (time)
           requete = "http://"+IPAddress+":8085/salles/getFreeSalles/"+time
           res = requests.get(requete)
           jsonRequest = json.loads(res.text)
           jsonList=[]
           cpt = 0
           reponse = "les salles libres en ce moment sont : "
           while (cpt <len(jsonRequest)):
                      reponse += jsonRequest[cpt]+" "
                      cpt+=1           
           dispatcher.utter_message(text=reponse)
	
           return []
           
           
           
class ActionContact(Action):

     def name(self) -> Text:
         return "action_contact"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

           
           contact = tracker.get_slot('contact')
           requete = "http://"+IPAddress+":8085/professeurs/getByName/Robert"
           res = requests.get(requete)
           reponse = "le contact de " + contact  + " est " + res.text
           
           dispatcher.utter_message(text=reponse)
	
           return []


class ActionNews(Action):

     def name(self) -> Text:
         return "action_news"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

           requete = "http://"+IPAddress+":8085/cours/infoTitre"
           res = requests.get(requete)
           reponse = res.text
           dispatcher.utter_message(text=reponse)
	
           return []
           
           
           
class ActionDescription(Action):

     def name(self) -> Text:
         return "action_description"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
           
           
           requete = "http://"+IPAddress+":8085/cours/infoDetails"
           res = requests.get(requete)
           reponse = res.text
           reponse = re.sub(r"<.*?>", '', reponse)
           dispatcher.utter_message(text=reponse)
	
           return []





