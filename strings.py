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
"{}That's great! I know the perfect place...".format(e)) #img: ev_class
eve_happy = "That's great! I know the perfect place..."
agree = "Sounds good."

desk_3_button_1 = u + "Yeah, sure! Let's go."
desk_3_button_2 = u + "Actually... I was hoping Alice and I go alone..."

#next
eve_persist = "Oh, but come on! I really want to show you this place!"

#fence
fence_prompt = "Alex: This seems real sketchy you guys. Are you sure you want to go through here?" #img: scary_fence
"{}Don't be a wuss! It's not like you'll get abducted by aliens in the forest or something!".format(e)
fence_reprimand = "Eve! You're not being a wuss, Alex."
fence_resp = u + "I think it'll be fine. We'll stay really close together."
al_resigned = a + "Alright..."
taunt = "Yeah, Alex, relax a little."

#forest
al_scared_2 = a + "What was that sound?"
forest_resp_1 = "I don't know... Let's find out."
forest_resp_2 = "They're bears! Let's go, let's go, let's go!"

#waterfalls
al_excited = a + "Oh! It's a pretty waterfall!"
al_water_fact = a + "Oh, and it looks like there's a little water running now. I'm hoping that means that there's going to be enough water in the reservoir. More minerals have been getting into the municipal water supply than usual because of the low water levels and making the water all discolored. Maybe the filtration system can catch up now."
al_pict_water = a + "Let's take a picture here! Say, water conservation!"

#bears
al_surprised = a + "OMG it IS bears! Run, it's the Big Red Bears!"
bear_fact = u = "This makes me think about how the Asiatic Black Bear is endangered because their gall bladders are sold as an expensive medicine."
#url: http://www.konicaminolta.com/kids/endangered_animals/library/field/asiatic-black-bear.html

#falls and breaks ankle
romantic_op = "Are you alright?! Do you need help? I'll carry you!"
tip = "Nearly 60 percent of a person's household water footprint can go toward lawn and garden maintenance."



#images
desk = ""
al_class = ""
al_class_2 = ""
eve_barges_in = ""
ev_class = ""
eve_fence = ""
scary_fence = ""
