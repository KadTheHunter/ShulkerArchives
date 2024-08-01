---
layout: single
title: "Mapart - Creating, Saving, Ripping"
toc: true
toc_sticky: true
toc_label: Table of Contents
toc_icon: scroll
---

This guide will show you everything you need to know about creating, saving, and ripping mapart in Minecraft.

# Creating
There are currently three methods for creating Mapart in Minecraft, each with their own pros and cons.

## Epsilon Bot
The first way to create mapart works in both singleplayer and multiplayer, and is called [Epsilon Bot](https://github.com/hhhzzzsss/EpsilonBot).

To get started, download or clone the repository and open it inside of something like [VisualStudio Code](https://code.visualstudio.com/Download) or [Intellij IDEA](https://www.jetbrains.com/idea/download/).

Navigate to `EpsilonBot/src/main/resources/default-config.yml` and edit the information as follows:
- Modify `host:` to the IP of the server you wish to connect to; Use `localhost` for a local world
- Modify `port:` to the port of the server you wish to connect to; Typically this is the default `25565` and does not need to be edited.
- Set `Username:` to the email for your Microsoft account
- Set `Password:` to the password for your Microsoft account
- Modify `mapartX:` and `mapartZ:` to different coordinates, if the world or server you play on restricts world size. To do so, find the North-West block of a chunk via F3, and use those coordinates.
- Modify `commandPrefix:` to a custom prefix for you. If you are using EpsilonBot in singleplayer or a private/whitelisted server, then you can skip this step.
- Modify `warpName:` to something unique. This is the name the bot will use to attempt to set a `/warp` when the map is finished.
- Add a new entry to `trusted:` with your UUID. Your UUID can be found by searching your username on a site like [NameMC](https://namemc.com/).

Once these changes are made (and saved!), run `Main.java` which is located at `src/main/java/com/github/hhhzzzsss/epsilonbot/Main.java`

On the first time you run EpsilonBot (and possibly other times in the future), you will need to sign in to your Microsoft account; You will be prompted in the console to do so, simply follow the instructions.

Once running, EpsilonBot (or rather, the MC Account you chose) will connect to the world or server. 
To get started using it, type 
``` 
`mapart <link-to-a-img/image.png> [1 2] [--NO_DITHER --USE_TRANSPARENCY]
```
in chat, modifying the prefix to yours.\
The numbers indicate the width and height in maps, e.g. `1 2` is 1 wide 2 high; When no dimensions are provided, EpsilonBot will default to a single map.\
The Dither and Transparency arguments are of course optional, but `--NO_DITHER` is highly recommended unless you preprocess the image.

Each mapart takes roughly 22 minutes for the Bot to build, and it will send a message in chat when it is finished.

If you are using EpsilonBot on a server that has the [EssentialsX](https://www.spigotmc.org/resources/essentialsx.9089/) plugin, EpsilonBot will create a warp in the format of `warpName_Number`, using the name you provided earlier, and the sequential mapart number.

To obtain the mapart, teleport to EpsilonBot, the coordinates you set earlier, or the warp it created, and create a map while standing over the relevant build.

## Schematic or .nbt Files
Another way to create mapart is to use an external program or site to generate and process an image into mapart, and then use the provided `.nbt` or `.schem` file to paste or build it in-game.

[MapartCraft](https://rebane2001.com/mapartcraft/) is the best tool for doing this, but there are numerous similar sites and programs scattered across the web; This guide will assume you are using MapartCraft, however.

Upload your image, and if needed, adjust the "Map size" option; Typically a 1x1 mapart is fine, but if your picture is of a wider or taller size, you can adjust the map size accordingly. 

Most of the other settings can be left on their defaults, but it is recommended to set "Dithering" to "None", to obtain the smoothest result, particularly if "Mapart size" is set to 1x1.

Click the "Download NBT" button; The `.nbt` file generated must be placed in the appropriate folder depending on what mod you will be using to load it in-game, so please consult the docs for your mod to find out where.

When pasting in your mapart, be sure to align it properly! An easy way of doing so is to pre-make the map in-game then fly to the North-West corner of the map, enable chunk borders with `F3 + G`, and find the furthest North and West block that's inside the map. Once you're certain you've found it, paste in the mapart and check the map.

## .dat Files
Similar to .nbt Mapart Files, .dat Mapart Files can be made on [MapartCraft](https://rebane2001.com/mapartcraft/).

Follow the steps for `.nbt` Mapart Files as shown above, but change "Mode" from "Schematic (NBT)" to "Datafile (map.dat)", then download the files with "Download mapdat". If the mapart is larger than 1x1, it is recommended to use the "Download mapdat.zip" option.

Cut the `.dat` files from your download folder, and paste them inside `/.minecraft/saves/YourWorldName/data/`. If there are already map.dat files in there, you will need to change the numbers of the ones you are adding before pasting them in (e.g: map_0.dat should become map_101755.dat

Join your world, and create a mapart. Then, using [NBT Editor](https://modrinth.com/mod/nbt-editor), or a similar mod of your choice, modify the `map` tags value to be the ID in the name of the `.dat` file.

You now have mapart, and without the large cumbersome build!

## Saving
If you found a really cool mapart on a server and want to save it, the easiest way is to find the build used for it, and make a copy.

There really isn't much of a guide to write here; Find the build and save a copy either with WorldEdit (if the server allows you to download schematics), Litematica, or other tools.

For some tips and tricks, check out the [Saving Builds](/guides/saving-builds/) guide.

# Ripping
Unfortunately, sometimes mapart builds can not be found (or in the case of generated .dat files, don't even exist!).

This brings us to the final mapart guide: Ripping.

To rip mapart, you will need the mod [Map.png](https://modrinth.com/mod/map.png).

Once in the server or world containing the mapart, simply hold the mapart in your hand and press `F8` to save it to `.minecraft/maps/`