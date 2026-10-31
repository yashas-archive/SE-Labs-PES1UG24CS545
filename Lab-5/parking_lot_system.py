
"""Manage parking slots, fees, vehicle hashes, and parking manifests."""

import hashlib
import secrets

PARKING_SLOTS = {
    "P01": {
        "plate": "KA01AB1234",
        "hours": 2,
        "rate": 20.0,
        "is_occupied": True,
    },
    "P02": {
        "plate": "TN07CD5678",
        "hours": 0,
        "rate": 20.0,
        "is_occupied": False,
    },
    "P03": {
        "plate": "MH02EF9012",
        "hours": 4,
        "rate": 30.0,
        "is_occupied": True,
    },
}

TOTAL_COLLECTIONS = 0.0


def park_vehicle(slot_id, plate_no, hours_booked=1, entry_logs=None):
    """Park a vehicle and record its parking charge."""
    global TOTAL_COLLECTIONS

    if slot_id not in PARKING_SLOTS:
        return False
    if PARKING_SLOTS[slot_id]["is_occupied"]:
        return False
    if not isinstance(hours_booked, int) or isinstance(hours_booked, bool):
        return False
    if hours_booked < 1:
        return False

    slot = PARKING_SLOTS[slot_id]
    slot["plate"] = plate_no
    slot["hours"] = hours_booked
    slot["is_occupied"] = True
    charge = slot["rate"] * hours_booked
    TOTAL_COLLECTIONS += charge

    if entry_logs is None:
        entry_logs = []
    entry_logs.append(
        f"Vehicle {plate_no} parked at slot {slot_id} "
        f"for {hours_booked} hours; charge: {charge:.2f}"
    )
    return True


def release_slot(slot_id):
    """Release an occupied slot; return False for an unknown slot."""
    if slot_id not in PARKING_SLOTS:
        return False

    slot = PARKING_SLOTS[slot_id]
    slot["is_occupied"] = False
    slot["plate"] = ""
    slot["hours"] = 0
    return True


def check_slot_availability(slot_id):
    """Return whether a known parking slot is vacant."""
    slot = PARKING_SLOTS.get(slot_id)
    return slot is not None and not slot["is_occupied"]


def calculate_parking_fee(slot_id, surge_multiplier=1.5):
    """Calculate a slot's hourly rate multiplied by a surge factor."""
    if slot_id not in PARKING_SLOTS:
        raise ValueError(f"Unknown parking slot: {slot_id}")
    if not isinstance(surge_multiplier, (int, float)):
        raise ValueError("Surge multiplier must be numeric.")
    if isinstance(surge_multiplier, bool) or surge_multiplier < 0:
        raise ValueError("Surge multiplier must be non-negative.")

    base_rate = PARKING_SLOTS[slot_id]["rate"]
    return base_rate * surge_multiplier


def generate_vehicle_hash(plate_no):
    """Generate a SHA-256 hash for a vehicle registration number."""
    return hashlib.sha256(plate_no.encode("utf-8")).hexdigest()


def generate_ticket_pin():
    """Generate a four-digit PIN using a cryptographically secure source."""
    return secrets.randbelow(9000) + 1000


def export_parking_manifest(filename="parking_manifest.txt"):
    """Export parking slot details to a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as manifest:
        manifest.write(str(PARKING_SLOTS))
    print(f"Parking manifest exported to: {filename}")


def get_available_summary(slots):
    """Count the vacant slots in the supplied parking-slot dictionary."""
    return sum(
        not details["is_occupied"] for details in slots.values()
    )


def main():
    """Run a demonstration of the parking management functions."""
    park_vehicle("P02", "DL03GH3456", 3)
    release_slot("P01")

    print("Is P02 available:", check_slot_availability("P02"))
    print("Surge Parking Fee:", calculate_parking_fee("P03", 1.50))
    print("Vehicle Hash:", generate_vehicle_hash("KA01AB1234"))
    print("Ticket PIN:", generate_ticket_pin())
    export_parking_manifest()
    print("Vacant slots:", get_available_summary(PARKING_SLOTS))
    print("Total collections:", TOTAL_COLLECTIONS)


if __name__ == "__main__":
    main()
