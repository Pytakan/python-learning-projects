def rout_info(route_dict, **kwargs):
  if('distance' in route_dict and type(route_dict['distance'])is int):
    return f"Distance to your destination is {route_dict['distance']} km"
  if('speed' in route_dict and 'time' in route_dict):
    if(type(route_dict['speed'])is int and type(route_dict['time'])is int):
        return f"Distance to your destination is {route_dict['speed']* route_dict['time']} km/h"
    return "No distance info is available"
  
print(rout_info({'distance': 150}))
print(rout_info({'speed': 60, 'time': 2}))
print(rout_info({'speed': 'fast', 'time': 2}))
print(rout_info({'speed':45,'time': 2,'distance': 55}))
