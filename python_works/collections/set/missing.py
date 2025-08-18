ware_house={'laptop','mouse','keyboard','wifi-adaptor','mic','speakers','projector'}
actual_items={'laptop','mouse','keyboard'}

missing_items=ware_house.difference(actual_items)

print(missing_items)
