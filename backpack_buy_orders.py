#!/usr/bin/env python3
"""
Backpack.tf Buy Order Creator
Simplified tool for creating buy orders on backpack.tf using the v2 API
"""

import json
import requests
import sys
import os
from typing import Dict, List, Any, Optional

class BackpackBuyOrderTool:
    def __init__(self, access_token: str):
        """Initialize with your backpack.tf access token"""
        self.access_token = access_token
        self.base_url = "https://backpack.tf/api"
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "BackpackTF-BuyOrderTool/1.0"
        }
    
    def create_buy_orders(self, orders: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Create buy orders using the batch API endpoint"""
        url = f"{self.base_url}/v2/classifieds/listings/batch"
        
        # Convert simplified format to API format
        listings = []
        for order in orders:
            listing = self._convert_order_to_listing(order)
            listings.append(listing)
        
        params = {"token": self.access_token}
        payload = {"listings": listings}
        
        try:
            response = requests.post(url, headers=self.headers, params=params, json=payload)
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                if "listings" in result and "error" in result["listings"]:
                    return {"success": False, "error": result["listings"]["error"]["message"]}
                return {"success": True, "result": result}
            else:
                return {"success": False, "error": f"HTTP {response.status_code}: {response.text}"}
                
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def _convert_order_to_listing(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """Convert simplified order format to API listing format"""
        
        # Basic listing structure
        listing = {
            "intent": 0,  # 0 = buy order
            "details": order.get("comment", ""),
            "buyout": 1,
            "offers": 1,
            "currencies": {},
            "item": {
                "quality": 6,  # Unique quality by default
                "quantity": 1
            }
        }
        
        # Handle price
        if "keys" in order:
            listing["currencies"]["keys"] = order["keys"]
        if "metal" in order:
            listing["currencies"]["metal"] = order["metal"]
        
        # Handle item identification
        if "defindex" in order:
            listing["item"]["defindex"] = order["defindex"]
        
        # Handle quality
        quality_map = {
            "normal": 0, "genuine": 1, "vintage": 3, "unusual": 5,
            "unique": 6, "community": 7, "self-made": 9, "strange": 11
        }
        if "quality" in order:
            if isinstance(order["quality"], str):
                listing["item"]["quality"] = quality_map.get(order["quality"].lower(), 6)
            else:
                listing["item"]["quality"] = order["quality"]
        
        # Handle attributes for special items
        if "attributes" in order:
            listing["item"]["attributes"] = order["attributes"]
        
        # Handle other item properties
        for prop in ["level", "craftable"]:
            if prop in order:
                if prop == "craftable":
                    listing["item"]["flag_cannot_craft"] = not order[prop]
                else:
                    listing["item"][prop] = order[prop]
        
        return listing

def load_config(filename: str = "buy_orders.json") -> Dict[str, Any]:
    """Load configuration from JSON file"""
    try:
        with open(filename, 'r') as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        print(f"Config file '{filename}' not found!")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON config: {e}")
        return {}

def create_example_config():
    """Create an example configuration file"""
    example_config = {
        "access_token": "YOUR_ACCESS_TOKEN_HERE",
        "buy_orders": [
            {
                "comment": "Buying Tour of Duty Ticket",
                "metal": 1.33,
                "defindex": 725,
                "quality": "unique"
            },
            {
                "comment": "Buying Strange Scattergun",
                "keys": 2,
                "metal": 5.33,
                "defindex": 13,
                "quality": "strange"
            },
            {
                "comment": "Buying Pro KS Shotgun Kit - Hot Rod + Cerebral Discharge",
                "keys": 3,
                "defindex": 6527,
                "quality": "unique",
                "attributes": [
                    {"defindex": 2025, "float_value": 3},
                    {"defindex": 2013, "float_value": 2003},
                    {"defindex": 2014, "float_value": 7},
                    {"defindex": 2012, "float_value": 9}
                ]
            }
        ]
    }
    
    with open("buy_orders.json", 'w') as f:
        json.dump(example_config, f, indent=2)
    
    print("Created example config file: buy_orders.json")
    print("Please edit it with your access token and desired buy orders!")

def main():
    """Main function"""
    print("=== Backpack.tf Buy Order Creator ===\n")
    
    config_filename = "buy_orders.json"
    
    # Check if config file exists
    if not os.path.exists(config_filename):
        print("Configuration file doesn't exist.")
        create_example_config()
        return
    
    # Load the config
    config = load_config()
    
    # If config is empty or invalid, don't overwrite the existing file
    if not config:
        print("Error loading configuration. Please check the file format.")
        return
    
    # Get access token
    access_token = config.get("access_token")
    if not access_token or access_token == "YOUR_ACCESS_TOKEN_HERE":
        print("Please set your access token in buy_orders.json!")
        print("Get it from: https://backpack.tf/settings (Advanced section)")
        return
    
    # Get buy orders
    buy_orders = config.get("buy_orders", [])
    if not buy_orders:
        print("No buy orders found in config!")
        return
    
    # Initialize tool
    tool = BackpackBuyOrderTool(access_token)
    
    # Show summary
    print(f"Found {len(buy_orders)} buy order(s) to create:")
    for i, order in enumerate(buy_orders, 1):
        price_str = ""
        if "keys" in order:
            price_str += f"{order['keys']} keys "
        if "metal" in order:
            price_str += f"{order['metal']} metal"
        print(f"  {i}. {order.get('comment', 'No comment')} - {price_str.strip()}")
    
    # Confirm before creating
    print(f"\nReady to create {len(buy_orders)} buy order(s).")
    print("⚠️  Make sure you have enough currency in your TF2 backpack!")
    confirm = input("Continue? (y/N): ").lower().strip()
    
    if confirm != 'y':
        print("Cancelled.")
        return
    
    # Create buy orders
    print("Creating buy orders...")
    result = tool.create_buy_orders(buy_orders)
    
    if result.get("success", False):
        print("✓ Buy orders created successfully!")
    else:
        print("✗ Failed to create buy orders")
        error = result.get("error", "Unknown error")
        print(f"Error: {error}")
        
        if "zero" in error.lower():
            print("\nTip: Make sure you have enough keys/metal in your TF2 backpack!")
        elif "unauthorized" in error.lower():
            print("\nTip: Check your access token in buy_orders.json")

if __name__ == "__main__":
    main()
