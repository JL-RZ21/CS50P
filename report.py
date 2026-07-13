def main():
    spacecraft = {"name": "Voyager 1"}
    spacecraft.update({"distance": 0.01, "orbit": "SUN"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    =========REPORT========

    Name: {spacecraft["name"]}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ========================
    """

main()