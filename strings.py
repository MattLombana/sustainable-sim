#dialogue/prompts
instructions = "Hi! Welcome to Sustainable Sim! \n This is a prototypical choose-your-own-adventure/a dating sim where you can learn a thing or two about environmental conservation. Please note that we'll be using your camera to occasionally take your photos -- when you encounter a new environmental fact, smile big! Your potential partner is keeping track of how genuine you are about protecting the environment. \n Have fun exploring!"
u = "You: "
e = "Eve: "
name = "Alex"
a = "Alex: "

#desk first frame
desk_al_1 = "?: Hey, you!" #img: desk

#desk second frame
desk_second_prompt = "Alex: Oh, hey, what are you up to after school?"
desk_1_button_1 = "Nothing, I'm free tonight!"
desk_1_button_2 = "I'm hanging out with Eve." #->Hotel California
hell_1 = "You had a fun evening hanging out with Eve, although Alex looked forlorn. Maybe try again for a more interesting adventure?"

# desk 2.5
desk_25_prompt = "Alex: Cool! Do you want to go hiking with me?"

desk_25_button_1 = "yeah!"
desk_25_button_2 = "Uh..."


#desk third
desk_3_prompt = "Eve: HIKING?! Can I join you?!?\n".format(e) #img: eve_barges_in
"{}Oh, yeah... That's fine, I guess!".format(a) #img: al_class_2
"{}That's great! I know the perfect place...".format(e)#img: ev_class
eve_happy = "That's great! I know the perfect place..."
agree = "Sounds good."

desk_3_button_1 = "Yeah, sure! Let's go."
desk_3_button_2 = "Actually... I was hoping Alice and I go alone..."

#next
eve_persist = "Oh, but come on! I really want to show you this place!"

#fence
fence_prompt = "Alex: This seems real sketchy you guys. Are you sure you want to go through here?\nDon't be a wuss! It's not like you'll get abducted by aliens in the forest or something!".format(e)
fence_reprimand = "Eve! You're not being a wuss, Alex."
fence_resp = "I think it'll be fine. We'll stay really close together."
al_resigned = "Alright..."
taunt = "Yeah, Alex, relax a little."

#forest
al_scared_2 = "What was that sound?"
forest_resp_1 = "I don't know... Let's find out."
forest_resp_2 = "They're bears! Let's go, let's go, let's go!"

#waterfalls
al_excited = "Oh! It's a pretty waterfall!"
al_water_fact = "Oh, and it looks like there's a little water running now. I'm hoping that means that there's going to be enough water in the reservoir. More minerals have been getting into the municipal water supply than usual because of the low water levels and making the water all discolored. Maybe the filtration system can catch up now."
al_pict_water = "Let's take a picture here! Say, water conservation!"

#bears
al_surprised = "OMG it IS bears! Run, it's the Big Red Bears!"
bear_fact = "This makes me think about how the Asiatic Black Bear is endangered because their gall bladders are sold as an expensive medicine."
#url: http://www.konicaminolta.com/kids/endangered_animals/library/field/asiatic-black-bear.html

#falls and breaks ankle
romantic_op = "Are you alright?! Do you need help? I'll carry you!"
tip = "Nearly 60 percent of a person's household water footprint can go toward lawn and garden maintenance."
what = "What?"
disappoint = "You had a fun evening hanging out with Eve, although Alex looked forlorn. Maybe try again for a more interesting adventure?"
adis =  "Alex gave up and went home, and you and Eve barely explored the forest before it got too dark."
saycheese = "Hey, let's take a picture. Say water conservation!"


#Break ankle scene
Break_ankle_prompt="Alex:Ah! Ouch!\nYou:Are you alright?\nAlex:I think I twisted my ankle. I really dont think I can go on."# al is on the ground
response_1="Common on, get up! We can't keep Eve waiting"
response_2=" Ok let me help you up and we can take a look at it!"
# Flash Light scene
#while user takes a look at it
Flashlight_prompt="Alex:How bad is it? It's not too bad right?\nEve:Stop being a wuss! It's probably just a minor bruise.\nYou:Well, I could tell if I had a flash light. I can barely see a thing!"

#tractor beam silence even in the forest

Tracer_beam_prompt="Unidentified voice:Alex of Lafayette! You are the chosen one! You have been identified as the most environmentally concerned!\nEve:Hey look a UFO! Let me take a picture! smile!"
response_5="What?"# takes picture requries surprise
#If not smile
If_not_smile_prompt="Eve:User!!I said smile!"#else go into next mod
#alein interaction
Alein_interaction_prompt="Eve:And Mr. unidentified voice what do you mean by that he is the most environmentally concerned? Did you know that I recycled 2 pop cans last week?\nYou:Talking about recycling, Did you know the average person has the opportunity to recycle more than 25,000 cans in a lifetime?"




#Sounds of beams on alex he is getting sucked in
sucked_in_prompt="Alex:Oh God!What's happening?\nEve:Come on user let's go!\nYou:But what about Alex? We can't abandon him\nEve:We dont have time! We gotta get going!"
response_3="Sorry Alex!I promise I'll come back!" #leads to node where you run into an alein
response_4="No! I am not gonna leave him! We were all in this together!!"

#next scene
#flashlight goes off


#next screen blacks out , thud sounds
MUM_prompt="Mom:Honey! Wake up , you were talking in your sleep again!"
#wakes up in bed
wake_bed_prompt= "Mom:You need start getting ready! Your bus will be here any time now!\nYou:For what?\nMom:It's the last day of school"
response_7="You:Mom Did you know that..."
#at school
at_school_promt="?:Hey you!"
"........"


#hell node
hell_prompt="Unfortunately that was a bad choice. Better luck next time."


tesstvar1 = "I'm hanging out with Eve."
tesstvar2 = "Nothing, I'm free tonight!"
empty_string = ""
