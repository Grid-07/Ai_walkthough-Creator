class FeasibilityAnalyzer:

    def analyze(self, floor_plan):
        warnings = []

        for room in floor_plan.get("rooms", []):
            area = room["width"] * room["length"]

            if area < 6:
                warnings.append(
                    f"Room '{room['name']}' area may be too small ({area} sqm)."
                )

            if room["width"] / room["length"] > 3:
                warnings.append(
                    f"Room '{room['name']}' has disproportionate shape."
                )

        return warnings
