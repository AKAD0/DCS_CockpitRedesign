n = open("C:/Program Files/Eagle Dynamics/DCS World/Custom-Mods/materials-new.lua", "r")
t = open("C:/Program Files/Eagle Dynamics/DCS World/Mods/aircraft/FA-18C/Cockpit/Scripts/materials.lua", "w")
t.write(n.read())

print('New color.')