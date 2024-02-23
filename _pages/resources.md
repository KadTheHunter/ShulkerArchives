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
- [Restoring HD Heads]({{ site.baseurl }}/guides/restoring-hd-heads/)

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
- [Armor Stands](https://modrinth.com/mod/armor-stands/)
  - Armor Stands is an excellent way to edit every detail about an armorstand while in-game, and all using a nice, clean GUI.
- [Custom Skin Loader](https://modrinth.com/mod/customskinloader)
  - Custom Skin Loader allows loading skins from a variety of sources, but most importantly loads from the full `minecraft.net` domain *and* allows HD + Transparency, thus supporting [HD Heads]({{ site.baseurl }}/guides/restoring-hd-heads/)
- [FZMM](https://modrinth.com/mod/FZMM)
  - FZMM is a somewhat niche but still incredible mod, offering tons of advanced features like creating Lore Art/Hologram Art, modifying Player Head Data to add custom textures, a GUI for designing Banners, and an excellent array of tools to give text everything from simple colors to beautiful gradients.
- ~~[Hotbars+](https://modrinth.com/mod/Hotbars+)~~
  - ~~Hotbars+ allows you to have an infinite number of hotbars by creating new hotbar files, and swapping them out at the click of a button. It may not be the easiest for on-the-go item storage (for that, see NBT Editor) but it's perfect for making sure your items and kits are safely stored and accessible from anywhere in your Minecraft instance.~~
  - ***Hotbars+ is currently stuck on 1.20.2 due to Minecraft 1.20.3+ breaking how Hotbar files are saved. See [Issue #33](https://github.com/VideoGameSmash12/HotbarsPlus/issues/33#issuecomment-1844678093) for more information.***
- [IBE Editor](https://modrinth.com/mod/ibe-editor)
  - IBE Editor (Item Block Entity Editor) is a Mod with similar features to NBT Editor (NBT/SNBT editing, Item Vault, etc.), though it really shines with its NBT Tag Editing page. No other mod displays NBT Tags in such a nice, easy to read tree format besides IBE Editor, and that alone makes it worthy of including in your Minecraft instance.
- [NBT Editor](https://modrinth.com/mod/nbt-editor)
  - NBT Editor is the pinnacle of NBT Editing Mods. What it lacks in UI design, it makes up for a thousand times over in other features, such as the ability to Import and Export `.nbt` files, retrieval of "lost" items via its /get lostitem history command, and its amazing Client Chest, which by default has 100 large chests' space for items, but can be expanded infinitely. All of its features also fully support tags such as `Infinity` and `NaN`, which means you can safely use it without worrying about your tags being messed with.
- [NBT Void](https://modrinth.com/mod/nbt-void)
  - NBT Void logs every item with custom NBT that your client encounters. Whether you want a form of backup in case you accidentally lose something, or you want a rudimentary ItemLogger, NBT Void can do it.
- [Song Player](https://modrinth.com/mod/songplayer)
  - Song Player plays valid `.midi` and `.nbs` song files on Note Blocks. While this alone (and how it does it) is fairly impressive, the NBT aspect comes in with Song Items: Items with song data encoded to them in an NBT tag, allowing sharing of songs so other users can play them without having copies of the files. Now *that's* impressive.
- [Symbol Chat](https://modrinth.com/mod/symbol-chat)
  - Symbol Chat adds a menu to Chat, Signs, Books, and most other Text Inputs that allows you to use different fonts, and all manner of unicode symbols.
- ~~[WNT](https://modrinth.com/mod/wnt)~~
  - ~~WNT is the ultimate combination of Utility and Protection in Minecraft. Using its commands, or the built-in Blackbox menu, you can dump almost any data you choose (be it Entities, Maps, Threads, etc.), and if you don't want all of it you can choose a specific point to dump. In addition to this (and perhaps more importantly), it protects against the worst NBT Exploits, and allows you to still have some control over your game even when Minecraft has frozen.~~
  - ***WNT is currently stuck on 1.20.2 due to Minecraft 1.20.3/.4 breaking major components of WNT.***

## Websites
- [Block Display Studio](https://eszesbalint.github.io/bdstudio/editor)
  - Block Display Studio is a 3D editor and command generator for Minecraft's display entities, enabling you to bring custom 3D models into your Minecraft worlds without the use of mods or resource packs.
- [MapartCraft](https://rebane2001.com/mapartcraft/)
  - MapartCraft is the do-it-all site for Mapart, where you can upload an image and customize the dithering, size, blocks used, etc. before either saving the preview image or downloading the map as a Schematic (.nbt) or Data (.dat) file.
- [MCStacker](https://mcstacker.net/)
  - MCStacker is an online Command/NBT generator that allows you to choose the command and features, and then generates it for you.
- [Minecraft-ArmorStand](https://haselkern.com/Minecraft-ArmorStand/)
  - Minecraft-ArmorStand is an excellent way to pose armor stands and test out armor and tags before generating a command for them.
- [NBT Minifier](https://autocompressor.net/tools/nbt-minifier)
  - NBT Minifier is an experimental compressor to remove un-needed/blank/duplicate tags from SNBT, such as ones added by ItemizerX.
- [Obj To Schematic](https://objtoschematic.com/)
  - Obj To Schematic converts 3D model files such as `.obj` and `.glb` files into `.schematic`, `.schem`, `.litematic`, `.nbt` and `.json` files, with tons of settings to tweak and customize the output.
  - *There is also an (older) application version of this site available at [LucasDower/ObjToSchematic](https://github.com/LucasDower/ObjToSchematic) on GitHub.*
- [R74n](https://r74n.com/)
  - R74n is an interesting amalgamation of resources and tools for Minecraft and other things. Of particular note is the hidden [HD Heads](https://r74n.com/mc/heads) page, as well as the [Box Page](https://r74n.com/box) containing the `/give` commands and NBT for a number of Shulker Kits.
- [webNBT](https://irath96.github.io/webNBT/)
  - webNBT lets you upload any .nbt file and edit it just as you would with an External Editor such as NBT Studio.

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


