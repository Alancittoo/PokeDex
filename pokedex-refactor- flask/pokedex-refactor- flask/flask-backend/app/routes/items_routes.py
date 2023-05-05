from flask import Blueprint, redirect ## imports Blueprint + etcprice
from ..models import Item
item = Blueprint("item", __name__)

@item.route("")
def get_all_item():
    all_items = Item.query.all()
    print(all_items)
    all_items_dict = [item.to_dict() for item in all_items]
    print(all_items_dict)
    return all_items_dict