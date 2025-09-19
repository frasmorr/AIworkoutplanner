import random
from exercises import chestexercises, backexercises, legexercises, shoulderexercises, armexercises, coreexercises
from goals import goals

exercise_db = {
    "chest": chestexercises,
    "back": backexercises,
    "legs": legexercises,
    "shoulders": shoulderexercises,
    "arms": armexercises,
    "core": coreexercises
}

muscle_aliases = {

    #chest other names
    "upper chest": "chest",
    "lower chest": "chest",
    "pecs": "chest",

    #back other names
    "lats": "lats",
    "rhomboids": "rhomboids",
    "traps": "traps",
    "upper back": "back",
    "lower back": "back",

    #legs other names
    "quads": "quads",
    "quadriceps": "quads",
    "hamstrings": "hamstrings",
    "hammies": "hamstrings",
    "glutes": "glutes",
    "butt": "glutes",
    "calves": "calves",
    "calf": "calves",
    "adductors": "adductors",
    "abductors": "abductors",
    "thighs": "quadriceps",
    "thighs": "hamstrings",

    #arms other names
    "biceps": "biceps",
    "triceps": "triceps",
    "forearms": "forearms",
    "brachialis": "biceps",
    "brachioradialis": "biceps",
    "bicep": "biceps",
    "tricep": "triceps",
    "forearm": "forearms",
    "arms": "arms",
    "arm": "arms",
    "upper arms": "biceps",
    "upper arms": "triceps",
    "lower arms": "forearms",

    #shoulders other names
    "delts": "delts",
    "deltoids": "delts",
    "shoulder": "shoulders",
    "shoulders": "shoulders",
    "rotator cuff": "delts",
    "rotator cuffs": "delts",
    "front delts": "anterior delts",
    "front delts": "front delts",
    "side delts": "lateral delts",
    "rear delts": "posterior delts",
    "anterior delts": "anterior delts",
    "lateral delts": "lateral delts",
    "posterior delts": "posterior delts",

    
    #core other names
    "abdominals": "abs",
    "six pack": "abs",
}

def generate_workout(muscle_group, num_exercises=3, goal=None):
    """Generate a workout plan for a given muscle group or alias."""

    muscle_group = muscle_group.lower().strip()
    goal = goal.lower().strip() if goal else "strength"

    # Translate alias → canonical name
    if muscle_group in muscle_aliases:
        target = muscle_aliases[muscle_group]
    else:
        target = muscle_group

    # If the target is a broad category (like 'back'), pull full group
    if target in exercise_db:
        exercises = exercise_db[target]
    else:
        # Otherwise, filter exercises across ALL groups for that muscle
        exercises = []
        for group in exercise_db.values():
            for ex in group:
                if target in [m.lower() for m in ex["muscle"]]:
                    exercises.append(ex)

    if not exercises:
        return f"❌ Sorry, I don't have exercises for '{muscle_group}'."

    # Filter by goal if specified
    exercises = [ex for ex in exercises if goal in ex["goal"]]

    if not exercises:
        return f"❌ No exercises available for '{muscle_group}' with goal '{goal}'."

    selected = random.sample(exercises, min(num_exercises, len(exercises)))

    # Add sets/reps info to each exercise
    for ex in selected:
        ex["sets"] = goals[goal]["sets"]
        ex["reps"] = goals[goal]["reps"]

    return selected