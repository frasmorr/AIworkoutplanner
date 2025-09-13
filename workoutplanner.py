import random
import exercises, goals

def generate_workout(goals, equipment, days):
    plan = {}
    muscle_groups = list(exercises.keys())
    random.shuffle(muscle_groups)

    # Rotate muscle groups across workout days
    for day in range(1, days + 1):
        day_plan = []
        selected_muscles = random.sample(muscle_groups, 3)  # 3 muscle groups per workout
        for muscle in selected_muscles:
            available_exercises = exercises[muscle].get(equipment, [])
            if available_exercises:
                exercise = random.choice(available_exercises)
                prescription = f"{exercise} - {goals[goal]['sets']} sets of {goals[goal]['reps']} reps"
                day_plan.append(prescription)
        plan[f"Day {day}"] = day_plan