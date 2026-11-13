class Items:
    def __init__(self):
        self.items=["Book","Laptop","Notebook","Pen","Pencil","Keyboard","Mouse"]

    def __iter__(self):
        for item in self.items:
            yield item

your_items = Items()

for things in your_items:
    print(f"You have {things}")
