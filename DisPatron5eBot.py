# -*- coding: utf-8 -*-
"""
@author: Nathan Russell

DisPatron5e is an unofficial Dungeons and Dragons 5th Edition tool that
assists players and game masters alike in playing Dungeons and Dragons
over Discord servers.

 The information off of this bot is based off of the Players Handbook and the 
 Dungeon Master's Guide. Any other book's information may be added at a later
 date. 
"""

# bot.py
import os
import discord
import random
import nest_asyncio
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="*")
nest_asyncio.apply()
#If bootup is complete, will print in console. 
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
#command for rolling any number of multisided dice.     
@bot.command(
    help = "Use roll with 2 positive integers to foll a specific number of multisided dice. First number will be the number of dice. Second will be the number of sides of the dice."
    )
async def roll(ctx, arg1=None, arg2=None):  
    if (arg1.isnumeric() and arg2.isnumeric() and int(arg1) > 0 and int(arg2) > 0):
        for x in range(0, int(arg1)):
            await ctx.send(random.randint(1, int(arg2)))
    elif arg2 == None:
        await ctx.send("Must have 2 positive integers as input. Please try again.")
    else:
        await ctx.send("Input must be of 2 positive integers. Please try again.")
    
#command to add multiple numbers together. Used when adding damage dice in combat, 
#adding up skill checks, and any other required math problem that my be needed.  
@bot.command(
    help = "Adds up integers to calculate dice rolls with character stats."
    )
async def add(ctx, *args):
    total = 0
    
    for arg in args:
        if arg.isnumeric():
            total = total + int(arg)
            
    await ctx.send(total)

#command for information look up of a variety of charts and item descriptions. 
@bot.command(
    help = ("Gives information from Player's Handbook or Dungeon Master's Guide.\nValid Commands are:\n races \n classes \n backgrounds \n weapons \n spells \n wildmagic \n conditions")
    )
