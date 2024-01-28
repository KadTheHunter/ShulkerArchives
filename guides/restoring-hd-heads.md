---
layout: single
title: "Restoring HD Heads"
toc: true
toc_sticky: true
toc_label: Table of Contents
toc_icon: scroll
---
# HD Heads Background
Prior to Minecraft 1.17, HD Heads were custom player heads with high resolution textures that were viewable in vanilla minecraft.

In the Caves & Cliffs 1.17 update, Mojang patched the ability to both create and view HD Heads; Despite this, the HD Heads themselves still exist, as do their textures.

While creating new HD Heads is currently impossible (due to the exploit used to upload textures to the Minecraft: Education Edition website being patched), viewing them is simply a matter of unblocking the Minecraft: Education Edition domain, so that the Minecraft client can retrieve the HD Heads textures.

To do this, a Fabric Mod called [Custom Skin Loader](https://modrinth.com/mod/customskinloader) (CSL) is used, which allows loading skin textures from anywhere on the internet-- from the default list of sites, to custom entries added by you.

By default, CSL is painfully slow at loading *any* textures, HD or otherwise. Fortunately, it can be sped up significantly with this guide!

# Speeding up CSL
This is a fairly simple process; All you'll need is File Explorer, and Notepad.

Navigate to `.minecraft/CustomSkinLoader/` and open `CustomSkinLoader.json` in Notepad.

Modify the `"loadlist"` entry, so that it looks like the following:

```
"loadlist": [
{
"name": "Mojang",
"type": "MojangAPI",
"apiRoot": "https://api.mojang.com/",
"sessionRoot": "https://sessionserver.mojang.com/"
},
{
"name": "LocalSkin",
"type": "Legacy",
"checkPNG": false,
"skin": "LocalSkin/skins/{USERNAME}.png",
"model": "auto",
"cape": "LocalSkin/capes/{USERNAME}.png",
"elytra": "LocalSkin/elytras/{USERNAME}.png"
}
],
```

Doing this removes the default lists of sites provided by CSL, and thus the functionality of loading skins from the sites CSL advertises, instead reducing it to the full (unblocked) Mojang API and local files.

# Additional Notes
- I am not entirely sure *why* CSL is so slow by default, but I suspect it's because CSL queries all the entries listed in `CustomSkinLoader.json` for each and every texture it needs to load, which includes your skin, other players skins, and any Player Heads loaded. Additionally, it doesn't query all the entries at once, but one at a time (which makes sense to some degree, as it seems to stop querying once a texture is acquired, and it would be wasteful to query any additional entries when the texture has already been acquired), which surely increases the time taken. *Additionally,* additionally, the reason you could open a shulker of heads and half would load their textures while the other half remains blank is because while CSL seems to query entries one at a time per texture, it can query for multiple textures at once. This results in ~27 queries being sent to a single entry at once, which (depending on the entry) will eventually trigger a ratelimit, essentially resulting in a cutoff. It's been some time since I did my research on this, but I believe the reason such a ratelimit/cutoff doesn't occur when the entries are reduced to the Mojang API and Local Skins, is because Mojang has a far higher ceiling for requests than other entries, allowing for many more simultaneous queries.
- It is *theoretically* possible to load textures from other sources, such as GitHub or Discord; However, I have absolutely no clue how one would go about this, or if it even *is* possible. Even if you could, it would be of little use for HD Heads, as other CSL users would need to modify their `CustomSkinLoader.json` to include your source in order to see your HD Heads.
- The phenomenon of HD Heads seems to be fairly unknown to the larger Minecraft community. Aside from a couple of obscure reddit posts and YouTube videos (most have which have been deleted or made private), an old TotalFreedom Forum thread, and a random blog post, there's virtually no discussion of them or even any indication they *exist*. That being said, I'm going to compile a list of the media that *does* still exist below:
  - [Get Custom Modded Heads](https://totalfreedom.boards.net/thread/63771/get-custom-modded-heads) TotalFreedom Forum Thread
  - [Cracking the mystery of Minecraft HD Heads](https://hans5958.github.io/blog/minecraft-hd-heads/) Blog Post
  - [HD Player Heads Java 1.16.4](https://www.youtube.com/watch?v=iWB9rzQpLu0) YouTube Video
  - [Tiny Blocks Blast Furnace HD Player Heads](https://www.youtube.com/watch?v=UHNvxo2ULD8) YouTube Video
  - [Tiny Blocks Lit Blast Furnace HD Player Heads](https://www.youtube.com/watch?v=rAXEkgt9njo) YouTube Video
  - [Dream Logo HD Player Heads](https://www.youtube.com/watch?v=lJ5yKAy6DHw) YouTube Video
  - [Tiny Blocks Melon HD Player Heads](https://www.youtube.com/watch?v=Keze7m0Dcvo) YouTube Video
  - [Make HD and Transparent Heads Minecraft Java 1.16.x](https://www.youtube.com/watch?v=mnAkRALt09k) YouTube Video
  - [HD Heads Generator](https://www.reddit.com/r/gamergeeksnz/comments/kldiip/hd_heads_generator/) Reddit Thread
  - [How to get HD Heads](https://www.reddit.com/r/Minecraft/comments/aqlzis/how_to_get_hd_heads/) Reddit Thread
  - [r74n.com Heads](https://r74n.com/mc/heads) Head SNBT Collection