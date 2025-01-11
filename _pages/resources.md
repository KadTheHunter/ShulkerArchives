---
permalink: /resources/
layout: single
title: "Resources"
toc: true
toc_sticky: true
toc_label: Table of Contents
toc_icon: scroll
---

<style>
#page-title{
text-align: center;
}
article.page {
  float: left;
  width: 100%;
}
.toc__menu li ul li ul > li a {
  padding-left: 2.5rem;
}

.toc__menu li ul li ul li ul > li a {
  padding-left: 3rem;
}

.toc__menu li ul li ul li ul li ul > li a {
  padding-left: 3.5rem;
}
</style>

# Recommended Mods, Websites, Software and Servers
This is a list of recommended Mods, Websites, Software and Servers, some directly related to NBT and some loosely related but still useful.

## Official Archives Modpack
The Shulker Archives has an [official Modpack](https://modrinth.com/modpack/the-shulker-archives) containing many of the mods listed below, alongside the latest release of the Map, all preconfigured and ready to use. 

If you aren't into making your own instances and dealing with Mods, the Modpack is a perfect alternative.

## (Fabric) Mods
### [NBT Editor](https://modrinth.com/mod/nbt-editor)
  - NBT Editor is the current pinnacle of NBT Editing Mods, making creating and editing items a breeze, with a variety of advanced features, including the ability to Import and Export `.nbt` files, retrieval of "lost" items via its /get lostitem history command, and its amazing Client Chest, which by default has 100 large chests' space for items, but can be expanded infinitely.

### [FZMM](https://modrinth.com/mod/FZMM)
  - FZMM is a somewhat niche but still incredible mod, offering tons of advanced features like creating Lore Art/Hologram Art, modifying Player Head Data to add custom textures, a GUI for designing Banners, and an excellent array of tools to give text everything from simple colors to beautiful gradients.

### [Map.png](https://modrinth.com/mod/map.png)
  - Map.png allows downloading and converting Minecraft maps to `.png` images at the press of a keybind, in both Single and Multiplayer gamemodes.

### [Armor Stands](https://modrinth.com/mod/armor-stands)
  - Armor Stands adds a full-featured and easy to use UI for editing Armor Stands. Simply right-click on the armorstand, and begin!

### [Hotbars+](https://github.com/VideoGameSmash12/HotbarsPlus/releases/)
  - Hotbars+ allows switching between multiple hotbar files with ease, allowing for effectively infinite hotbar storage.

### [Symbol Chat](https://modrinth.com/mod/symbol-chat)
  - Symbol Chat adds a menu to Chat, Signs, Books, and most other Text Inputs that allows you to use different fonts, and all manner of unicode symbols.

### [Song Player](https://modrinth.com/mod/songplayer)
  - Song Player plays valid `.midi` and `.nbs` song files on Note Blocks. While this alone (and how it does it) is fairly impressive, the NBT aspect comes in with Song Items: Items with song data encoded to them in an NBT tag, allowing sharing of songs so other users can play them without having copies of the files. Now *that's* impressive.

## Websites
### [MCStacker](https://mcstacker.net/)
  - MCStacker is an online Command/NBT generator that allows you to choose the command and features, and then generates it for you.

### [GamerGeeks](https://www.gamergeeks.net/apps/minecraft/)
  - GamerGeeks.net provides a variety of generators similar to MCStacker, though with a more visually pleasing UI.

### [Block Display Engine](https://block-display.com/)
  - Block Display Engine is a 3D editor and command generator for Minecraft's display entities, enabling you to bring custom 3D models into your Minecraft worlds without the use of mods or resource packs. The site also contains a library of user-created display entities for use in your world. _See also: [Block Display Engine App](#block-display-engine-app)._

### [MapartCraft](https://rebane2001.com/mapartcraft/)
  - MapartCraft is the do-it-all site for Mapart, where you can upload an image and customize the dithering, size, blocks used, etc. before either saving the preview image or downloading the map as a Schematic (.nbt) or Data (.dat) file.

### [Obj To Schematic](https://objtoschematic.com/)
  - Obj To Schematic converts 3D model files such as `.obj` and `.glb` files into `.schematic`, `.schem`, `.litematic`, `.nbt` and `.json` files, with tons of settings to tweak and customize the output.
  - *There is also an (older) application version of this site available at [LucasDower/ObjToSchematic](https://github.com/LucasDower/ObjToSchematic) on GitHub.*

### [MCUtils](https://mcutils.com/)
  - MCUtils holds a wide array of utilities for Minecraft, ranging from Server Info and Skin Stealers, to Firework Creators and even a database of Noteblock Songs.

### [Item NBT -> Components](https://misode.github.io/nbt2components/)
  - Item NBT -> Components is a tool for converting Item NBT data in the form of SNBT to Component data, with output as JSON, Command and SNBT data.

{::comment}

Add txsla.net back whenever txsla finally brings it back online.

### [txsla.net](http://www.txsla.net/)
  - Txsla.net is the official website for Tesla Tower and hosts a variety of tools, from programs for the Ti84+CE calculator, to the Tesla Kit series, and the NBT Archives Minecraft Server. Of particular use is the dedicated [Tesla Kits page](http://www.txsla.net/kit/kit.htm), providing downloads for the latest release of the Tesla Kits.

{:/comment}

## Software
{::comment}

Add Epsilon Bot back whenever hhhzzzsss finally fixes it

### [EpsilonBot](https://github.com/hhhzzzsss/EpsilonBot/)
  - Epsilon Bot turns your chosen Minecraft account into a mapart building bot, with the bonus function of being able to sync with a local build server.
  - *Check out our guide on [using Epsilon Bot to Create Mapart]({{ site.baseurl }}/guides/mapart#epsilon-bot)!*

{:/comment}

### [Block Display Engine App](https://block-display.com/BDEngine.exe)
  - Block Display Engine is a 3D editor and command generator for Minecraft's display entities, enabling you to bring custom 3D models into your Minecraft worlds without the use of mods or resource packs. The app is the same as the [website](#block-display-engine), but in a standalone app format with improved performance.

### [map-to-img](https://github.com/mircokroon/minecraft-maps-to-images/)
  - map-to-img is a fairly obscure tool for converting Minecraft maps to images.

### [MCA Selector](https://github.com/Querz/mcaselector)
  - MCA Selector is *intended* to be used as a tool for exporting or deleting chunks from a Minecraft world; What it can *also* be used for, is mass-editing the NBT of selected chunks. Ever needed to mass-edit the `DataVersion` tag of several hundred chunks? I have, and MCA Selector did when nothing else could/would!

### [NBT Studio](https://github.com/tryashtar/nbt-studio/)
  - NBT Studio is one of the best External NBT Editors, capable of editing any `.nbt` file with ease. Significant knowledge of NBT is needed to use it effectively.

## Servers
### [NBT Archives](https://discord.gg/ZhJyamzvvE)
  - NBT Archives is the largest public collection of Component Data for Minecraft, where users can easily submit their creations for all to see. Join it via `play.nbtarchives.net`!
