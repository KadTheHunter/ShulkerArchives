import asyncio
import io
import json

import discord
from discord.ext import commands

client = discord.Client()
intents = discord.Intents.default()
bot = commands.Bot(command_prefix=".", intents=intents)

with open("trustedlist.json") as f:
    trustedUsers = json.load(f)


def addTrusterUser(id):
    global trustedUsers
    trustedUsers.append(id)
    with open("trustedlist.json", "w") as f:
        json.dump(trustedUsers, f)


with open("db.json", encoding="utf8") as f:
    dbDict = json.load(f)

with open("unsorted.json", encoding="utf8") as f:
    unsortedDbDict = json.load(f)


def setAliases():
    with open("aliases.json") as f:
        aliases = json.load(f)


def addAliases(original, alias):
    aliases[original] = alias

    with open("aliases.json", "w") as f:
        json.dump(aliases, f)


def updatedb(d):
    with open("db.json", encoding="utf8") as f:
        data = json.load(f)

    for creator, shulkers in d.items():
        if creator in data:
            data[creator] |= shulkers
        else:
            data[creator] = shulkers

    with open("db.json", "w", encoding="utf8") as f:
        json.dump(data, f)
    global dbDict
    dbDict = data


def savedb():
    with open("db.json", "w", encoding="utf8") as f:
        json.dump(dbDict, f)


"""
	{
		"CreatorName": {
			"KitName": {
				"nbt":"{}",
				"container":"shulker_box"
			}
		}
	}
"""


@bot.event
async def on_ready():
    print("Logged in as " + bot.user.name)
    await bot.change_presence(
        activity=discord.Game(name="https://discord.gg/kgM6kfMBFh")
    )


@bot.command()
async def trust(ctx, *args):  # db list / db add
    if ctx.author.id == 356179003318468608:
        addTrusterUser(str(ctx.message.mentions[0].id))
        await ctx.send("Trusted!")
    else:
        await ctx.send("ur no bot owner")


@bot.command()
async def stop(ctx, *args):
    if ctx.author.id == 356179003318468608:
        await ctx.send("Stopping.")
        exit()


