# The Shulker Archives Guidelines
This document is intended to serve as a reference for Kaddicus (and any future Archivists) for the process of adding new entries.

If you have tools or suggestions to improve any aspect of the process, please send them to [Discord](https://discord.gg/cfq25qURfv) or [Issues](https://github.com/KadTheHunter/ShulkerArchives/issues).

## Note
There will always be exceptions to the guidelines listed. 

There will always be that one kit added to Archivist Picks that doesn't quite meet the standards, always that one Item that could technically fit into a different category, always some sort of exception. At the end of the day, it is up to the current Archivist(s) to use their experience with the Archives to properly source, qualify, categorize and add new entries; These guidelines just serve as loose markings to prevent _too_ much variance.

## Prerequisites
- [Minecraft](https://www.minecraft.net/en-us)
  - [Fabric Loader](https://fabricmc.net/)
    - [NBT Editor](https://modrinth.com/mod/nbt-editor)
    - [QuickCoords Copy](https://github.com/KadTheHunter/QuickCoordsCopy/releases/latest) (Kaddicus' Fork)
      - Refer to [Resources](#resources) for the QCC command format
- [WebStorm](https://www.jetbrains.com/webstorm/)
  - [CSV Editor Plugin](https://plugins.jetbrains.com/plugin/10037-csv-editor)
- [GitHub Account](https://github.com/)
  - [Access to The Shulker Archives Repository](https://github.com/KadTheHunter/ShulkerArchives)
- [Web Browser](https://www.mozilla.org/en-US/firefox/new/) (Firefox preferred)

## Sourcing Entries
There are three ways to source entries:
1. Submitted Entries - These are entries sent in by the community.
2. Ripped Entries - These are entries ripped from a server, typically done in bulk from a Plot or other large collection. Ripped entries are not as common nowadays, but do still exist.
3. Found Entries - These are entries found on servers such as NBT Archives, and saved locally.

All sourced entries **MUST** be checked against the Database before proceeding to the next steps.

## Qualifying
There are several layers of qualification. If a sourced entry fails any layer, it may be immediately discarded.

Entries must have:
1. Components
   - Any valid component counts.
2. Quality
   - This is entirely subjective to the Archivists definition of quality, but should generally be used to weed out anvil renames, enchant spam, and junk items.
3. Uniqueness
   - Kits must be at least somewhat unique, whether in idea or presentation. A box of max enchant Netherite armor, or a box of "Unobtainable" or "Illegal" items is **NOT** unique.
4. No Broken/Outdated Data
   - This refers to older Name/Lore that has been corrupted, and Sign, Potion or other NBT data that is from an older version. Such data may be repaired, if worthwhile.
   - This also refers to data from pre-1.20.5 that does not port properly, e.g. Level 0 Enchantments, improperly written Attribute Values, missing Entity IDs, etc.
5. Correct Author
   - This refers to the Author, if provided. Some players have attempted to claim credit for popular items in the past, by modifying the authors username to their own.

## Categorizing Entries
All entries will fall into one of the following categories:

### Kits
#### PvP
Kits may be categorized as PvP if they meet all the following requirements:
- Contains at least one Melee Weapon (or Item intended as a Melee Weapon) that is intended for PvP combat
- Contains at least two pieces of Armor that are intended for PvP combat (Player Heads and Elytra do not count as armor on their own, but do count when paired with other armor pieces)
  - _NBT PvP often does not require armor, so this requirement can be waived under the right circumstances._
- Items must be themed and/or arranged in a way that indicates they form a Kit, not just a random collection of PvP items

#### PvP (Related)
Kits may be categorized as PvP (Related) if they meet the following requirement but failed the PvP requirements:
- Contains items meant to deal or negate damage

#### Abuse
Kits may be categorized as Abuse if they meet all the following requirements:
- Contains items used to Troll, Exploit, Attack or otherwise "Abuse" on servers and worlds
- Primary focus is on Trolling/Exploiting

#### Utilities
Kits may be categorized as Utilities if they meet the following requirement:
- **Only** contains items that provide useful features, tools or services to the player

#### Misc. Functional
Kits may be categorized as Misc. Functional if they meet the following requirement but failed other categories requirements:
- Primarily consists of items that are "Functional" e.g. Command Blocks, Spawn Eggs, etc.

#### Lore
Kits may be categorized as Lore if they meet all the following requirements:
- Contains at least one item with >5 lines of lore _OR_ two items with >3 lines of lore
- Items are stylized and/or arranged in a way that indicates they form a Kit, not just a random collection of lore items

#### Random
Kits may be categorized as Random if the items within have no lore and/or have no relation to one-another

#### Misc. Non-Functional
Kits may be categorized as Misc. Non-Functional if they do not fall into Lore or Random.

### Items
#### Melee Weapons
Items may be categorized as Melee Weapons if they meet the following requirement:
- Is intended to be used as a Melee Weapon

#### Ranged Weapons
Items may be categorized as Ranged Weapons if they meet the following requirement:
- Can shoot a projectile or be thrown as a projectile to damage another Player or Entity

#### Arrows
Items may be categorized as Arrows if they meet the following requirement:
- Is an arrow intended for use in combat

#### Armor
Items may be categorized as Armor if they meet the following requirement:
- Is intended to protect the wearer from damage when worn

#### Potions
Items may be categorized as Potions if they meet all the following requirements:
- Is a Potion, Splash Potion, Lingering Potion or Suspicious Stew
- Applies one or more effects to the target player when drunk or thrown

#### Spawn Eggs
Items may be categorized as Spawn Eggs if they meet all the following requirements:
- Is a Spawn Egg or Mob Spawner that does not fall into the Abuse or Utilities categories
- Spawns a mob or entity other than that which it would normally spawn

#### Elytra
Items may be categorized as Elytra if the meet all the following requirements:
- Is an Elytra, or has the Glider properties
- Is intended to be used as an Elytra

#### Fireworks
Items may be categorized as Fireworks if they meet all the following requirements:
- Is a Firework
- Contains at least one custom Explosion

#### Abuse
Items may be categorized as Abuse if they meet the following requirement:
- Is used to Troll, Exploit, Attack or otherwise "Abuse" on servers and worlds

#### Misc. Functional
Items may be categorized as Misc. Functional if they meet the following requirement but failed other categories requirements:
- Is a "Functional" item e.g. Command Blocks, Armor Stands, Spawn Eggs, etc.

#### Lore
Items may be categorized as Lore if they meet the following requirement:
- Has >3 lines of lore

#### Misc. Non-Functional
Items may be categorized as Misc. Non-Functional if they do not fall into Lore, and are not "Functional"

### Books
#### Utility
Books may be categorized as Utility if they meet the following requirement and do not fall into Abuse:
- Contains at least one command click_event that provides a useful service to the player

#### Abuse
Books may be categorized as Abuse if they meet the following requirement:
- Is used to Troll, Exploit, Attack or otherwise "Abuse" on servers and worlds

#### Misc. Functional
Books may be categorized as Misc. Functional if they do not fall into Utility or Abuse, but have command click_events or other functionality

#### Fiction
Books may be categorized as Fiction if they meet the following requirement:
- Is a work of Fiction, original or otherwise

#### Non-Fiction
Books may be categorized as Non-Fiction if they meet the following requirement:
- Is a work of Non-Fiction, original or otherwise

#### Misc. Non-Functional
Books may be categorized as Misc. Non-Functional if they do not fall into any other categories

### Collections
Entries that are part of a larger line or group of entries are typically flagged as Collections, and separated from the main body of the Archives.

Collections have similar standards as Archivist Picks, but somewhat looser; While entries in Collections must meet a certain level of quality, the primary focus is separating large "clumps" of entries from the larger Archive, making it easier to find entries from popular series.

New Collections can be formed if all the following requirements are met:
- All entries are linked to one another
- There is 4+ existing entries, or sufficient reason to believe there will be more coming in the future

Entries can be added to existing collections if the following requirement is met:
- It is linked to or part of an existing Collection

## AP Guidelines
Particularly good entries can be flagged as Archivist Picks, with copies placed in the Archivist Pick sheet.

In order to be an Archivist Pick, an entry must meet the following requirements:
- Kits must be nicely arranged and not in a jumble
- Items must fulfill one or more of the following:
    - Has lengthy and/or well done lore, properly styled and relatively void of common tropes
    - Is a useful utility/tool, properly functioning and usable
    - Is a top of the line PvP item; No common or overused Weapons/Armor
    - Has a generally high level of quality

It's important to note that Archivist Picks are the cream of the crop; It's entirely possible for an entry to meet the above requirements, and still not be an Archivist Pick. The guidelines listed are exactly that: guidelines. If an entry meets them, then it's possible for it to be an Archivist Pick, but is still entirely up to the Archivist to make that decision, using their experience with the Archives to know if it really _is_ an Archivist Pick.

If an entry is selected as an Archivist Pick, place a _copy_ of it in the Archivist Pick sheet, after first adding it to the appropriate sheet in the main Archive.

## Adding Entries
Adding new entries requires adding them to the correct location on the map, copying the coordinates and entering them along with the relevant information in the Database.

### Map
1. Locate the appropriate location for the entry
2. Find the next available barrel
3. Place the entry in the exact center of the barrel
4. Modify the sign to have the entries name in green (`§a`), and the authors name in light gray italic (`§7§o`). 
   1. The entry name can use up to three lines of the sign. 
   2. The authors name is never placed higher than the third line. 
   3. Multiple authors should be separated by a comma, with one author per line. 
5. Decide if the entry is an Archivist Pick, following [AP Guidelines](#ap-guidelines)
6. Begin the process of [Database](#database)

### Database
1. Position yourself in front of the barrel so that your head is level with the relevant sign, with one block of air between you and the sign
2. Copy the coordinates using QuickCoordsCopy
3. Test the copied coordinates to ensure they are proper
4. If you are adding more than one entry, place a blank line between the existing database and your new entries, so you can easily see where the new entries begin.
5. Switch to WebStorm, and in the CSV file add the new entry in the format of
    ```CSV
    Name,Author,Teleport Command,Notes,Category,Entry Type
    ```
    Notes should be left blank unless the entry contains NSFW or is an Archivist Pick, in which case you can add `NSFW` or `Archivist Pick` respectively.
6. When finished adding entries, begin the process of [Changelog](#changelog)
7. After finishing the Changelog, convert the contents of the CSV file to JSON using [ConvertCSV.com](https://www.convertcsv.com/csv-to-json.htm).
   1. Ensure that under Step 3, "Consider value of NULL in CSV to be null in JSON" is unchecked. This option has been known to cause issues in the past.
   2. Under Step 5, select "CSV to JSON Array". Copy and paste the contents into `/assets/database.json`

### Changelog
1. Open or create the relevant Changelog (`/releases/vX.X.X/Changelog.md`)
2. Copy and paste the contents of the Changelog Template, located in `/releases/`
3. Copy and paste all the new entries to `changelog.csv` located in `/scripts/`, then run `changelog.py`
4. The script will output the entries sorted by Entry Type, with proper formatting applied to all. Simply copy and paste each entry type into its appropriate place in the Changelog.
   1. If an entry is a Collection, it will be printed at the bottom of the script, and you will need to cherry-pick them by Collection. Refer to older changelogs for examples.
   2. If an entry is an Archivist Pick, you will need to manually cherry-pick them from each entry type, and paste them into the relevant sections of Archivist Picks. Refer to older changelogs for examples.
5. When finished writing the Changelog, remove the blank line(s) from the CSV file
6. Return to step 7 of [Database](#database)

## Resources
The `quickcoordscopy.properties` format is as follows:

Main Archive:
```javascript
formatting=/tp @s $x.5 $y $z.5 180 0
```

Collections:
```javascript
formatting=/tp @s $x.5 $y $z.5 0 0
```

The `.5` ensures that users will be centered when teleporting.

In the past, $LRSnap was used instead of a hardcoded Yaw coordinate, but this was incredibly buggy, and is also no longer needed due to all entries being either a `180` or `0` Yaw.

## Rambling & Notes / From the First Archivist "Kad"
_November 3rd, 2024_

Deciding what gets accepted and what gets rejected is tough. It's even more tough when you have to deliver a rejection to an author who, despite their kit being objectively bad, has clearly spent some time making it and tried their hardest.

But it has to be done.

You may ask, "but shouldn't all entries be accepted, if this is truly an archive?", and the answer is... yes, from a certain point of view, but no, from my point of view.

Using the Merriam-Webster dictionary, the definition of "Archive" is:
> 1
: a place in which public records or historical materials (such as documents) are preserved
<br> 2
: a repository or collection especially of information

Collecting _all_ the relevant materials is not mentioned. While many other Archives seek to preserve as much as possible, I choose to take a different approach.

The Shulker Archives exists to keep copies of Kits, Items and Books that are not (relatively) easily recreated. Ideas, artwork, utilities etc. that cannot be easily recreated by a player or even dreamed up by another player, belong here.

With this in mind, it is only logical to reject kits whose contents consist of armor that simply have every enchantment applied at the max level, or items with barely any customization applied. These things can be easily recreated by even the most novice of players; Simply hand them a copy of NBT Editor, or direct them to MCStacker, and they can create such items in just a few clicks.

You may also ask, "but don't such simple, un-unique entries exist in the Archives anyway? where is the line drawn?", and you would be right.

In v1 of The Shulker Archives, a substantial amount of- for lack of a better term- _shit-tier_ entries were accepted.

In v2 of The Shulker Archives, the amount of these entries is substantially less, but they are still present. I have no real excuse or explanation for why they should be there.

The best I can say, is that they stand right on the border between good and bad. Had they one more terrible quality I would reject them, but they do not, and so I have chosen to accept them despite their seeming violation of these guidelines.

Other, future, Archivists might take a different approach, and allow more or less of these poor quality, un-unique, easily recreated entries into the Archives; That is their prerogative.

I hope however, that they will interpret these Guidelines as I do, and they will accept and reject as I have.

I hope too, that users of The Shulker Archives will find these Guidelines useful in better understanding why entries are accepted and rejected as they are, and how they are sorted into the categories they are.

- Kaddicus