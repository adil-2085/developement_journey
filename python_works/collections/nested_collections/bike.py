bikes=[
    ["passion-pro","hero",89000,"petrol",125],
    ["passion-plus","hero",89000,"petrol",125],
    ["activa","honda",120000,"petrol",125],
    ["xpulse","hero",139000,"petrol",150],
    ["hunter","re",200000,"petrol",350],
    ["metor","re",230000,"petrol",350],
    ["triumph-speed-400x","triumph",300000,"petrol",400],
    ["ola-S1-pro","ola",170000,"ev",120],
    ["ather-450-x","ather",150000,"ev",120]
]


all_bikes=[i[0] for i in bikes]

print(all_bikes)

bike_prices=[i[2] for i in bikes]

print(bike_prices)

fuel_variants={i[3] for i in bikes}

print(fuel_variants)

price_filter=[i[0] for i in bikes if i[2]>100000]

print(price_filter)

ev_bikes=[i[0] for i in bikes if i[3]=='ev']

print(ev_bikes)

# lambda parameter1,parameter2:expression


# def get_price(lst):

#     return lst[2]

get_price = lambda lst:lst[2]

costly_bike = max(bikes,key=get_price)

print(costly_bike)

