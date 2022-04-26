class Collection:
    def __init__(self, collection_slug):
        self.slug = collection_slug

    def update(self, json_data):
        self.json_data = json_data
        self.total_supply = json_data["stats"]["total_supply"]
        self.count = json_data["stats"]["count"]
        self.num_owners = json_data["stats"]["num_owners"]
        self.one_day_volume = json_data["stats"]["one_day_volume"]
        self.seven_day_volume = json_data["stats"]["seven_day_volume"]
        self.total_volume = json_data["stats"]["total_volume"]
        self.total_sales = json_data["stats"]["total_sales"]
        self.average_price = json_data["stats"]["average_price"]
        self.floor_price = json_data["stats"]["floor_price"]