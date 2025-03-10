# Simulated in-memory database
items_db = []

def fetch_all_items():
    return items_db

def create_item(item: dict):
    items_db.append(item)
