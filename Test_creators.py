
# generator_testing**********************************


# from app.geometry import GeometryGenerator

# sample_floor = {
#     "rooms": [
#         {
#             "name": "Living Room",
#             "width": 5,
#             "length": 4,
#             "position": [0, 0]
#         }
#     ]
# }

# gen = GeometryGenerator()
# scene = gen.generate_floor(sample_floor)

# for obj in scene:
#     print(obj)


#validator_testing***********************************************

# from app.validator import FloorPlanValidator

# #OVERLAPPING FLOORS
# sample_floor_overlap = {
#     "rooms": [
#         {"name": "Room A", "width": 4, "length": 4, "position": [0, 0]},
#         {"name": "Room B", "width": 3, "length": 3, "position": [2, 2]}
#     ]
# }

# #NON-OVERLAP FLOORS
# sample_floor = {
#     "rooms": [
#         {"name": "Room A", "width": 4, "length": 4, "position": [0, 0]},
#         {"name": "Room B", "width": 3, "length": 3, "position": [5, 0]}
#     ]
# }

# validator = FloorPlanValidator()
# result = validator.validate(sample_floor_overlap)

# print(result)

#feasibility_testing*******************************************************

# from app.feasibility import FeasibilityAnalyzer

# sample_floor_problem = {
#     "rooms": [
#         {"name": "Tiny Room", "width": 2, "length": 2, "position": [0, 0]},
#         {"name": "Long Room", "width": 10, "length": 2, "position": [3, 0]}
#     ]
# }
# analyzer = FeasibilityAnalyzer()
# warnings = analyzer.analyze(sample_floor_problem)

# print("Warnings:", warnings)
# print("Type:", type(warnings))

#Full Agent Testing*******************************************************

from app.agent import FloorPlanAgent

sample_floor = {
    "rooms": [
        {"name": "Living Room", "width": 5, "length": 4, "position": [0, 0]},
        {"name": "Kitchen", "width": 3, "length": 3, "position": [5, 0]}
    ]
}

agent = FloorPlanAgent()
result = agent.process(sample_floor)

print("STATUS:", result["status"])
print("WARNINGS:", result["warnings"])
print("GEOMETRY COUNT:", len(result["geometry"]))
print("\nREPORT:\n", result["report"])
