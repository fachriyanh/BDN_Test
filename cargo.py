heightDoor        = 7
widthDoor         = 5
weightCargo       = 20
widthCargo        = 10
heightCargo       = 10
lengthCargo       = 10
volumeCargo       = 1000
passItems = []
items = [
         {"packageId"   : "item001", 
          "type"        : "S", 
          "width"       : 5, 
          "height"      : 8, 
          "length"      : 2, 
          "weight"      : 5}, 
         {"packageId"   : "item002", 
          "type"        : "L", 
          "temperature" : 25, 
          "weight"      : 6},
         {"packageId"   : "item003", 
          "type"        : "L", 
          "temperature" : 19, 
          "weight"      : 6},
         {"packageId"   : "item004", 
          "type"        : "S", 
          "width"       : 1, 
          "height"      : 15, 
          "length"      : 2, 
          "weight"      : 1},
         {"packageId"   : "item005", 
          "type"        : "S", 
          "width"       : 1, 
          "height"      : 1, 
          "length"      : 10, 
          "weight"      : 2},
         {"packageId"   : "item006", 
          "type"        : "L", 
          "temperature" : 25, 
          "weight"      : 10}
         ]

for i in range(len(items)) :
  #Liquid Filter
  if items[i]["type"] == "L" and (20 > items[i]["temperature"] or  items[i]["temperature"] > 30 or  items[i]["weight"] > weightCargo) and (lengthCargo * widthCargo * heightCargo) > 1 :
    print(items[i]["packageId"]+": REJECT")
    pass
  elif items[i]["type"] == "L" :
    print(items[i]["packageId"]+": PASS")
    weightCargo -= items[i]["weight"]
    passItems.append(items[i]["packageId"])
    pass
  #Solid Filter
  else :
    dimensi = [items[i]["height"],items[i]["length"],items[i]["width"]]
    dimensi.sort()
    if dimensi[0] <= widthDoor and dimensi[1] <= heightDoor and dimensi[2] <= 10 :
      #print(items[i]["packageId"]+": SOLID PASS DOOR")
      if (items[i]["length"] * items[i]["width"] * items[i]["height"]) <= volumeCargo and items[i]["weight"] <= weightCargo :
        print(items[i]["packageId"]+": PASS")
        volumeCargo -= (items[i]["length"] * items[i]["width"] * items[i]["height"])
        weightCargo -= items[i]["weight"]
        passItems.append(items[i]["packageId"])
        pass
      else : 
        print(items[i]["packageId"]+": REJECT")
        pass
    else :
      print(items[i]["packageId"]+": REJECT")

print("Item in Cargo : ", passItems)

# Result :
# item001: PASS
# item002: PASS
# item003: REJECT
# item004: REJECT
# item005: PASS
# item006: REJECT
# Item in Cargo :  ['item001', 'item002', 'item005']