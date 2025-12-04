from typing import Any, Dict, List, Tuple
"""
Partial solution to task from EPR-Blatt 06s
"""
__author__ = "Calderon, 12345"

def add_items(inventory: Dict[str, Any], **items: Dict[str, Any]) -> Dict[str, Any]:
    for location, content in items.items():
        if location in inventory:
            inventory[location].update(content)
        else:
            inventory[location] = content
    return inventory # Not neccesry

def list_all_items(inventory: Dict[str, Any]) -> List[str]:
    sorted_items = []
    for location in inventory.values():
        for item in location:
            sorted_items.append(item)
    sorted_items.sort()
    return sorted_items

def search_item_by_name(inventory: Dict[str, Any], item_name: str) -> Tuple[bool, Dict[str, Any]]:
    for location, items in inventory.items():
        if item_name in items:
            return (True, {location : items[item_name]})
    return (False, {f"Item '{item_name}'" : "not found"})