async def lookup(ctx, info):
    weapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer",
               "Mace", "QuarterStaff", "Sickle", "Spear", "Light Crossbow", "Dart",
               "Shortbow", "Sling", "Battleaxe", "Flail", "Glaive", "Greataxe",
               "Greatsword", "Halberd", "Lance", "Longsword", "Maul", "Morningstar",
               "Pike", "Rapier", "Scimitar", "Shortsword", "Trident", "Warpick",
               "Warhammer", "Whip", "Blowgun", "Hand Crossbow", "Heavy Crossbow",
               "Longbow", "Net"] 
    weapondice = ["1d4 bludgeoning", "1d4 piercing", "1d8 bludgeoning",
                  "1d6 slashing", "1d6 piercing", "1d4 bludgeoning", "1d6 bludgeoning",
                  "1d6 bludgeoning", "1d4 slashing", "1d6 piercing", "1d8 piercing",
                  "1d4 piercing", "1d6 piercing", "1d4 bludgeoning", "1d8 slashing",
                  "1d8 bludgeoning", "1d10 slashing", "1d12 slashing", "2d6 slashing",
                  "1d10 slashing", "1d12 piercing", "1d8 slashing", "2d6 bludgeoning",  
                  "1d8 piercing", "1d10 piercing", "1d8 piercing", "1d6 slashing",
                  "1d6 piercing", "1d6 piercing", "1d8 piercing", "1d8 bludgeoning", 
                  "1d4 slashing", "1 piercing", "1d6 piercing", "1d10 piercing", "1d8 piercing",
                  "No damage. Strength Check DC 10 or be restrained"]
    
    wildmagic = ["01-02	Roll on this table at the start of each of your turns for the next minute, ignoring this result on subsequent rolls.",
                 "03-04	For the next minute, you can see any invisible creature if you have line of sight to it.",
                 "05-06	A modron chosen and controlled by the DM appears in an unoccupied space within 5 feet of you, then disappears I minute later.",
                 "07-08	You cast Fireball as a 3rd-level spell centered on yourself.",
                 "09-10	You cast Magic Missile as a 5th-level spell.",
                 "11-12	Roll a d10. Your height changes by a number of inches equal to the roll. If the roll is odd, you shrink. If the roll is even, you grow.",
                 "13-14	You cast Confusion centered on yourself.",
                 "15-16	For the next minute, you regain 5 hit points at the start of each of your turns.",
                 "17-18	You grow a long beard made of feathers that remains until you sneeze, at which point the feathers explode out from your face.",
                 "19-20	You cast Grease centered on yourself.",
                 "21-22	Creatures have disadvantage on saving throws against the next spell you cast in the next minute that involves a saving throw.",
                 "23-24	Your skin turns a vibrant shade of blue. A Remove Curse spell can end this effect.",
                 "25-26	An eye appears on your forehead for the next minute. During that time, you have advantage on Wisdom (Perception) checks that rely on sight.",
                 "27-28	For the next minute, all your spells with a casting time of 1 action have a casting time of 1 bonus action.",
                 "29-30	You teleport up to 60 feet to an unoccupied space of your choice that you can see.",
                 "31-32	You are transported to the Astral Plane until the end of your next turn, after which time you return to the space you previously occupied or the nearest unoccupied space if that space is occupied.",
                 "33-34	Maximize the damage of the next damaging spell you cast within the next minute.",
                 "35-36	Roll a d10. Your age changes by a number of years equal to the roll. If the roll is odd, you get younger (minimum 1 year old). If the roll is even, you get older.",
                 "37-38	1d6 flumphs controlled by the DM appear in unoccupied spaces within 60 feet of you and are frightened of you. They vanish after 1 minute.",
                 "39-40	You regain 2d10 hit points.",
                 "41-42	You turn into a potted plant until the start of your next turn. While a plant, you are incapacitated and have vulnerability to all damage. If you drop to 0 hit points, your pot breaks, and your form reverts.",
                 "43-44	For the next minute, you can teleport up to 20 feet as a bonus action on each of your turns.",
                 "45-46	You cast Levitate on yourself.",
                 "47-48	A unicorn controlled by the DM appears in a space within 5 feet of you, then disappears 1 minute later.",
                 "49-50	You can't speak for the next minute. Whenever you try, pink bubbles float out of your mouth.",
                 "51-52	A spectral shield hovers near you for the next minute, granting you a +2 bonus to AC and immunity to Magic Missile.",
                 "53-54	You are immune to being intoxicated by alcohol for the next 5d6 days.",
                 "55-56	Your hair falls out but grows back within 24 hours.",
                 "57-58	For the next minute, any flammable object you touch that isn't being worn or carried by another creature bursts into flame.",
                 "59-60	You regain your lowest-level expended spell slot.",
                 "61-62	For the next minute, you must shout when you speak.",
                 "63-64	You cast Fog Cloud centered on yourself.",
                 "65-66	Up to three creatures you choose within 30 feet of you take 4d10 lightning damage.",
                 "67-68	You are frightened by the nearest creature until the end of your next turn.",
                 "69-70	Each creature within 30 feet of you becomes invisible for the next minute. The invisibility ends on a creature when it attacks or casts a spell.",
                 "71-72	You gain resistance to all damage for the next minute.",
                 "73-74	A random creature within 60 feet of you becomes poisoned for 1d4 hours.",
                 "75-76	You glow with bright light in a 30-foot radius for the next minute. Any creature that ends its turn within 5 feet of you is blinded until the end of its next turn.",
                 "77-78	You cast Polymorph on yourself. If you fail the saving throw, you turn into a sheep for the spell's duration.",
                 "79-80	Illusory butterflies and flower petals flutter in the air within 10 feet of you for the next minute.",
                 "81-82	You can take one additional action immediately.",
                 "83-84	Each creature within 30 feet of you takes 1d10 necrotic damage. You regain hit points equal to the sum of the necrotic damage dealt.",
                 "85-86	You cast Mirror Image.",
                 "87-88	You cast Fly on a random creature within 60 feet of you.",
                 "89-90	You become invisible for the next minute. During that time, other creatures can't hear you. The invisibility ends if you attack or cast a spell.",
                 "91-92	If you die within the next minute, you immediately come back to life as if by the Reincarnate spell.",
                 "93-94	Your size increases by one size category for the next minute.",
                 "95-96	You and all creatures within 30 feet of you gain vulnerability to piercing damage for the next minute.",
                 "97-98	You are surrounded by faint, ethereal music for the next minute.",
                 "99-00	You regain all expended sorcery points."]
    
    
    
    
    spell0 = ["Acid Splash", "Chill Touch", "Dancing Lights", "Fire Bolt", "Light", 
              "Mage Hand", "Mending", "Message", "Minor Illusion", "Poison Spray", "Prestidigitation", 
            "Ray of Frost", "Shocking Grasp", "True Strike"]
    
    spell1 = ["Alarm", "Burning Hands", "Charm Person", "Color Spray", "Comprehend Languages",
              "Detect Magic", "Disguise Self", "Expeditious Retreat", "False Life", "Feather Fall", 
              "Find Familiar", "Floating Disk", "Fog Cloud", "Grease", "Hideous Laughter",
              "Identify", "Illusory Script", "Jump", "Longstrider", "Mage Armor",
              "Magic Missile", "Protection from Evil and Good", "Shield", "Silent Image",
              "Sleep", "Thunderwave", "Unseen Servant"]
    
    spell2 = ["Acid Arrow", "Alter Self", "Arcane Lock", "Arcanist's Magic Aura",
              "Blindness/Deafness", "Blur", "Continual Flame", "Darkness", "Darkvision",
              "Enlarge/Reduce", "Flaming Sphere", "Gentle Repose", "Gust of Wind",
              "Hold Person", "Invisibility", "Knock", "Levitate", "Locate Object", 
              "Magic Mouth", "Magic Weapon", "Mirror Image", "Misty Step", "Ray of Enfeeblement",
              "Rope Trick", "Scorching Ray", "See Invisibility", "Shatter", "Spider Climb",
              "Suggestion", "Web"]
    
    spell3 = ["Animate Dead", "Bestow Curse", "Blink", "Clairvoyance", "Counterspell",
              "Dispel Magic", "Fear", "Fireball", "Fly", "Gaseous Form", "Glyph of Warding",
              "Haste", "Hypnotic Pattern", "Lightning Bolt", "Magic Circle", "Major Image", 
              "Nondetection", "Phantom Steed", "Protection from Energy", "Remove Curse",
              "Sending", "Sleet Storm", "Slow", "Stinking Cloud", "Tiny Hut", "Tongues",
              "Vampiric Touch", "Water Breathing"]
    
    spell4 = ["Arcane Eye", "Banishment", "Black Tentacles", "Blight", "Confusion",
              "Conjure Minor Elementals", "Control Water", "Dimension Door", "Fabricate",
              "Faithful Hound", "Fire Shield", "Greater Invisibility", "Hallucinatory Terrain",
              "Ice Storm", "Locate Creature", "Phantasmal Killer", "Polymorph", 
              "Private Sanctum", "Resilient Sphere", "Secret Chest", "Stone Shape",
              "Stoneskin", "Wall of Fire"]
    
    spell5 = ["Animate Objects", "Arcane Hand", "Cloudkill", "Cone of Cold", "Conjure Elemental",
              "Contact Other Plane", "Creation", "Dominate Person", "Dream", "Geas",
              "Hold Monster", "Legend Lore", "Mislead", "Modify Memory", "Passwall",
              "Planar Binding", "Scrying", "Seeming", "Telekinesis", "Telepathic Bond",
              "Teleportation Circle", "Wall of Force", "Wall of Stone"]
    
    spell6 = ["Chain Lightning", "Circle of Death", "Contingency", "Create Undead",
              "Disintegrate", "Eyebite", "Flesh to Stone", "Freezing Sphere", 
              "Globe of Invulnerability", "Guards and Wards", "Instant Summons",
              "Irresistible Dance", "Magic Jar", "Mass Suggestion", "Move Earth",
              "Programmed Illusion", "Sunbeam", "True Seeing", "Wall of Ice"]
    
    spell7 = ["Arcane Sword", "Delayed Blast Fireball", "Etherealness", "Finger of Death",
              "Forcecage", "Magnificent Mansion", "Mirage Arcane", "Plane Shift", 
              "Prismatic Spray", "Project Image", "Reverse Gravity","Sequester",
              "Simulacrum","Symbol","Teleport"]
    
    spell8 = ["Antimagic Field", "Antipathy/Sympathy", "Clone", "Control Weather",
              "Demiplane", "Dominate Monster", "Feeblemind", "Incendiary Cloud",
              "Maze", "Mind Blank", "Power Word Stun", "Sunburst"] 
    
    spell9 = ["Astral Projection", "Foresight", "Gate", "Imprisonment", "Meteor Swarm",
              "Power Word Kill", "Prismatic Wall", "Shapechange", "Time Stop", 
              "True Polymorph", "Weird", "Wish"]
    
    
    classname = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard"]
    classinfo = [" Path of the Berserker \n Path of the Totem Warrior", 
                 " College of Lore \n College of Valor",
                 " Knowledge Domain \n Life Domain \n Light Domain \n Nature Domain \n Tempest Domain \n Trickery Domain \n War Domain", 
                 " Circle of Land \n Circle of Moon",
                 " Battle Master \n Champion \n Eldritch Knight",
                 " Way of Shadow \n Way of Four Elements \n Way of Open Hand",
                 " Oath of Devotion \n Oath of Redemption \n Oath of the Ancients \n Oath of Vengeance",
                 " Beast Master \n Hunter",
                 " Arcane Trickster \n Assassin \n Thief",
                 " Draconic Bloodline \n Wild Magic",
                 " Archfey \n Fiend \n Great Old One",
                 " Abjuration \n Conjuration \n Divination \n Enchantment \n Evocation \n Illusion \n Necromancy \n Transmutation"]
    
    race = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-elf", "Halfling", "Half-orc",
            "Human", "Tiefling"] 
    
    background = ["Acolyte", "Charlatan", "Criminal/Spy", "Entertainer", "Folk Hero",
                  "Gladiator", "Guild Artisan/ Merchant", "Hermit", "Knight", "Noble",
                  "Outlander", "Pirate", "Sage", "Sailor", "Soldier", "Urchin"]
    
    conditions = ["Blinded", "Charmed", "Deafened", "Frightened", "Grappled",
                  "Incapacitated", "Invisible", "Paralyzed", "Petrified", "Poisoned",
                  "Prone", "Restrained", "Stunned", "Unconscious"]
    conditioninfo = ["A blinded creature can’t see and automatically fails any ability check that requires sight and attack Rolls against the creature have advantage, and the creature’s Attack Rolls have disadvantage.",
                     "A charmed creature can’t Attack the charmer or target the charmer with harmful Abilities or magical Effects andthe charmer has advantage on any ability check to interact socially with the creature",
                     "A deafened creature can’t hear and automatically fails any ability check that requires hearing.",
                     "A frightened creature has disadvantage on Ability Checks and Attack Rolls while the source of its fear is within Line of Sight and the creature can’t willingly move closer to the source of its fear.",
                     "A grappled creature’s speed becomes 0, and it can’t benefit from any bonus to its speed, the condition ends if the Grappler is incapacitated, and the condition also ends if an Effect removes the grappled creature from the reach of the Grappler or Grappling Effect,",
                     "An incapacitated creature can’t take Actions or Reactions.",
                     "An invisible creature is impossible to see without the aid of magic or a Special sense. For the Purpose of Hiding, the creature is heavily obscured. The creature’s location can be detected by any noise it makes or any tracks it leaves and Attack Rolls against the creature have disadvantage, and the creature’s Attack Rolls have advantage.",
                     "A paralyzed creature is incapacitated (see the condition) and can’t move or speak, the creature automatically fails Strength and Dexterity Saving Throws, Attack Rolls against the creature have advantage, and any Attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.", 
                     "A petrified creature is transformed, along with any nonmagical object it is wearing or carrying, into a solid inanimate substance (usually stone). Its weight increases by a factor of ten, it ceases aging, the creature is incapacitated (see the condition), can’t move or speak, and is unaware of its surroundings, Attack Rolls against the creature have advantage, the creature automatically fails Strength and Dexterity Saving Throws, the creature has Resistance to all damage, and, the creature is immune to poison and disease, although a poison or disease already in its system is suspended, not neutralized.",
                     "A poisoned creature has disadvantage on Attack Rolls and Ability Checks.",
                     "A prone creature’s only Movement option is to crawl, unless it stands up and thereby ends the condition, the creature has disadvantage on Attack Rolls, and an Attack roll against the creature has advantage if the attacker is within 5 feet of the creature. Otherwise, the Attack roll has disadvantage.",
                     "A restrained creature’s speed becomes 0, and it can’t benefit from any bonus to its speed, Attack Rolls against the creature have advantage, and the creature’s Attack Rolls have disadvantage, and the creature has disadvantage on Dexterity Saving Throws.",
                     "A stunned creature is incapacitated (see the condition), can’t move, and can speak only falteringly, the creature automatically fails Strength and Dexterity Saving Throws, and Attack Rolls against the creature have advantage.",
                     "An unconscious creature is incapacitated (see the condition), can’t move or speak, and is unaware of its surroundings, the creature drops whatever it’s holding and falls prone, the creature automatically fails Strength and Dexterity Saving Throws., Attack Rolls against the creature have advantage, and any Attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature."]
   
    if info == "weapons":
        await ctx.send("Weapons Table")
        text = ""
        for items in range(len(weapons)):
           text = text + "{} - {}".format(weapons[items], weapondice[items]) + "|n"
        ctx.send(text)
        
    elif info == "wildmagic":
        await ctx.send("Wild Magic Table")
        for items in range(len(wildmagic)):
            await ctx.send("{}".format(wildmagic[items]))
            
    elif info == "spells":
        await ctx.send("Spell Table \n")
        
        await ctx.send("Cantrips \n")
        message = ""
        for items in range(len(spell0)):
            message = message + ("{}".format(spell0[items])) + "\n"
        await ctx.send(message)
        
        await ctx.send("\n1st Level Spells \n")
        message = ""
        for items in range(len(spell1)):
            message = message + ("{}".format(spell1[items])) + "\n"
        await ctx.send(message)
        
        await ctx.send("\n2nd Level Spells \n")
        message = ""
        for items in range(len(spell2)):
            message = message + ("{}".format(spell2[items])) + "\n"
        await ctx.send(message)
        
        await ctx.send("\n3rd Level Spells \n")
        message = ""
        for items in range(len(spell3)):
            message = message + ("{}".format(spell3[items])) + "\n"
        await ctx.send(message)
        
        await ctx.send("\n4th Level Spells \n")
        message = ""
        for items in range(len(spell4)):
            message = message + ("{}".format(spell4[items])) + "\n"
        await ctx.send(message)
        
        await ctx.send("\n5th Level Spells \n")
        message = ""
        for items in range(len(spell5)):
            message = message + ("{}".format(spell5[items])) + "\n"
        await ctx.send(message)
        
        await ctx.send("\n6th Level Spells \n")
        message = ""
        for items in range(len(spell6)):
            message = message + ("{}".format(spell6[items])) + "\n"
        await ctx.send(message)
        
        await ctx.send("\n7th Level Spells \n")
        message = ""
        for items in range(len(spell7)):
            message = message + ("{}".format(spell7[items])) + "\n"
        await ctx.send(message)
        
        await ctx.send("\n8th Level Spells \n")
        message = ""
        for items in range(len(spell8)):
            message = message + ("{}".format(spell8[items])) + "\n"
        await ctx.send(message)
        
        await ctx.send("\n9th Level Spells \n")
        message = ""
        for items in range(len(spell9)):
            message = message + ("{}".format(spell9[items])) + "\n"
        await ctx.send(message)
    
    elif info == "classes":
        await ctx.send("Classes")
        for items in range(len(classname)):
            await ctx.send(classname[items] + "\n" + classinfo[items])
    
    elif info == "races":
        text = ""
        await ctx.send("Races")
        for items in range(len(race)):
            text = text + ("{}".format(race[items])) + "\n"
        await ctx.send(text)
        
    
    elif info == "backgrounds":
        text = ""
        await ctx.send("Backgrounds")
        for items in range(len(background)):
            text = text + ("{}".format(background[items])) + "\n"
        await ctx.send(text)
        
    elif info == "conditions":
        ctx.send("Conditions")
        for items in range(len(conditions)):
            await ctx.send("{} \n {} \n".format(conditions[items], conditioninfo[items]))
    
    else:
        await ctx.send("Command not valid. Please input valid command. Use *help lookup for valid commands.")
    
    await bot.process_commands(info)
    
nest_asyncio.apply()

bot.run(TOKEN)