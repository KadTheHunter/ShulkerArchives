---
permalink: /resources/
layout: single
title: "Resources"
toc: true
toc_sticky: true
toc_label: Table of Contents
toc_icon: scroll
---

# Guides
This is a collection of guides for various Minecraft NBT related things.
- [Mapart]({{ site.baseurl }}/guides/mapart/) (Creating, Saving, Ripping)
- [Saving Builds]({{ site.baseurl }}/guides/saving-builds/) (WorldEdit, Chunk Ripper)

*Coming soon:*
- Basic NBT (Name, Lore, Colors)
- Intermediate NBT (Attributes, Enchantments, Gradients)
- Advanced NBT (Damage, Entities, Exploits)

# Recommended Mods, Websites, and Software
This is a list of recommended Mods, Websites, and Software, some directly connected to NBT and some loosely related but still useful.

## Official Archives Modpack
The Shulker Archives has an [official Modpack](https://modrinth.com/modpack/the-shulker-archives) containing many of the mods listed below, alongside the latest release of the Map, all preconfigured and ready to use. 

If you aren't into making your own instances and dealing with Mods, the Modpack is a perfect alternative.

## (Fabric) Mods
- [FZMM](https://modrinth.com/mod/FZMM)
  - FZMM is a somewhat niche but still incredible mod, offering tons of advanced features like creating Lore Art/Hologram Art, modifying Player Head Data to add custom textures, a GUI for designing Banners, and an excellent array of tools to give text everything from simple colors to beautiful gradients.
- [Map.png](https://modrinth.com/mod/map.png)
  - Map.png allows downloading and converting Minecraft maps to `.png` images with the press of a key-bind, in both Single- and Multi- player gamemodes.
- [NBT Editor](https://modrinth.com/mod/nbt-editor)
  - NBT Editor is the pinnacle of NBT Editing Mods. What it lacks in UI design, it makes up for a thousand times over in other features, such as the ability to Import and Export `.nbt` files, retrieval of "lost" items via its /get lostitem history command, and its amazing Client Chest, which by default has 100 large chests' space for items, but can be expanded infinitely. All of its features also fully support tags such as `Infinity` and `NaN`, which means you can safely use it without worrying about your tags being messed with.
- [Song Player](https://modrinth.com/mod/songplayer)
  - Song Player plays valid `.midi` and `.nbs` song files on Note Blocks. While this alone (and how it does it) is fairly impressive, the NBT aspect comes in with Song Items: Items with song data encoded to them in an NBT tag, allowing sharing of songs so other users can play them without having copies of the files. Now *that's* impressive.
- [Symbol Chat](https://modrinth.com/mod/symbol-chat)
  - Symbol Chat adds a menu to Chat, Signs, Books, and most other Text Inputs that allows you to use different fonts, and all manner of unicode symbols.

## Websites
- [Block Display Studio](https://eszesbalint.github.io/bdstudio/editor)
  - Block Display Studio is a 3D editor and command generator for Minecraft's display entities, enabling you to bring custom 3D models into your Minecraft worlds without the use of mods or resource packs.
- [MapartCraft](https://rebane2001.com/mapartcraft/)
  - MapartCraft is the do-it-all site for Mapart, where you can upload an image and customize the dithering, size, blocks used, etc. before either saving the preview image or downloading the map as a Schematic (.nbt) or Data (.dat) file.
- [MCStacker](https://mcstacker.net/)
  - MCStacker is an online Command/NBT generator that allows you to choose the command and features, and then generates it for you.
- [NBT Minifier](https://autocompressor.net/tools/nbt-minifier)
  - NBT Minifier is an experimental compressor to remove un-needed/blank/duplicate tags from SNBT, such as ones added by ItemizerX.
- [Obj To Schematic](https://objtoschematic.com/)
  - Obj To Schematic converts 3D model files such as `.obj` and `.glb` files into `.schematic`, `.schem`, `.litematic`, `.nbt` and `.json` files, with tons of settings to tweak and customize the output.
  - *There is also an (older) application version of this site available at [LucasDower/ObjToSchematic](https://github.com/LucasDower/ObjToSchematic) on GitHub.*
- [R74n](https://r74n.com/)
  - R74n is an interesting amalgamation of resources and tools for Minecraft and other things. Of particular note is the [Box Page](https://r74n.com/box) containing the `/give` commands and NBT for a number of Shulker Kits.
- [txsla.net](http://www.txsla.net/)
  - Txsla.net is the official website for Tesla Tower and hosts a variety of tools, from programs for the Ti84+CE calculator, to the Tesla Kit series, and the NBT Archives Minecraft Server. Of particular use is the dedicated [Tesla Kits page](http://www.txsla.net/kit/kit.htm), providing downloads for the latest release of the Tesla Kits.

## Software
- [EpsilonBot](https://github.com/hhhzzzsss/EpsilonBot/)
  - Epsilon Bot turns your chosen Minecraft account into a mapart building bot, with the bonus function of being able to sync with a local build server.
  - *Check out our guide on [using Epsilon Bot to Create Mapart]({{ site.baseurl }}/guides/mapart#epsilon-bot)!*
- [map-to-img](https://github.com/mircokroon/minecraft-maps-to-images/)
  - map-to-img is a fairly obscure tool for converting Minecraft maps to images.
- [MCA Selector](https://github.com/Querz/mcaselector)
  - MCA Selector is *intended* to be used as a tool for exporting or deleting chunks from a Minecraft world; What it can *also* be used for, is mass-editing the NBT of selected chunks. Ever needed to mass-edit the `DataVersion` tag of several hundred chunks? I have, and MCA Selector did when nothing else could/would!
- [NBT Studio](https://github.com/tryashtar/nbt-studio/)
  - NBT Studio is one of the best External NBT Editors, capable of editing any `.nbt` file with ease. Significant knowledge of NBT is needed to use it effectively.


