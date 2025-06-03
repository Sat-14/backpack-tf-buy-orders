# Backpack.tf Buy Order Creator

A simple Python tool to automatically create buy orders on backpack.tf using their v2 API. Perfect for traders who want to automate their buying process!

**⚠️ IMPORTANT: You need keys/metal in your TF2 backpack to make buy orders!**

## Features

- ✅ **Simple Configuration** - Easy JSON format, no complex API knowledge needed
- ✅ **Batch Creation** - Create multiple buy orders at once
- ✅ **Smart Validation** - Checks your config before sending to API
- ✅ **Clear Error Messages** - Helpful tips when things go wrong
- ✅ **Professional Killstreaks** - Full support for unusual effects, killstreaks, etc.

## Complete Setup Guide (For Beginners)

### Step 1: Install Python (If You Don't Have It)

#### For Windows:
1. Go to [python.org](https://www.python.org/downloads/)
2. Click the big yellow **"Download Python"** button
3. **IMPORTANT**: When installing, check the box that says **"Add Python to PATH"**
4. Click "Install Now"
5. Wait for installation to complete

#### For Mac:
1. Go to [python.org](https://www.python.org/downloads/)
2. Download the macOS installer
3. Open the downloaded file and follow the installer
4. Python will be installed automatically

#### For Linux:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Step 2: Verify Python Installation
1. Press `Windows Key + R` (Windows) or open Terminal (Mac/Linux)
2. Type `cmd` and press Enter (Windows) or just use Terminal (Mac/Linux)
3. Type: `python --version` and press Enter
4. You should see something like "Python 3.x.x"
5. If it says "command not found", restart your computer and try again

### Step 3: Download This Tool

#### Option A: Download ZIP (Easiest)
1. Click the green **"Code"** button at the top of this page
2. Click **"Download ZIP"**
3. Extract the ZIP file to your Desktop or Documents folder
4. Remember where you extracted it!

#### Option B: Use Git (If You Know How)
```bash
git clone https://github.com/yourusername/backpack-tf-buy-orders.git
cd backpack-tf-buy-orders
```

### Step 4: Install Required Libraries
1. Open Command Prompt (Windows) or Terminal (Mac/Linux)
2. Navigate to the folder where you extracted the files:
   ```bash
   cd Desktop/backpack-tf-buy-orders-main
   ```
   (Replace with your actual folder path)
3. Install the required library:
   ```bash
   pip install requests
   ```
4. Wait for it to say "Successfully installed"

### Step 5: Get Your Backpack.tf Access Token
1. Go to [backpack.tf](https://backpack.tf) and log in with Steam
2. Click your profile picture in the top right
3. Click **"Settings"**
4. Scroll down to the **"Advanced"** section
5. Find **"Third party access token"**
6. Copy this token (it looks like: `xxxxxxxxxxxxxxxxxxxxxxxxx`)
7. **DO NOT share this token with anyone!**

### Step 6: Create Your First Buy Order
1. In your command prompt/terminal, navigate to the tool folder
2. Run the script for the first time:
   ```bash
   python backpack_buy_orders.py
   ```
3. It will create a file called `buy_orders.json`
4. Open this file with any text editor (Notepad on Windows, TextEdit on Mac)

### Step 7: Edit Your Configuration
1. Open `buy_orders.json` in a text editor
2. Replace `"YOUR_ACCESS_TOKEN_HERE"` with your actual token from Step 5
3. Edit the buy orders to match what you want to buy

**Example for beginners:**
```json
{
  "access_token": "your_token_goes_here_without_quotes",
  "buy_orders": [
    {
      "comment": "Buying Tour of Duty Ticket",
      "metal": 1.33,
      "defindex": 725,
      "quality": "unique"
    }
  ]
}
```

### Step 8: Run the Tool
1. Save the `buy_orders.json` file
2. In your command prompt/terminal, run:
   ```bash
   python backpack_buy_orders.py
   ```
3. The tool will show you what it's going to create
4. Type `y` and press Enter to confirm
5. Your buy orders will be created!

## Requirements

- Python 3.6 or higher
- `requests` library (`pip install requests`)
- Team Fortress 2 items (keys/metal) in your Steam inventory
- Backpack.tf account with access token

## Detailed Configuration Guide

### Basic Buy Order Format

Every buy order needs these **required fields**:

```json
{
  "comment": "Description of what you're buying",    // Required: Shows in your listing
  "defindex": 725                                    // Required: Item's unique ID number
}
```

And at least **one price field**:

```json
{
  "keys": 2,        // Optional: Number of Mann Co. Keys
  "metal": 5.33     // Optional: Refined metal amount
}
```

### Complete Field Reference

| Field | Required | Type | Description | Example |
|-------|----------|------|-------------|---------|
| `comment` | ✅ Yes | String | Listing description (max 200 chars) | `"Buying Strange Scattergun"` |
| `defindex` | ✅ Yes | Number | Item's unique identifier | `13` |
| `keys` | ⚠️ One price required | Number | Mann Co. Keys to offer | `2` |
| `metal` | ⚠️ One price required | Number | Refined metal to offer | `5.33` |
| `quality` | ❌ Optional | String | Item quality | `"strange"` |
| `craftable` | ❌ Optional | Boolean | Is item craftable? | `true` |
| `level` | ❌ Optional | Number | Specific item level | `100` |
| `attributes` | ❌ Optional | Array | Special attributes (killstreaks, etc.) | See examples below |

### Supported Qualities

| Quality Name | Number | Description |
|--------------|--------|-------------|
| `"normal"` | 0 | Normal quality (gray text) |
| `"genuine"` | 1 | Genuine quality (dark green) |
| `"vintage"` | 3 | Vintage quality (blue) |
| `"unusual"` | 5 | Unusual quality (purple) |
| `"unique"` | 6 | Unique quality (yellow) - **Default** |
| `"community"` | 7 | Community quality (green) |
| `"self-made"` | 9 | Self-Made quality (green) |
| `"strange"` | 11 | Strange quality (orange) |

### Price Format Examples

```json
// Keys only
{
  "comment": "Buying Unusual Hat",
  "keys": 50,
  "defindex": 123
}

// Metal only  
{
  "comment": "Buying Tour of Duty Ticket",
  "metal": 1.33,
  "defindex": 725
}

// Keys + Metal
{
  "comment": "Buying Strange Weapon",
  "keys": 2,
  "metal": 5.66,
  "defindex": 13
}
```

**Metal Format Guide:**
- `0.11` = 1 Scrap Metal
- `0.33` = 1 Reclaimed Metal  
- `1.00` = 1 Refined Metal
- `1.33` = 1 Refined + 1 Reclaimed
- `1.44` = 1 Refined + 1 Reclaimed + 1 Scrap

## Common Items & Defindexes

### Currency Items
| Item | Defindex | Typical Price |
|------|----------|---------------|
| Tour of Duty Ticket | 725 | 1.33 metal |
| Mann Co. Supply Crate Key | 5021 | N/A (currency) |
| Refined Metal | 5002 | 1.00 metal |
| Reclaimed Metal | 5001 | 0.33 metal |
| Scrap Metal | 5000 | 0.11 metal |

### Popular Weapons
| Item | Defindex | Strange Version |
|------|----------|-----------------|
| Scattergun | 13 | 200 |
| Rocket Launcher | 18 | 205 |
| Flamethrower | 21 | 208 |
| Grenade Launcher | 19 | 206 |
| Shotgun | 9 | 199 |
| Pistol | 23 | 209 |
| Medigun | 29 | 211 |
| Sniper Rifle | 14 | 201 |
| Knife | 4 | 194 |

### Killstreak Kits
| Kit Type | Defindex |
|----------|----------|
| Professional Killstreak Kit | 6527 |
| Specialized Killstreak Kit | 6523 |
| Killstreak Kit | 6522 |

*Find more defindexes: [TF2 Schema API](https://wiki.teamfortress.com/wiki/WebAPI/GetSchema)*

## Advanced Items (Killstreaks, Unusuals, etc.)

### Professional Killstreak Example

```json
{
  "comment": "Buying Pro KS Shotgun Kit - Hot Rod + Cerebral Discharge",
  "keys": 3,
  "defindex": 6527,
  "quality": "unique",
  "attributes": [
    {"defindex": 2025, "float_value": 3},    // Professional Killstreak tier
    {"defindex": 2013, "float_value": 2003}, // Cerebral Discharge effect
    {"defindex": 2014, "float_value": 7},    // Hot Rod sheen  
    {"defindex": 2012, "float_value": 9}     // Target weapon: Shotgun
  ]
}
```

### Unusual Hat Example

```json
{
  "comment": "Buying Unusual Team Captain - Burning Flames",
  "keys": 150,
  "defindex": 378,
  "quality": "unusual",
  "attributes": [
    {"defindex": 134, "float_value": 13}     // Burning Flames effect
  ]
}
```

### Strange Weapon with Parts

```json
{
  "comment": "Buying Strange Scattergun with Kills + Dominations",
  "keys": 5,
  "defindex": 200,
  "quality": "strange", 
  "attributes": [
    {"defindex": 380, "float_value": 0},     // Strange Part: Kills
    {"defindex": 382, "float_value": 31}     // Strange Part: Dominations
  ]
}
```

## Complete Attributes Reference

### Killstreak Attributes

#### Killstreak Tiers (defindex 2025)
| Value | Type |
|-------|------|
| `1` | Killstreak |
| `2` | Specialized Killstreak |
| `3` | Professional Killstreak |

#### Killstreak Effects (defindex 2013) - Professional Only
| Value | Effect Name |
|-------|-------------|
| `2002` | Fire Horns |
| `2003` | Cerebral Discharge |
| `2004` | Tornado |
| `2005` | Flames |
| `2006` | Singularity |
| `2007` | Incinerator |
| `2008` | Hypno-Beam |

#### Killstreak Sheens (defindex 2014) - Specialized & Professional
| Value | Sheen Name |
|-------|------------|
| `1` | Team Shine |
| `2` | Deadly Daffodil |
| `3` | Manndarin |
| `4` | Mean Green |
| `5` | Agonizing Emerald |
| `6` | Villainous Violet |
| `7` | Hot Rod |

#### Target Weapon (defindex 2012) - For Killstreak Kits
Use the defindex of the weapon the kit applies to (e.g., `9` for Shotgun, `13` for Scattergun).

### Unusual Effects (defindex 134)
| Value | Effect Name | Value | Effect Name |
|-------|-------------|-------|-------------|
| `6` | Purple Energy | `13` | Burning Flames |
| `7` | Green Energy | `14` | Scorching Flames |
| `8` | Purple Confetti | `15` | Searing Plasma |
| `9` | Pink Confetti | `16` | Vivid Plasma |
| `10` | Peace Sign | `17` | Sunbeams |
| `11` | Heart | `18` | Green Confetti |
| `12` | Question Mark | `29` | Stormy Storm |
| `703` | Disco Beat Down | `704` | Miami Nights |
| `720` | Stare From Beyond | `722` | Vicious Vortex |

*[Full list available on TF2 Wiki](https://wiki.teamfortress.com/wiki/Unusual)*

### Paint Colors (defindex 142 & 261)
| Value | Paint Name | Hex Color |
|-------|------------|-----------|
| `7511618` | Indubitably Green | `#729E42` |
| `4345659` | Zepheniah's Greed | `#424F3B` |
| `5322826` | Noble Hatter's Violet | `#51384A` |
| `14204632` | Color No. 216-190-216 | `#C8BED8` |
| `8208497` | A Deep Commitment to Purple | `#7D4071` |
| `13595446` | Mann Co. Orange | `#CF7336` |
| `10843461` | Muskelmannbraun | `#A57545` |
| `12955537` | Peculiarly Drab Tincture | `#C5AF91` |
| `6901050` | Radigan Conagher Brown | `#694D3A` |
| `8154199` | Ye Olde Rustic Colour | `#7C6C57` |
| `15185211` | Australium Gold | `#E7B53B` |
| `8289918` | Aged Moustache Grey | `#7E7E7E` |
| `15132390` | An Extraordinary Abundance of Tinge | `#E6E6E6` |
| `1315860` | A Distinctive Lack of Hue | `#141414` |

### Strange Parts (Multiple defindexes)
| Defindex | Part Name | Defindex | Part Name |
|----------|-----------|----------|-----------|
| `380` | Strange Part: Kills | `395` | Strange Part: Robots Destroyed |
| `382` | Strange Part: Ubers | `396` | Strange Part: Giant Robots Destroyed |
| `384` | Strange Part: Kill Assists | `397` | Strange Part: Cloaked Spies Killed |
| `385` | Strange Part: Sentry Kills | `398` | Strange Part: Health Dispensed |
| `386` | Strange Part: Sodden Victims | `399` | Strange Part: Teammates Extinguished |
| `387` | Strange Part: Spies Killed | `400` | Strange Part: Freezecam Taunt Appears |
| `388` | Strange Part: Heads Taken | `401` | Strange Part: Damage Dealt |
| `389` | Strange Part: Humiliations | `402` | Strange Part: Fires Survived |
| `390` | Strange Part: Gifts Given | `403` | Strange Part: Allied Healing Done |
| `391` | Strange Part: Deaths Feigned | `404` | Strange Part: Point Blank Kills |

### Halloween Spells
| Defindex | Spell Type | Values |
|----------|------------|--------|
| `1004` | Paint Spell | `0` = Die Job, `1` = Chromatic Corruption, `2` = Putrescent Pigmentation, `3` = Spectral Spectrum, `4` = Sinister Staining |
| `1005` | Footprint Spell | `1` = Team Spirit, `2` = Headless Horseshoes, `8421376` = Gangreen, `3100495` = Corpse Gray, `5322826` = Violent Violet, `13595446` = Rotten Orange, `8208497` = Bruised Purple |
| `1006` | Voices From Below | No value needed |
| `1007` | Pumpkin Bombs | No value needed |
| `1008` | Halloween Fire | No value needed |
| `1009` | Exorcism | No value needed |

### Weapon Wear (defindex 749) - For Decorated Weapons
| Value Range | Wear Level |
|-------------|------------|
| `0.0 - 0.199` | Factory New |
| `0.2 - 0.399` | Minimal Wear |
| `0.4 - 0.599` | Field-Tested |
| `0.6 - 0.799` | Well-Worn |
| `0.8 - 1.0` | Battle Scarred |

### Weapon Skins (defindex 834)
Use the skin's defindex as the value. Find skin defindexes in the TF2 schema.

### Special Attributes
| Defindex | Attribute | Usage |
|----------|-----------|-------|
| `229` | Craft Number | `{"defindex": 229, "value": 100}` - For craft #100 items |
| `2027` | Australium | `{"defindex": 2027}` - No value needed |
| `2053` | Festivized | `{"defindex": 2053, "float_value": 1}` - Makes item festivized |

### Example: Complete Unusual Hat
```json
{
  "comment": "Buying Painted Unusual Team Captain - Burning + Australium Gold",
  "keys": 200,
  "defindex": 378,
  "quality": "unusual",
  "attributes": [
    {"defindex": 134, "float_value": 13},    // Burning Flames effect
    {"defindex": 142, "value": 15185211}     // Australium Gold paint
  ]
}
```

### Example: Strange Weapon with Parts
```json
{
  "comment": "Buying Strange Scattergun - Kills + Damage + Dominations",
  "keys": 8,
  "defindex": 200,
  "quality": "strange",
  "attributes": [
    {"defindex": 380, "float_value": 0},     // Kills tracker
    {"defindex": 401, "float_value": 0},     // Damage dealt tracker  
    {"defindex": 388, "float_value": 31}     // Dominations tracker
  ]
}
```

### Example: Decorated Weapon
```json
{
  "comment": "Buying Factory New Killstreak Warhawk Rocket Launcher",
  "keys": 15,
  "defindex": 18,
  "quality": "unique",
  "attributes": [
    {"defindex": 834, "value": 276},         // Warhawk skin
    {"defindex": 749, "float_value": 0.1},   // Factory New wear
    {"defindex": 2025, "float_value": 1}     // Killstreak tier
  ]
}
```

## Example Configurations

### Beginner Trading
```json
{
  "access_token": "your_token_here",
  "buy_orders": [
    {
      "comment": "Buying Tour of Duty Tickets - Quick metal",
      "metal": 1.33,
      "defindex": 725
    },
    {
      "comment": "Buying Refined Metal", 
      "metal": 1.00,
      "defindex": 5002
    }
  ]
}
```

### Strange Weapon Collection
```json
{
  "access_token": "your_token_here",
  "buy_orders": [
    {
      "comment": "Buying Strange Scattergun",
      "keys": 1,
      "metal": 2.33,
      "defindex": 200,
      "quality": "strange"
    },
    {
      "comment": "Buying Strange Rocket Launcher",
      "keys": 2,
      "defindex": 205,
      "quality": "strange"
    },
    {
      "comment": "Buying Strange Medigun", 
      "keys": 8,
      "defindex": 211,
      "quality": "strange"
    }
  ]
}
```

### Professional Killstreak Kits
```json
{
  "access_token": "your_token_here",
  "buy_orders": [
    {
      "comment": "Buying Pro KS Scattergun Kit - Any effect/sheen",
      "keys": 4,
      "defindex": 6527,
      "attributes": [
        {"defindex": 2025, "float_value": 3},
        {"defindex": 2012, "float_value": 13}
      ]
    },
    {
      "comment": "Buying Pro KS Medigun Kit - Hypno-Beam + Villainous Violet",
      "keys": 12,
      "defindex": 6527,
      "attributes": [
        {"defindex": 2025, "float_value": 3},
        {"defindex": 2013, "float_value": 2008},
        {"defindex": 2014, "float_value": 6},
        {"defindex": 2012, "float_value": 29}
      ]
    }
  ]
}
```

### Mixed Trading Portfolio
```json
{
  "access_token": "your_token_here",
  "buy_orders": [
    {
      "comment": "Buying Keys for metal trading",
      "metal": 66.33,
      "defindex": 5021
    },
    {
      "comment": "Buying Unusual Team Captain - Any effect", 
      "keys": 50,
      "defindex": 378,
      "quality": "unusual"
    },
    {
      "comment": "Buying Non-Craftable Refined Metal (cheap)",
      "metal": 0.88,
      "defindex": 5002,
      "craftable": false
    }
  ]
}
```

## Troubleshooting

### "Listing value cannot be zero"
**Cause**: You don't have enough currency in your TF2 backpack  
**Solution**: 
- Check your TF2 inventory for keys/metal
- The amount you offer must match what you actually have
- Example: Offering 5 keys? You need 5+ keys in your backpack

### "This access token is not valid"  
**Cause**: Wrong or expired access token  
**Solution**:
- Double-check you copied the token correctly
- Get it from backpack.tf/settings > Advanced section
- Use "Third party access token", NOT API key
- Try regenerating the token

### "Unauthorized" or 401 Error
**Cause**: Token permissions or account issues  
**Solution**:
- Verify your backpack.tf account is in good standing
- Check if you need Premium membership for buy orders
- Regenerate your access token

### "Internal Server Error" or 500 Error
**Cause**: Invalid item data or API issue  
**Solution**:
- Verify the defindex is correct
- Check attribute format for killstreaks/unusuals
- Try with a simpler item first (Tour of Duty Ticket)
- Wait a few minutes and try again

### Python Not Found
**Cause**: Python not installed or not in PATH  
**Solution**:
- Reinstall Python and check "Add to PATH"
- Restart your computer after installation
- Try `python3` instead of `python` (Mac/Linux)

### pip Not Found
**Cause**: pip not installed with Python  
**Solution**:
- Reinstall Python from python.org
- Make sure to check "Add to PATH"
- Try `pip3` instead of `pip` (Mac/Linux)

### File Not Found Errors
**Cause**: Running script from wrong folder  
**Solution**:
- Use `cd` command to navigate to the tool folder
- Make sure you're in the same folder as the Python files

### Common Config Mistakes

❌ **Wrong:**
```json
{
  "comment": "Buying key",
  "keys": 0,              // Zero value not allowed
  "defindex": "725"       // Should be number, not string
}
```

✅ **Correct:**
```json
{
  "comment": "Buying Tour of Duty Ticket",
  "metal": 1.33,          // Positive value
  "defindex": 725         // Number without quotes
}
```

## Video Tutorial (Coming Soon)

We're working on a video tutorial for complete beginners. Check back soon!

## Important Notes

⚠️ **Currency Requirement**: You MUST have the keys/metal you're offering in your TF2 backpack

⚠️ **Premium Membership**: Buy orders may require backpack.tf Premium subscription

⚠️ **Rate Limits**: Don't spam the API - wait between runs to avoid being blocked

⚠️ **Defindex Accuracy**: Double-check item defindexes - wrong numbers = wrong items

⚠️ **Price Checking**: Verify current market prices on backpack.tf before setting your offers

## Getting Help

If you're still having trouble:
1. Check the [Issues](https://github.com/yourusername/backpack-tf-buy-orders/issues) page
2. Create a new issue with your error message
3. Include your operating system and Python version
4. **Never share your access token!**

## Contributing

Found a bug or want to add features? Contributions welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes  
4. Submit a pull request

## License

This project is released under the MIT License. Use at your own risk.

## Disclaimer

This tool is not affiliated with backpack.tf. Use responsibly and follow backpack.tf's terms of service. The author is not responsible for any trading losses or account issues.

### Basic Buy Order Format

Every buy order needs these **required fields**:

```json
{
  "comment": "Description of what you're buying",    // Required: Shows in your listing
  "defindex": 725                                    // Required: Item's unique ID number
}
```

And at least **one price field**:

```json
{
  "keys": 2,        // Optional: Number of Mann Co. Keys
  "metal": 5.33     // Optional: Refined metal amount
}
```

### Complete Field Reference

| Field | Required | Type | Description | Example |
|-------|----------|------|-------------|---------|
| `comment` | ✅ Yes | String | Listing description (max 200 chars) | `"Buying Strange Scattergun"` |
| `defindex` | ✅ Yes | Number | Item's unique identifier | `13` |
| `keys` | ⚠️ One price required | Number | Mann Co. Keys to offer | `2` |
| `metal` | ⚠️ One price required | Number | Refined metal to offer | `5.33` |
| `quality` | ❌ Optional | String | Item quality | `"strange"` |
| `craftable` | ❌ Optional | Boolean | Is item craftable? | `true` |
| `level` | ❌ Optional | Number | Specific item level | `100` |
| `attributes` | ❌ Optional | Array | Special attributes (killstreaks, etc.) | See examples below |

### Supported Qualities

| Quality Name | Number | Description |
|--------------|--------|-------------|
| `"normal"` | 0 | Normal quality (gray text) |
| `"genuine"` | 1 | Genuine quality (dark green) |
| `"vintage"` | 3 | Vintage quality (blue) |
| `"unusual"` | 5 | Unusual quality (purple) |
| `"unique"` | 6 | Unique quality (yellow) - **Default** |
| `"community"` | 7 | Community quality (green) |
| `"self-made"` | 9 | Self-Made quality (green) |
| `"strange"` | 11 | Strange quality (orange) |

### Price Format Examples

```json
// Keys only
{
  "comment": "Buying Unusual Hat",
  "keys": 50,
  "defindex": 123
}

// Metal only  
{
  "comment": "Buying Tour of Duty Ticket",
  "metal": 1.33,
  "defindex": 725
}

// Keys + Metal
{
  "comment": "Buying Strange Weapon",
  "keys": 2,
  "metal": 5.66,
  "defindex": 13
}
```

**Metal Format Guide:**
- `0.11` = 1 Scrap Metal
- `0.33` = 1 Reclaimed Metal  
- `1.00` = 1 Refined Metal
- `1.33` = 1 Refined + 1 Reclaimed
- `1.44` = 1 Refined + 1 Reclaimed + 1 Scrap

## Common Items & Defindexes

### Currency Items
| Item | Defindex | Typical Price |
|------|----------|---------------|
| Tour of Duty Ticket | 725 | 1.33 metal |
| Mann Co. Supply Crate Key | 5021 | N/A (currency) |
| Refined Metal | 5002 | 1.00 metal |
| Reclaimed Metal | 5001 | 0.33 metal |
| Scrap Metal | 5000 | 0.11 metal |

### Popular Weapons
| Item | Defindex | Strange Version |
|------|----------|-----------------|
| Scattergun | 13 | 200 |
| Rocket Launcher | 18 | 205 |
| Flamethrower | 21 | 208 |
| Grenade Launcher | 19 | 206 |
| Shotgun | 9 | 199 |
| Pistol | 23 | 209 |
| Medigun | 29 | 211 |
| Sniper Rifle | 14 | 201 |
| Knife | 4 | 194 |

### Killstreak Kits
| Kit Type | Defindex |
|----------|----------|
| Professional Killstreak Kit | 6527 |
| Specialized Killstreak Kit | 6523 |
| Killstreak Kit | 6522 |

*Find more defindexes: [TF2 Schema API](https://wiki.teamfortress.com/wiki/WebAPI/GetSchema)*

## Advanced Items (Killstreaks, Unusuals, etc.)

### Professional Killstreak Example

```json
{
  "comment": "Buying Pro KS Shotgun Kit - Hot Rod + Cerebral Discharge",
  "keys": 3,
  "defindex": 6527,
  "quality": "unique",
  "attributes": [
    {"defindex": 2025, "float_value": 3},    // Professional Killstreak tier
    {"defindex": 2013, "float_value": 2003}, // Cerebral Discharge effect
    {"defindex": 2014, "float_value": 7},    // Hot Rod sheen  
    {"defindex": 2012, "float_value": 9}     // Target weapon: Shotgun
  ]
}
```

### Unusual Hat Example

```json
{
  "comment": "Buying Unusual Team Captain - Burning Flames",
  "keys": 150,
  "defindex": 378,
  "quality": "unusual",
  "attributes": [
    {"defindex": 134, "float_value": 13}     // Burning Flames effect
  ]
}
```

### Strange Weapon with Parts

```json
{
  "comment": "Buying Strange Scattergun with Kills + Dominations",
  "keys": 5,
  "defindex": 200,
  "quality": "strange", 
  "attributes": [
    {"defindex": 380, "float_value": 0},     // Strange Part: Kills
    {"defindex": 382, "float_value": 31}     // Strange Part: Dominations
  ]
}
```

## Complete Attributes Reference

### Killstreak Attributes

#### Killstreak Tiers (defindex 2025)
| Value | Type |
|-------|------|
| `1` | Killstreak |
| `2` | Specialized Killstreak |
| `3` | Professional Killstreak |

#### Killstreak Effects (defindex 2013) - Professional Only
| Value | Effect Name |
|-------|-------------|
| `2002` | Fire Horns |
| `2003` | Cerebral Discharge |
| `2004` | Tornado |
| `2005` | Flames |
| `2006` | Singularity |
| `2007` | Incinerator |
| `2008` | Hypno-Beam |

#### Killstreak Sheens (defindex 2014) - Specialized & Professional
| Value | Sheen Name |
|-------|------------|
| `1` | Team Shine |
| `2` | Deadly Daffodil |
| `3` | Manndarin |
| `4` | Mean Green |
| `5` | Agonizing Emerald |
| `6` | Villainous Violet |
| `7` | Hot Rod |

#### Target Weapon (defindex 2012) - For Killstreak Kits
Use the defindex of the weapon the kit applies to (e.g., `9` for Shotgun, `13` for Scattergun).

### Unusual Effects (defindex 134)
| Value | Effect Name | Value | Effect Name |
|-------|-------------|-------|-------------|
| `6` | Purple Energy | `13` | Burning Flames |
| `7` | Green Energy | `14` | Scorching Flames |
| `8` | Purple Confetti | `15` | Searing Plasma |
| `9` | Pink Confetti | `16` | Vivid Plasma |
| `10` | Peace Sign | `17` | Sunbeams |
| `11` | Heart | `18` | Green Confetti |
| `12` | Question Mark | `29` | Stormy Storm |
| `703` | Disco Beat Down | `704` | Miami Nights |
| `720` | Stare From Beyond | `722` | Vicious Vortex |

*[Full list available on TF2 Wiki](https://wiki.teamfortress.com/wiki/Unusual)*

### Paint Colors (defindex 142 & 261)
| Value | Paint Name | Hex Color |
|-------|------------|-----------|
| `7511618` | Indubitably Green | `#729E42` |
| `4345659` | Zepheniah's Greed | `#424F3B` |
| `5322826` | Noble Hatter's Violet | `#51384A` |
| `14204632` | Color No. 216-190-216 | `#C8BED8` |
| `8208497` | A Deep Commitment to Purple | `#7D4071` |
| `13595446` | Mann Co. Orange | `#CF7336` |
| `10843461` | Muskelmannbraun | `#A57545` |
| `12955537` | Peculiarly Drab Tincture | `#C5AF91` |
| `6901050` | Radigan Conagher Brown | `#694D3A` |
| `8154199` | Ye Olde Rustic Colour | `#7C6C57` |
| `15185211` | Australium Gold | `#E7B53B` |
| `8289918` | Aged Moustache Grey | `#7E7E7E` |
| `15132390` | An Extraordinary Abundance of Tinge | `#E6E6E6` |
| `1315860` | A Distinctive Lack of Hue | `#141414` |

### Strange Parts (Multiple defindexes)
| Defindex | Part Name | Defindex | Part Name |
|----------|-----------|----------|-----------|
| `380` | Strange Part: Kills | `395` | Strange Part: Robots Destroyed |
| `382` | Strange Part: Ubers | `396` | Strange Part: Giant Robots Destroyed |
| `384` | Strange Part: Kill Assists | `397` | Strange Part: Cloaked Spies Killed |
| `385` | Strange Part: Sentry Kills | `398` | Strange Part: Health Dispensed |
| `386` | Strange Part: Sodden Victims | `399` | Strange Part: Teammates Extinguished |
| `387` | Strange Part: Spies Killed | `400` | Strange Part: Freezecam Taunt Appears |
| `388` | Strange Part: Heads Taken | `401` | Strange Part: Damage Dealt |
| `389` | Strange Part: Humiliations | `402` | Strange Part: Fires Survived |
| `390` | Strange Part: Gifts Given | `403` | Strange Part: Allied Healing Done |
| `391` | Strange Part: Deaths Feigned | `404` | Strange Part: Point Blank Kills |

### Halloween Spells
| Defindex | Spell Type | Values |
|----------|------------|--------|
| `1004` | Paint Spell | `0` = Die Job, `1` = Chromatic Corruption, `2` = Putrescent Pigmentation, `3` = Spectral Spectrum, `4` = Sinister Staining |
| `1005` | Footprint Spell | `1` = Team Spirit, `2` = Headless Horseshoes, `8421376` = Gangreen, `3100495` = Corpse Gray, `5322826` = Violent Violet, `13595446` = Rotten Orange, `8208497` = Bruised Purple |
| `1006` | Voices From Below | No value needed |
| `1007` | Pumpkin Bombs | No value needed |
| `1008` | Halloween Fire | No value needed |
| `1009` | Exorcism | No value needed |

### Weapon Wear (defindex 749) - For Decorated Weapons
| Value Range | Wear Level |
|-------------|------------|
| `0.0 - 0.199` | Factory New |
| `0.2 - 0.399` | Minimal Wear |
| `0.4 - 0.599` | Field-Tested |
| `0.6 - 0.799` | Well-Worn |
| `0.8 - 1.0` | Battle Scarred |

### Weapon Skins (defindex 834)
Use the skin's defindex as the value. Find skin defindexes in the TF2 schema.

### Special Attributes
| Defindex | Attribute | Usage |
|----------|-----------|-------|
| `229` | Craft Number | `{"defindex": 229, "value": 100}` - For craft #100 items |
| `2027` | Australium | `{"defindex": 2027}` - No value needed |
| `2053` | Festivized | `{"defindex": 2053, "float_value": 1}` - Makes item festivized |

### Example: Complete Unusual Hat
```json
{
  "comment": "Buying Painted Unusual Team Captain - Burning + Australium Gold",
  "keys": 200,
  "defindex": 378,
  "quality": "unusual",
  "attributes": [
    {"defindex": 134, "float_value": 13},    // Burning Flames effect
    {"defindex": 142, "value": 15185211}     // Australium Gold paint
  ]
}
```

### Example: Strange Weapon with Parts
```json
{
  "comment": "Buying Strange Scattergun - Kills + Damage + Dominations",
  "keys": 8,
  "defindex": 200,
  "quality": "strange",
  "attributes": [
    {"defindex": 380, "float_value": 0},     // Kills tracker
    {"defindex": 401, "float_value": 0},     // Damage dealt tracker  
    {"defindex": 388, "float_value": 31}     // Dominations tracker
  ]
}
```

### Example: Decorated Weapon
```json
{
  "comment": "Buying Factory New Killstreak Warhawk Rocket Launcher",
  "keys": 15,
  "defindex": 18,
  "quality": "unique",
  "attributes": [
    {"defindex": 834, "value": 276},         // Warhawk skin
    {"defindex": 749, "float_value": 0.1},   // Factory New wear
    {"defindex": 2025, "float_value": 1}     // Killstreak tier
  ]
}
```

## Example Configurations

### Beginner Trading
```json
{
  "access_token": "your_token_here",
  "buy_orders": [
    {
      "comment": "Buying Tour of Duty Tickets - Quick metal",
      "metal": 1.33,
      "defindex": 725
    },
    {
      "comment": "Buying Refined Metal", 
      "metal": 1.00,
      "defindex": 5002
    }
  ]
}
```

### Strange Weapon Collection
```json
{
  "access_token": "your_token_here",
  "buy_orders": [
    {
      "comment": "Buying Strange Scattergun",
      "keys": 1,
      "metal": 2.33,
      "defindex": 200,
      "quality": "strange"
    },
    {
      "comment": "Buying Strange Rocket Launcher",
      "keys": 2,
      "defindex": 205,
      "quality": "strange"
    },
    {
      "comment": "Buying Strange Medigun", 
      "keys": 8,
      "defindex": 211,
      "quality": "strange"
    }
  ]
}
```

### Professional Killstreak Kits
```json
{
  "access_token": "your_token_here",
  "buy_orders": [
    {
      "comment": "Buying Pro KS Scattergun Kit - Any effect/sheen",
      "keys": 4,
      "defindex": 6527,
      "attributes": [
        {"defindex": 2025, "float_value": 3},
        {"defindex": 2012, "float_value": 13}
      ]
    },
    {
      "comment": "Buying Pro KS Medigun Kit - Hypno-Beam + Villainous Violet",
      "keys": 12,
      "defindex": 6527,
      "attributes": [
        {"defindex": 2025, "float_value": 3},
        {"defindex": 2013, "float_value": 2008},
        {"defindex": 2014, "float_value": 6},
        {"defindex": 2012, "float_value": 29}
      ]
    }
  ]
}
```

### Mixed Trading Portfolio
```json
{
  "access_token": "your_token_here",
  "buy_orders": [
    {
      "comment": "Buying Keys for metal trading",
      "metal": 66.33,
      "defindex": 5021
    },
    {
      "comment": "Buying Unusual Team Captain - Any effect", 
      "keys": 50,
      "defindex": 378,
      "quality": "unusual"
    },
    {
      "comment": "Buying Non-Craftable Refined Metal (cheap)",
      "metal": 0.88,
      "defindex": 5002,
      "craftable": false
    }
  ]
}
```

## Troubleshooting

### "Listing value cannot be zero"
**Cause**: You don't have enough currency in your TF2 backpack  
**Solution**: 
- Check your TF2 inventory for keys/metal
- The amount you offer must match what you actually have
- Example: Offering 5 keys? You need 5+ keys in your backpack

### "This access token is not valid"  
**Cause**: Wrong or expired access token  
**Solution**:
- Double-check you copied the token correctly
- Get it from backpack.tf/settings > Advanced section
- Use "Third party access token", NOT API key
- Try regenerating the token

### "Unauthorized" or 401 Error
**Cause**: Token permissions or account issues  
**Solution**:
- Verify your backpack.tf account is in good standing
- Check if you need Premium membership for buy orders
- Regenerate your access token

### "Internal Server Error" or 500 Error
**Cause**: Invalid item data or API issue  
**Solution**:
- Verify the defindex is correct
- Check attribute format for killstreaks/unusuals
- Try with a simpler item first (Tour of Duty Ticket)
- Wait a few minutes and try again

### Common Config Mistakes

❌ **Wrong:**
```json
{
  "comment": "Buying key",
  "keys": 0,              // Zero value not allowed
  "defindex": "725"       // Should be number, not string
}
```

✅ **Correct:**
```json
{
  "comment": "Buying Tour of Duty Ticket",
  "metal": 1.33,          // Positive value
  "defindex": 725         // Number without quotes
}
```

## Important Notes

⚠️ **Currency Requirement**: You MUST have the keys/metal you're offering in your TF2 backpack

⚠️ **Premium Membership**: Buy orders may require backpack.tf Premium subscription

⚠️ **Rate Limits**: Don't spam the API - wait between runs to avoid being blocked

⚠️ **Defindex Accuracy**: Double-check item defindexes - wrong numbers = wrong items

⚠️ **Price Checking**: Verify current market prices on backpack.tf before setting your offers

## Contributing

Found a bug or want to add features? Contributions welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes  
4. Submit a pull request

## License

This project is released under the MIT License. Use at your own risk.

## Disclaimer

This tool is not affiliated with backpack.tf. Use responsibly and follow backpack.tf's terms of service. The author is not responsible for any trading losses or account issues.
