import workoutplanner

if __name__ == "__main__":
    print("💪 AI Workout Planner Prototype")
    
    # User input
    goal = input("Enter your goal (strength / hypertrophy"" / endurance): ").strip()
    equipment = input("Enter equipment (bodyweight / dumbbell / barbell / machine): ").strip()
    days = int(input("How many days per week do you want to train? "))

    # Generate workout
    workout_plan = workoutplanner(goal, equipment, days)

    # Output
    print("\n📅 Your Weekly Workout Plan:")
    for day, exercises_list in workout_plan.items():
        print(f"\n{day}:")
        for ex in exercises_list:
            print(f" - {ex}")