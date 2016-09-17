# Sustainable Sim

Sustainable Sim is a dating simulation which allows the user to pick a character, play in a simulated life.

To influence the user to live a sustainable life, the game asks questions about their preferences.
It uses Microsoft's Cognitive API to judge the user's emotion/enthusiasm, and calculate their sincerity in answering the questions. The result of this calculation then affects the result of the simulation. For example, a player who decides to state "yes" to a question may have a harder time in successfully completing the game than if they were to answer enthusiastically.


## Customization
In order to run capture.py, you need to execute the following command:

```
cp conf/sustainable_sim.yml conf/sustainable_sim.local.yml
```
Then, you will need to edit conf/sustainable_sim.local.yml

## Capture.py
This python file takes an image and uploads it to a server. The specifications for this file are set in sustainable_sim.local.yml
