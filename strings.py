#dialogue/prompts
instructions = "Hi! Welcome to Sustainable Sim! \n This is a prototypical choose-your-own-adventure/a dating sim where you can learn a thing or two about environmental conservation. Please note that we'll be using your camera to occasionally take your photos -- when you encounter a new environmental fact, smile big! Your potential partner is keeping track of how genuine you are about protecting the environment. \n Have fun exploring!"
u = "You: "
e = "Eve: "
name = "Alex"
a = name + ": "

#desk first frame
desk_al_1 = "?: Hey, you!" #img: desk
#desk second frame
desk_resp_1 = "Oh, hey, " + name #img: al_class
desk_al_2 = a + ": What are you up to after school?"
desk_button_1 = "Nothing, I'm free tonight!" 
desk_button_2 = "I'm hanging out with Eve." #->Hotel California
desk_al_3 = a + "Cool! Do you want to go hiking with me?"
desk_resp_2 = "Um... yeah!"
desk_resp_3 = "Uh..."
#desk third
eve_ugh = e + "HIKING?! Can I join you?!?" #img: eve_barges_in
#fourth
al_resp = a + "Oh, yeah... That's fine, I guess!" #img: al_class_2
#next
eve_be_sketch = e + "That's great! I know the perfect place..." #img: ev_class
resp_to_eve_1 = u + "Yeah, sure! Let's go."
resp_to_eve_2 = u + "Actually... I was hoping Alice and I go alone..."
#next
eve_persist = e + "Oh, but come on! I really want to show you this place!"

#fence
al_scared = a + "This seems real sketchy you guys. Are you sure you want to go through here?" #img: scary_fence
eve_danger = e + "Don't be a wuss, " + name + "! It's not like you'll get abducted by aliens in the forest or something!" #img: eve_fence; ignore blatant foreshadowing
fence_reprimand = u + "Eve! You're not being a wuss, " + name + ". "
fence_resp = u + "I think it'll be fine, " + name + ". We'll stay really close together."
al_resigned = a + "Alright..."

#forest
al_scared_2 = a + "What was that sound?" 
forest_resp_1 = "I don't know... Let's find out."
forest_resp_2 = "They're bears! Let's go, let's go, let's go!"

#bears
al_surprised = a + "OMG it IS bears! Run, it's the Big Red Bears!"
bear_fact = u = "This makes me think about how the Asiatic Black Bear is endangered because their gall bladders are sold as an expensive medicine."
#url: http://www.konicaminolta.com/kids/endangered_animals/library/field/asiatic-black-bear.html

#falls and breaks ankle
romantic_op = "Are you alright?! Do you need help? I'll carry you!"




#images
desk = ""
al_class = ""
al_class_2 = ""
eve_barges_in = ""
ev_class = ""
eve_fence = ""
scary_fence = ""
