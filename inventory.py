"""Inventory management system for tracking stock items."""

import json
from datetime import datetime

# Global variable
stock_data = {}


def addItem(item="default", qty=0, logs=None):
    """Add items to the inventory.

    Args:
        item: Name of the item to add
        qty: Quantity to add
        logs: List to append log messages to (optional)
    """
    if logs is None:
        logs = []
    if not item:
        return
    # Validate types
    try:
        qty = int(qty)
    except (ValueError, TypeError):
        print(f"Error: Quantity must be a number, got {type(qty).__name__}")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{str(datetime.now())}: Added {qty} of {item}")


def removeItem(item, qty):
    """Remove items from the inventory.

    Args:
        item: Name of the item to remove
        qty: Quantity to remove
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Error: Item '{item}' not found in inventory")
    except ValueError as e:
        print(f"Error removing item: {e}")


def getQty(item):
    """Get the quantity of an item in inventory.

    Args:
        item: Name of the item to query

    Returns:
        Quantity of the item, or 0 if not found
    """
    return stock_data.get(item, 0)


def loadData(file="inventory.json"):
    """Load inventory data from a JSON file.

    Args:
        file: Path to the JSON file to load
    """
    global stock_data
    try:
        with open(file, "r", encoding='utf-8') as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        msg = (f"Warning: File '{file}' not found. "
               f"Starting with empty inventory.")
        print(msg)
        stock_data = {}


def saveData(file="inventory.json"):
    """Save inventory data to a JSON file.

    Args:
        file: Path to the JSON file to save
    """
    with open(file, "w", encoding='utf-8') as f:
        json.dump(stock_data, f)


def printData():
    """Print all items in the inventory."""
    print("Items Report")
    for item in stock_data:
        print(item, "->", stock_data[item])


def checkLowItems(threshold=5):
    """Check which items are below the threshold.

    Args:
        threshold: Minimum quantity threshold

    Returns:
        List of items below the threshold
    """
    result = []
    for item in stock_data:
        if stock_data[item] < threshold:
            result.append(item)
    return result


def main():
    """Main function to demonstrate inventory operations."""
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")  # invalid types, no check
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()


if __name__ == "__main__":
    main()
