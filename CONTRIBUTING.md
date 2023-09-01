# Prerequisites
Before contributing, please ensure you have the following:
- JetBrains WebStorm 2023 **OR** Visual Studio Code 
- The entry templates at the top of [index.html](https://github.com/KadTheHunter/ShulkerArchives/blob/master/index.html#L15) for Kits, [Items.html](https://github.com/KadTheHunter/ShulkerArchives/blob/master/html/Items.html#L15) for Items, [Books.html](https://github.com/KadTheHunter/ShulkerArchives/blob/master/html/Books.html#L15) for Books and [Unnamed.html](https://github.com/KadTheHunter/ShulkerArchives/blob/master/html/Unnamed.html#L15) for Unnamed Kits saved in some way, preferably as Code Snippets/Live Templates
- Minecraft with the [NBT Editor](https://modrinth.com/mod/nbt-editor/versions) mod installed
- File Explorer

# Adding Kits
## File Names
File names should follow the actual name seen in-game as closely as possible, minus spaces, apostrophes, and illegal chars. A shulker box labeled "Kad's Box Of Flags" should be exported as "KadsBoxOfFlags", etc.

There are extensions and exceptions to this rule:

### Extensions
- Kits with version numbers in their name **must** have the version numbers in the file name. "Example Kit v1.2.3" should be exported as "ExampleKitv1.2.3" **NOT** "ExampleKit", "ExampleKitv123" or "ExampleKitv1_2_3"; If the version number is not in the name (but is elsewhere in the Kit/on the Item) you do not *have* to add it in the filename, but it is still recommended that you do.
- All file names must be in english *characters*. If a name is in another alphabet, translate it to english (literal or transliteral) as best you can, online tools are permitted.

### Exceptions
- Kits whose names are suffixed with the name of the author may be exported without that suffix, *provided* that the kits name is unique. Examples are as follows:
  - "King of The Gods V2 by Z_cu" can be exported as "KingOfTheGodsV2", because the name is unique enough that it likely will not conflict with other entries.
  - "Spawn Eggs by Chargefruit" must be exported as "SpawnEggsbyChargefruit", because the name is not unique enough, and has a high likelihood of conflicting if there is no additional identifier such as the author (in this case, "by Chargefruit").
  - When a box has no name/unique name, but contains only a single item that *does* have a unique name, that items name may be used instead.

## Entry Names
Entry names should match the in-game name *and* file name as closely as possible, including any characters found on a standard english keyboard, excluding any characters *not* found on a standard english keyboard. 
- All extensions and exceptions for File Names apply to Entry Names as well.

## Authors
If the author of a kit is known, their IGN should be placed in the Author field. If the author is unknown, simply put 'Unknown Author'.

If an author has IGN history, you may use any of the following in the Author field:
- IGN Credited within the Kit/Item
- Current IGN
- IGN at the time of Kit/Item Creation

To check IGNs and IGN History, use a site such as [NameMC](https://namemc.com/), and query their IGN.

## Descriptions
Descriptions should be a clear, concise sentence that describes the content of a kit, features of an item or purpose of a book.

### Include
- Information on the theme, contents, and purpose
- Highlight of anything particularly unique or interesting

### Avoid
- More than 2 sentences
- Unimportant details (such as filler, box color, etc.)
- Any lengthy history or detail

You may use *very limited* amounts of Italic `<i></i>`, and Links `<a href=""></a>` in descriptions. Other HTML styling tags such as Bold `<b></b>`, Underlined `<u></u>`, etc. are allowed, but it is preferred you do not use them.
- If you do use Links, ensure that `target="_blank" rel="noopener noreferrer"` is included after the `href=""`; This ensures that links will open in a new tab when clicked.

## Tags
Tags should act as an even more concise version of the description, by breaking it down into key features, and assigning tags accordingly. 

Unlike descriptions, Tags should avoid being unique to each kit; Check other entries tags to get an idea of what tags are in use currently, and how they can be applied to the entry you are tagging.

You may create new unique tags as needed, but *please* make sure no other existing tag applies before doing so.

- All tags must be separated by a comma and space (`, `)
- No more than three tags should be applied to any given entry; In some special cases four will be allowed, but please avoid adding a fourth in general
- Tags should be listed in order of relevancy. A kit of leather armor and diamond weapons, with aquatic themed lore and name but little enchantment or attribute modification should be tagged first with 'Themed', and second with 'PvP'; No other tags directly apply, so no more are added.
- Items that are exported individually but combined form a set should be tagged with 'Set'.
## .nbt links
.nbt links point directly to the .nbt file to download. Using the templates linked above, all you will need to do is fill in the file name itself. 

Please double-check and ensure that the filename is correct; They are case sensitive, so a swapped capital/lowercase letter will break things!

# Code Contributions
Code contributions rather ironically follow a less strict set of guidelines than Kit Entries; Below is a short list of expectations for contributed code:
- Tab Size/Indentation must be 2 spaces
- 'Script code must be commented/documented
- CSS styles must be placed in the appropriate part of the file; See the [comment dividers](https://github.com/KadTheHunter/ShulkerArchives/blob/master/assets/main.css#L27) for reference.
  - If there is not an existing category for your style, please insert a new one where you think appropriate.
- Links **must** use `target="_blank" rel="noopener noreferrer"` when linking to external pages.

Everything else expected falls under the header of 'Common Sense'; Use best practices, don't format your braces and brackets like a retard, check your spelling and grammar, test your changes before submitting them, etc.