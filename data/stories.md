## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## schedule
* greet
  - utter_greet
* ask_schedule
  - utter_ask_section
* give_section
  - utter_ask_group
* give_group
  - action_schedule
  - utter_goodbye

## contact
* greet
  - utter_greet
* ask_contact
  - utter_ask_contact
* give_contact
  - action_contact
  - utter_goodbye

## all_rooms
* greet
  - utter_greet
* ask_room
  - action_all_rooms
  - utter_goodbye

## map_ceri
* greet
  - utter_greet
* ask_map
  - utter_ask_site
* give_ceri
  - utter_give_ceri
  - utter_goodbye

## map_agroscience
* greet
  - utter_greet
* ask_map
  - utter_ask_site
* give_agroscience
  - utter_give_agroscience
  - utter_goodbye

## news
* greet
  - utter_greet
* ask_news
  - action_news
  - utter_description

## description
* ask_description
  - action_description
  - utter_goodbye
