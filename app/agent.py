from app.validator import FloorPlanValidator
from app.feasibility import FeasibilityAnalyzer
from app.geometry import GeometryGenerator
from app.report_generator import ReportGenerator


class FloorPlanAgent:

    def __init__(self):
        self.validator = FloorPlanValidator()
        self.feasibility = FeasibilityAnalyzer()
        self.geometry = GeometryGenerator()
        self.report_generator = ReportGenerator()

    def process(self, floor_plan):

        validation_result = self.validator.validate(floor_plan)

        if not validation_result["valid"]:
            # Try auto-correction if only overlaps
            auto_corrected = self._attempt_autocorrect(floor_plan)

            if auto_corrected:
                floor_plan = auto_corrected
            else:
                return {
                    "status": "invalid",
                    "errors": validation_result["errors"]
                }

        feasibility_warnings = self.feasibility.analyze(floor_plan)

        geometry_objects = self.geometry.generate_floor(floor_plan)

        report = self.report_generator.generate(
            floor_plan,
            feasibility_warnings,
            geometry_objects
        )

        return {
            "status": "success",
            "warnings": feasibility_warnings,
            "geometry": geometry_objects,
            "report": report
        }
    
    def _attempt_autocorrect(self, floor_plan):
        rooms = floor_plan.get("rooms", [])

        corrected = False

        for i in range(len(rooms)):
            for j in range(i + 1, len(rooms)):
                r1 = rooms[i]
                r2 = rooms[j]

                if self._rooms_overlap(r1, r2):
                    # Shift r2 to the right of r1
                    r2["position"][0] = r1["position"][0] + r1["width"] + 0.2
                    corrected = True

        return floor_plan if corrected else None

    def _rooms_overlap(self, r1, r2):
        x1, y1 = r1["position"]
        x2, y2 = r2["position"]

        return not (
            x1 + r1["width"] <= x2 or
            x2 + r2["width"] <= x1 or
            y1 + r1["length"] <= y2 or
            y2 + r2["length"] <= y1
        )
