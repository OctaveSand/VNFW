#VNFW

VNFW is a light framework for making sandbox-style Renpy games. It builds on
the renpy framework to provide a set of classes and convienience functions to
enable the dev to focus on implementing storyline rather than things like
game-time, RPG-style stats-tracking, inventory, clothing, and money systems.
All of these entities are represented by classes in VNFW. The dev can implement
the objects she needs and move on with the story.

Renpy was designed to create linear novels, where the player follows a more or
less straight path through the narrative, but most successful VN's take a more
open-sandbox approach, allowing the player to progress the narrative by
visiting locations and interacting with players. VNFW makes this (pretty) easy
with its built-in `Event` and `Interaction` classes, which represent automation
that can be attached to in-game day/times or `Entities` respectively.
