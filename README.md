# Backpack.tf Buy Order Creator

A simple Python tool to automatically create buy orders on backpack.tf using their v2 API. Perfect for traders who want to automate their buying process!

## Features

- ✅ **Simple Configuration** - Easy JSON format, no complex API knowledge needed
- ✅ **Batch Creation** - Create multiple buy orders at once
- ✅ **Smart Validation** - Checks your config before sending to API
- ✅ **Clear Error Messages** - Helpful tips when things go wrong
- ✅ **Professional Killstreaks** - Full support for unusual effects, killstreaks, etc.

## Requirements

- Python 3.6 or higher
- `requests` library (`pip install requests`)
- Team Fortress 2 items (keys/metal) in your Steam inventory
- Backpack.tf account with access token

## Quick Start

### 1. Download the Script
```bash
git clone https://github.com/yourusername/backpack-tf-buy-orders.git
cd backpack-tf-buy-orders
```

### 2. Install Dependencies
```bash
pip install requests
```

### 3. Get Your Access Token
1. Go to [backpack.tf/settings](https://backpack.tf/settings)
2. Scroll to the **"Advanced"** section
3. Copy your **"Third party access token"** (not API key!)

### 4. Run the Script
```bash
python backpack_buy_orders.py
```

The first run will create an example `buy_orders.json` file.

### 5. Configure Your Buy Orders
Edit `buy_orders.json` with your access token and desired buy orders:

```json
{
  "access_token": "your_actual_token_here",
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

### 6. Run Again
```bash
python backpack_buy_orders.py
```

## Configuration Guide

### Basic Buy Order Format

```json
{
  "comment": "Description of what you're buying",
  "keys": 2,           // Optional: number of keys
  "metal": 5.33,       // Optional: refined metal amount
  "defindex": 13,      // Item's defindex (required)
  "quality": "strange" // Item quality (optional, default: "unique")
}
```

### Supported Qualities
- `"normal"` - Normal quality
- `"genuine"` - Genuine quality  
- `"vintage"` - Vintage quality
- `"unusual"` - Unusual quality
- `"unique"` - Unique quality (default)
- `"community"` - Community quality
- `"self-made"` - Self-Made quality
- `"strange"` - Strange quality

### Advanced Items (Killstreaks, Unusuals, etc.)

For items with special attributes like killstreaks or unusual effects:

```json
{
  "comment": "Buying Pro KS Shotgun Kit - Hot Rod + Cerebral Discharge",
  "keys": 3,
  "defindex": 6527,
  "quality": "unique",
  "attributes": [
    {"defindex": 2025, "float_value": 3},    // Professional Killstreak
    {"defindex": 2013, "float_value": 2003}, // Cerebral Discharge effect
    {"defindex": 2014, "float_value": 7},    // Hot Rod sheen
    {"defindex": 2012, "float_value": 9}     // Target: Shotgun
  ]
}
```

## Common Defindexes

| Item | Defindex |
|------|----------|
| Tour of Duty Ticket | 725 |
| Scattergun | 13 |
| Rocket Launcher | 18 |
| Shotgun | 9 |
| Professional Killstreak Kit | 6527 |
| Mann Co. Supply Crate Key | 5021 |

*Find more defindexes at [TF2 Schema](https://wiki.teamfortress.com/wiki/WebAPI/GetSchema)*

## Killstreak Reference

### Killstreak Tiers (defindex 2025)
- `1` - Killstreak
- `2` - Specialized Killstreak  
- `3` - Professional Killstreak

### Killstreak Effects (defindex 2013)
- `2002` - Fire Horns
- `2003` - Cerebral Discharge
- `2004` - Tornado
- `2005` - Flames
- `2006` - Singularity
- `2007` - Incinerator
- `2008` - Hypno-Beam

### Killstreak Sheens (defindex 2014)
- `1` - Team Shine
- `2` - Deadly Daffodil
- `3` - Manndarin
- `4` - Mean Green
- `5` - Agonizing Emerald
- `6` - Villainous Violet
- `7` - Hot Rod

## Troubleshooting

### "Listing value cannot be zero"
- **Solution**: Make sure you have enough keys/metal in your TF2 backpack
- The amount you're offering must match what you actually have in your inventory

### "This access token is not valid"
- **Solution**: Double-check your access token from backpack.tf/settings
- Make sure you're using the "Third party access token", not the API key

### "Unauthorized" or 401 Error
- **Solution**: Verify your access token is correct and has proper permissions
- Try regenerating your token on backpack.tf

### "Internal Server Error" 
- **Solution**: Check your item defindex and attributes are valid
- Try with a simpler item first (like Tour of Duty Ticket)

## Example Configurations

### Simple Metal Trading
```json
{
  "access_token": "your_token_here",
  "buy_orders": [
    {
      "comment": "Buying Tour of Duty Tickets",
      "metal": 1.33,
      "defindex": 725
    },
    {
      "comment": "Buying Scrap Metal",
      "metal": 0.11,
      "defindex": 5000
    }
  ]
}
```

### Strange Weapons
```json
{
  "access_token": "your_token_here", 
  "buy_orders": [
    {
      "comment": "Buying Strange Scattergun",
      "keys": 1,
      "metal": 2.33,
      "defindex": 13,
      "quality": "strange"
    },
    {
      "comment": "Buying Strange Rocket Launcher", 
      "keys": 2,
      "defindex": 18,
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
    }
  ]
}
```

## Important Notes

⚠️ **Currency Requirement**: You MUST have the keys/metal you're offering in your TF2 backpack

⚠️ **Premium Membership**: Some features may require backpack.tf Premium

⚠️ **Rate Limits**: Don't spam the API - use reasonable delays between runs

⚠️ **Defindex Accuracy**: Double-check item defindexes to avoid buying wrong items

## Contributing

Feel free to submit issues and pull requests! This tool is designed to be simple and reliable.

## License

This project is released under the MIT License. Use at your own risk.

## Disclaimer

This tool is not affiliated with backpack.tf. Use responsibly and follow backpack.tf's terms of service.
