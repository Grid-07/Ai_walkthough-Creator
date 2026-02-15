class FloorPlanValidator:

    def validate(self, floor_plan):
        errors = []

        rooms = floor_plan.get("rooms", [])

        if not rooms:
            errors.append("No rooms defined.")

        for i, room in enumerate(rooms):
            width = room.get("width", 0)
            length = room.get("length", 0)

            if width <= 0 or length <= 0:
                errors.append(f"Room {room.get('name')} has invalid dimensions.")

            if width < 1 or length < 1:
                errors.append(f"Room {room.get('name')} dimensions unrealistically small.")

        # Check overlaps
        overlaps = self._check_overlaps(rooms)
        errors.extend(overlaps)

        return {
            "valid": len(errors) == 0,
            "errors": errors
        }

    def _check_overlaps(self, rooms):
        overlap_errors = []

        for i in range(len(rooms)):
            for j in range(i + 1, len(rooms)):
                if self._rooms_overlap(rooms[i], rooms[j]):
                    overlap_errors.append(
                        f"Rooms '{rooms[i]['name']}' and '{rooms[j]['name']}' overlap."
                    )

        return overlap_errors

    def _rooms_overlap(self, r1, r2):
        x1, y1 = r1["position"]
        x2, y2 = r2["position"]

        return not (
            x1 + r1["width"] <= x2 or
            x2 + r2["width"] <= x1 or
            y1 + r1["length"] <= y2 or
            y2 + r2["length"] <= y1
        )
