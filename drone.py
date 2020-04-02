class drone():
    drone_cap = 20
    km_per_batt = 1.5  # stores how much drone can travel with 1% battery

    def __init__(self, drone_id, battery, curr_loc, status, curr_load):
        self.drone_id = drone_id
        self.drone_loc = curr_loc
        self.battery = battery
        self.status = status
        self.curr_load = curr_load

    def getDistance(self, x):
        self.point_dist = abs(self.drone_loc-x)

    def getOrder(self):
        self.trav_dist = self.battery*drone.km_per_batt

    def capacity(self):
        self.remain_capacity = drone.drone_cap-self.curr_load


class hub:
    obj_mass = {'chair': 2, 'phone': 0.5, 'hat': 0.5, 'books': 1, 'table': 2.5}#object with unit weight
    temp_mass = []
    supply_support=[]

    def __init__(self, name, loc, supplies):
        self.name = name
        self.hub_loc = loc
        self.avl_supplies = supplies

    def getDistance(self, source_loc, des_loc):
        self.order_dist = abs(source_loc-des_loc)

    def getOrder(self, pick_up, drop, list_supp):
        self.source_name = pick_up
        self.dest_name = drop
        self.supplies = list_supp

    def getMass(self, supplies):
        self.supplies=supplies
        supply = list(supplies.keys())
        b = list(hub.obj_mass.keys())
        for key in supply:
            if key in b:
                x=float(self.supplies[key])*float(hub.obj_mass[key])
                hub.temp_mass.append(x)
        self.order_mass = sum(hub.temp_mass)
        hub.temp_mass=[]
    def efficient_drone(self,drones):
        temp_list_point_dis=[]
        temp_list_eff_drone=[]
        for drone in drones:
            if(drone.trav_dist>hub.order_dist):
                if(drone.remain_capacity>hub.order_mass):
                    temp_list_point_dis.append(drone.point_dist)
                    temp_list_eff_drone.append(drone)

        for dron in temp_list_eff_drone:
            if(dron.point_dist==min(temp_list_point_dis)):
                self.efficient_drone_id= dron.drone_id;
                print("efficient drone for this delivery willbe with id",self.efficient_drone_id)
                break;
    def suppliesStatus(self,order_supplies):
        order_keys = list(order_supplies.keys())
        avl_keys=list(self.avl_supplies.keys())
        for key in order_keys:
            if key in avl_keys:
                if order_supplies[key]<=self.avl_supplies[key]:
                    pass
                else :     
                    self.supply_status=0
                    return
            else:
                self.supply_status=0
                return
        self.status=1
        hub.supply_support.append(self)
d1 = drone(1, 100, 140, 1, 2)
d2 = drone(2, 50, 40, 0, 0)
d3 = drone(3, 80, 160, 0, 0)
d4 = drone(4, 70, 80, 0, 0)
d5 = drone(5, 80, 100, 1, 3)
d6 = drone(6, 50, 120, 0, 0)
d7 = drone(7, 70, 40, 0, 0)
d8 = drone(8, 50, 130, 1, 4)
d9 = drone(9, 90, 80, 0, 0)
drones = [d1, d2, d3, d4, d5, d6, d7, d8, d9]
h1 = hub("h1", 40, {'chair': 3, 'hat': 4, 'phone': 10,
                    'table': 2, 'books': 5})
h2 = hub("h2", 160, {'chair': 2, 'hat': 2, 'phone': 3,
                     'table': 2, 'books': 1})
h3 = hub("h3", 80, {'chair': 5, 'hat': 8, 'phone': 5,
                    'table': 2, 'books': 10})
h4 = hub("h4", 120, {'chair': 6, 'hat': 5, 'phone': 6,
                     'table': 2, 'books': 2})
hubs = [h1, h2, h3, h4]
source_hub = input(
    "enter the name of sourcehub where the order is to be picked up[h1,h2,h3")
des_hub = input(
    "enter the name of deshub where the order is to be delivered[h1,h2,h3")
no_of_supplies = int(input("enter the no of supplies you want"))
supplies = dict()
for i in range(no_of_supplies):
    key = input("Enter the product: ")
    value = int(input("Enter the quantity: "))
    supplies[key] = value
source_loc=eval(source_hub).hub_loc
des_loc=eval(des_hub).hub_loc
for drone in drones:
    drone.getDistance(source_loc)
    drone.getOrder()
    drone.capacity()

for hub in hubs:
    hub.suppliesStatus(supplies)
    hub.getDistance(source_loc,des_loc)
    hub.getOrder(source_hub,des_hub,supplies)
if(len(hub.supply_support)==0):
    print("request cant be fulfilled")
else:
    hub.getMass(supplies)
    print("mass is",hub.order_mass)
    if(hub.order_mass>drone.drone_cap):
        print("mass to much request cant be processed")
    else:
        hub.efficient_drone(drones)