############################# DB ################################
@bot.command()
async def db(ctx, *args):  # db list / db add
    args = list(args)

    ########################### DB HELP ###############################
    async def helpmsg():
        helpmsg = """
Usage:
```md
.db 
  - add            # Add an entry to the database
  - info           # Information about the database

  - list           # Lists entries in the database
    - kits           # Lists kits
    - creators       # Lists creators
    - <Creator Name> # Lists entries from a specific creator
    - unsorted       # Lists entries from the raw list from /warp kits

  - get            # Get an item from the database (Case sensitive!)
    - [Creator Name] # Name of the creator of the kit
      - [Kit Name]     # Kit name
    - unsorted       # Pull from the unsorted list
      - [Kit Name]     # Kit name
```
"""
        await ctx.send(helpmsg)

    ###################### DB LIST ############################
    maxPerPage = 10

    def selectFromList(thelist, offset):
        msg = ""
        if thelist == "unsorted":
            kitsList = ""
            for name, nbt in unsortedDbDict.items():
                kitsList += "\n" + name + " - " + str(len(nbt)) + " bytes long."

            kitsList = kitsList.split("\n")
            msg = "\n".join(kitsList[0 + offset : maxPerPage + offset])
            pages = int(len(kitsList) / 10)

        elif thelist == "creators":
            creatorList = ""
            for name, kits in dbDict.items():
                creatorList += "\n" + name + " - " + str(len(kits)) + " kits."
            creatorList = creatorList.split("\n")

            msg = "\n".join(creatorList[0 + offset : maxPerPage + offset])
            pages = int(len(creatorList) / 10)

        elif thelist == "kits":
            kitsList = ""
            for creator, kits in dbDict.items():
                for kitname, kit in kits.items():
                    kitsList += (
                        "\n"
                        + creator
                        + ": "
                        + kitname
                        + " | "
                        + kit["container"]
                        + " - "
                        + str(len(kit["nbt"]))
                        + " bytes long."
                    )

            kitsList = kitsList.split("\n")
            msg = "\n".join(kitsList[0 + offset : maxPerPage + offset])
            pages = int(len(kitsList) / 10)

        elif thelist in dbDict:
            kitList = ""
            for name, kit in dbDict[thelist].items():
                kitList += (
                    "\n"
                    + name
                    + " | "
                    + kit["container"]
                    + " - "
                    + str(len(kit["nbt"]))
                    + " bytes long."
                )

            kitList = kitList.split("\n")

            msg = "\n".join(kitList[0 + offset : maxPerPage + offset])
            pages = int(len(kitList) / 10)
        else:
            return "Unknown argument or creator!", -1

        if not msg:
            msg = "Empty!"
        return msg, pages + 1

    def list_embed(listing, offset):
        value, pages = selectFromList(listing, offset)
        fields = [
            {"name": listing, "value": value, "inline": False},
            {
                "name": "\u2800",
                "value": "\n\n*Page "
                + str(int(offset / 10 + 1))
                + "/"
                + str(pages)
                + "*",
            },
        ]

        e = {
            "title": "DB List",
            "type": "rich",
            "description": "",
            "color": 0x00FFFF,
            "fields": fields,
        }
        return discord.Embed.from_dict(e)

    async def db_list(*subcommand):  # db list all / db list Yurni
        subcommand = subcommand[0]
        if not subcommand:
            await helpmsg()
            return

        offset = 0

        if len(subcommand) > 1:
            offset = (int("".join(filter(str.isdigit, "0" + subcommand[1]))) - 1) * 10

        subcommand = subcommand[0]

        if subcommand == "creators":
            await ctx.send(embed=list_embed("creators", offset))
        else:
            await ctx.send(embed=list_embed(subcommand, offset))

    ################### DB ADD ##################################
    def textreply(m):
        return m.channel == ctx.channel and ctx.author == m.author

    async def ask(q):
        msg = await ctx.send(q)
        try:
            reply = await bot.wait_for("message", check=textreply, timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("You You took too long to answer this prompt!")
            raise Merror

        if reply.content == "cancel":
            await ctx.send("Cancelling.")
            raise Merror
        await msg.delete()
        return reply.content

    def filereply(m):
        return (
            m.channel == ctx.channel
            and ctx.author == m.author
            and len(m.attachments) > 0
        )

    async def askFile(q):
        msg = await ctx.send(q)
        try:
            reply = await bot.wait_for("message", check=filereply, timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("You You took too long to answer this prompt!")
            raise Merror
        if reply.content == "cancel":
            await ctx.send("Cancelling.")
            raise Merror
        await msg.delete()
        f = await reply.attachments[0].read()
        return f.decode("utf-8")

    async def db_add(args):
        if not str(ctx.author.id) in trustedUsers:
            await ctx.send("You need to be a trusted user to do that!")
            return
        await ctx.send("Say cancel at any time to cancel.")
        entry = {}
        creator = await ask("What is the name of the creator? **(CASE SENSITIVE)**")
        entry[creator] = {}
        kit = await ask("What is the name of the kit?")
        entry[creator][kit] = {}
        entry[creator][kit]["container"] = await ask(
            "What is the namespaced ID of the kit container? (trapped_chest, pink_shulker_box, ...)"
        )
        entry[creator][kit]["nbt"] = await askFile(
            "What is the nbt of the item? (Send in a text file, messages over 2000 characters long will automatically be made into a text file.)"
        )
        updatedb(entry)
        await ctx.send("Added!")

    ################### DB GET ##################################
    async def db_get(args):
        if not args:
            await helpmsg()
            return

        creator = args.pop(0)
        kname = " ".join(args)

        if creator == "unsorted":
            if not kname in unsortedDbDict:
                await ctx.send(
                    "This kit doesnt exist! (Are you sure it's spelled right?)"
                )
            else:
                container = "shulker_box"
                nbt = unsortedDbDict[kname]
        elif not creator in dbDict:
            await ctx.send("Unknown creator!")
        elif not kname in dbDict[creator]:
            await ctx.send("Unknown kit from " + creator + "!")
        else:
            container = dbDict[creator][kname]["container"]
            nbt = dbDict[creator][kname]["nbt"]
        msg = "Wurst: .give " + container + " 1 " + nbt
        msg += "\n\nMeteor: .give " + container + nbt
        msg += "\n\nVanilla: /give @p " + container + nbt
        if len(msg) > 2000:
            await ctx.send(
                file=discord.File(
                    io.BytesIO(str.encode(msg)), filename="Give Commands.txt"
                )
            )
        else:
            await ctx.send(msg)

    ##################### DB INFO ##################################

    async def db_info(args):
        kitCount = 0
        for creator, kits in dbDict.items():
            for kitname, kit in kits.items():
                kitCount += 1
        fields = [
            {"name": "Sorted Kits", "value": kitCount, "inline": True},
            {"name": "Unsorted Kits", "value": len(unsortedDbDict), "inline": True},
            {"name": "Creators", "value": str(len(dbDict)), "inline": False},
            {
                "name": "Sorted DB Size",
                "value": str(len(str(dbDict))) + " bytes.",
                "inline": True,
            },
            {
                "name": "Unsorted DB Size",
                "value": str(len(str(unsortedDbDict))) + " bytes.",
                "inline": True,
            },
            {"name": "\u2800", "value": "\n\n*Made by Folfy_Blue*"},
        ]

        e = {
            "title": "DB List",
            "type": "rich",
            "description": "",
            "color": 0x00FFFF,
            "fields": fields,
        }
        e = discord.Embed.from_dict(e)

        await ctx.send(embed=e)

    ################### DB DELETE ##################################
    async def db_del(args):
        if not str(ctx.author.id) in trustedUsers:
            await ctx.send("You need to be a trusted user to do that!")
            return
        creator = args.pop(0)
        kit = " ".join(args)
        if creator in dbDict:
            if kit in dbDict[creator]:
                del dbDict[creator][kit]
                savedb()
                await ctx.send("Done!")
            else:
                await ctx.send("Unknown kit")
        else:
            await ctx.send("Unknown creator")

    ################### DB ##################################
    if not args or not "db_" + args[0] in locals():
        await helpmsg()
    else:
        subcmd = "db_" + args.pop(0)
        await locals()[subcmd](args)


bot.run(env.token)
