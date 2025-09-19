from workoutplanner import generate_workout

def main():
    print("=== AI Workout Planner ===")
    muscle_group = input("Enter a muscle group (e.g., chest, back, legs, or something specific like 'rhomboids'): ")
    goal = input("Enter your goal (strength, hypertrophy, endurance, or leave blank for default 'strength'): ").strip().lower()
    num_exercises = input("How many exercises do you want? (default 3): ")

    if num_exercises.isdigit():
        num_exercises = int(num_exercises)
    else:
        num_exercises = 3

    # Get workout plan (list of exercises)
    exercises = generate_workout(muscle_group, num_exercises, goal if goal else None)

    if isinstance(exercises, str):  # error message from generator
        print("\n" + exercises)
    else:
        #print(f"\n💪 {muscle_group.capitalize()} Workout Plan" + (f" ({goal})" if goal else " (strength)") + ":")
        #print(f"\n💪 Workout plan for {muscle_group}" + (f" {goal}" if goal else " strength" + ":"))
        print(f"\n💪 {muscle_group.capitalize()} workout plan:")
        for i, ex in enumerate(exercises, 1):
            equip = ex.get("equipment", [])
            if isinstance(equip, list):
                equip_str = ", ".join(equip)
            else:
                equip_str = str(equip)

            print(f"{i}. {ex['name']} ({equip_str}, {ex.get('time', '?')} min) - Sets: {ex.get('sets')} Reps: {ex.get('reps')}")

if __name__ == "__main__":
    main()
