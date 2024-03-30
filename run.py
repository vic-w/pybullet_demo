import pybullet as p
import time
import json

physicsClient = p.connect(p.GUI)

p.setGravity(0,0,-10)
planeId = p.loadURDF("toys/plane.urdf")

binId = p.loadURDF("toys/bin.urdf",[0,0,1], p.getQuaternionFromEuler([0,0,0]))

cylinders = []
for i in range (50):
    cylinderId = p.loadURDF("toys/cylinder.urdf",[0,0,2], p.getQuaternionFromEuler([0.1,0,0]))
    cylinders.append(cylinderId)

    for i in range (50):
        p.stepSimulation()
        time.sleep(1./240.)

for i in range (1000):
    p.stepSimulation()
    time.sleep(1./240.)


json_data = {}
json_data['bin'] = []
Pos, Orn = p.getBasePositionAndOrientation(binId)
bin = {'position': Pos, 'orientation': Orn}
json_data['bin'].append(bin)

json_data['cylinders'] = []
for cylinderId in cylinders:
    Pos, Orn = p.getBasePositionAndOrientation(cylinderId)
    cylinder = {'position': Pos, 'orientation': Orn}
    json_data['cylinders'].append(cylinder)

with open('output.json', 'w') as outfile:
    json.dump(json_data, outfile, indent=4)

p.disconnect()
