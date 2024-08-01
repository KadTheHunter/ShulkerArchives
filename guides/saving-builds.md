---
layout: single
title: "Saving Builds"
toc: true
toc_sticky: true
toc_label: Table of Contents
toc_icon: scroll
---

# WorldEdit/Litematica
One of the simplest ways of saving builds is with WorldEdit or Litematica schematics.

The instructions differ based on method, but it is recommended to use WorldEdit if you have access to download the generated `.schematic` files; Otherwise, use Litematica.

Below are some general pointers to help you out:
- Always set the first position at the top, and second position at the bottom. This ensures when you load and paste it elsewhere, you don't accidentally sink it into the ground!
- Take note of the cardinal/extracardinal directions either through F3 or a Map mod like [Xaero's Minimap](https://modrinth.com/mod/xaeros-minimap), and be consistent with what direction your build will be pasted in. If you set Position 1 to the North-East and Position 2 + Copy in the South-West, the build will always paste in to the North-East.
- Use a mod such as [BlockMeter](https://modrinth.com/mod/blockmeter) to measure builds, and make sure you're copying the full build, as well as not copying excess air.
- When using WorldEdit, add the `-a` flag to your `//paste` command; By ignoring air blocks, the time it takes to paste in can be drastically reduced!
- If you're saving a build with floating objects (e.g. signs, flowers, sand, etc.), use the command `//perf neighbors off` to disable neighboring block updates.
- When in doubt, check the docs! WorldEdits documentation can be found on [EngineHub's site](https://worldedit.enginehub.org/en/latest/), and Litematica's documentation on the [Litematica GitHub](https://github.com/maruohon/litematica/wiki)

# Chunk Ripper
The Chunk Ripper is an effective, but rather extreme method of saving builds. It will copy and save the block contents of entire chunks locally, and then paste them into a local world.

This method will properly capture NBT data, such as chests, barrels, shulkers, signs, entities, etc. Despite this, it is not recommended to be used for saving NBT data unless no other options are available.

To get started, download the [WorldTools](https://modrinth.com/mod/worldtools) mod for Fabric or Forge. Make sure to get v1.1.1 or newer, because v1.0.0 has some very annoying bugs!

Join the server you want to copy chunks from, and teleport to the area you wish to save. Once there, press `F12` to start the WorldTools capture.

Walk or fly around the entire area to be sure that everything you want to save is captured. Open chests to save their contents. When you're satisfied with the capture area, press `F12` again to end the capture and save to a local world.

WorldTools will save the chunks to both a local world folder and a `.zip` file inside of `.minecraft/saves/`; Join the local world to make sure everything saved properly.

Congrats, you've now ripped chunks from a multiplayer server to your local worlds!
