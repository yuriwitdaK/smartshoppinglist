def main():
    print("WELCOME IN SMARTSHOPPING LIST")

if __name__ == "__main__":
    main()

ingredients = {
"rice": {"price": 1.79, "weight": 1000, "kcal": 130},
"pasta": {"price": 1.09, "weight": 500, "kcal": 131},
"chicken breast": {"price": 6.99, "weight": 400, "kcal": 165},
"salmon": {"price": 6.49, "weight": 300, "kcal": 208},
"eggs": {"price": 2.99, "weight": 10, "kcal": 155},
"milk": {"price": 1.19, "weight": 1000, "kcal": 42},
"ground beef": {"price": 5.99, "weight": 500, "kcal": 250},
"garlic": {"price": 1.29, "weight": 200, "kcal": 149},
"onion": {"price": 0.99, "weight": 1000, "kcal": 40},
"potatoes": {"price": 3.49, "weight": 2500, "kcal": 77},
"tomatoes": {"price": 2.79, "weight": 1000, "kcal": 18},
"bell pepper": {"price": 2.99, "weight": 500, "kcal": 26},
"cucumber": {"price": 1.19, "weight": 400, "kcal": 15},
"carrots": {"price": 1.49, "weight": 1000, "kcal": 41},
"broccoli": {"price": 2.29, "weight": 500, "kcal": 34},
"cauliflower": {"price": 2.49, "weight": 600, "kcal": 25},
"spinach": {"price": 2.29, "weight": 450, "kcal": 23},
"lettuce": {"price": 1.59, "weight": 300, "kcal": 15},
"apple": {"price": 3.49, "weight": 1000, "kcal": 52},
"banana": {"price": 1.99, "weight": 1000, "kcal": 89},
"orange": {"price": 2.99, "weight": 1000, "kcal": 47},
"lemon": {"price": 2.49, "weight": 500, "kcal": 29},
"avocado": {"price": 1.99, "weight": 200, "kcal": 160},
"olive oil": {"price": 7.99, "weight": 1000, "kcal": 884},
"sunflower oil": {"price": 3.49, "weight": 1000, "kcal": 884},
"butter": {"price": 2.79, "weight": 250, "kcal": 717},
"cheese": {"price": 3.99, "weight": 250, "kcal": 402},
"mozzarella": {"price": 1.49, "weight": 125, "kcal": 280},
"yogurt": {"price": 0.89, "weight": 150, "kcal": 60},
"cream": {"price": 1.49, "weight": 200, "kcal": 340},
"bread": {"price": 2.49, "weight": 1000, "kcal": 265},
"toast": {"price": 1.99, "weight": 500, "kcal": 260},
"flour": {"price": 1.29, "weight": 1000, "kcal": 364},
"sugar": {"price": 1.39, "weight": 1000, "kcal": 387},
"salt": {"price": 0.69, "weight": 500, "kcal": 0},
"pepper": {"price": 2.99, "weight": 100, "kcal": 251},
"paprika powder": {"price": 2.49, "weight": 100, "kcal": 282},
"chili powder": {"price": 2.29, "weight": 100, "kcal": 282},
"basil": {"price": 1.79, "weight": 20, "kcal": 233},
"oregano": {"price": 1.79, "weight": 20, "kcal": 265},
"parsley": {"price": 1.29, "weight": 30, "kcal": 36},
"thyme": {"price": 1.79, "weight": 20, "kcal": 276},
"rosemary": {"price": 1.89, "weight": 20, "kcal": 131},
"beef steak": {"price": 8.99, "weight": 300, "kcal": 271},
"pork chops": {"price": 6.49, "weight": 500, "kcal": 242},
"bacon": {"price": 3.99, "weight": 200, "kcal": 541},
"ham": {"price": 2.99, "weight": 150, "kcal": 145},
"sausage": {"price": 3.49, "weight": 300, "kcal": 301},
"tofu": {"price": 2.99, "weight": 400, "kcal": 76},
"tempeh": {"price": 3.99, "weight": 400, "kcal": 192},
"lentils": {"price": 2.49, "weight": 500, "kcal": 116},
"chickpeas": {"price": 1.99, "weight": 500, "kcal": 164},
"beans": {"price": 2.29, "weight": 500, "kcal": 127},
"peas": {"price": 2.19, "weight": 450, "kcal": 81},
"corn": {"price": 1.49, "weight": 300, "kcal": 96},
"mushrooms": {"price": 2.49, "weight": 400, "kcal": 22},
"zucchini": {"price": 2.19, "weight": 500, "kcal": 17},
"eggplant": {"price": 2.49, "weight": 500, "kcal": 25},
"cabbage": {"price": 1.99, "weight": 1000, "kcal": 25},
"red cabbage": {"price": 2.49, "weight": 1000, "kcal": 31},
"brussels sprouts": {"price": 3.49, "weight": 750, "kcal": 43},
"leek": {"price": 2.19, "weight": 500, "kcal": 31},
"celery": {"price": 1.89, "weight": 400, "kcal": 16},
"pumpkin": {"price": 2.99, "weight": 1000, "kcal": 26},
"apple juice": {"price": 2.19, "weight": 1000, "kcal": 46},
"orange juice": {"price": 2.49, "weight": 1000, "kcal": 45},
"coffee": {"price": 6.99, "weight": 500, "kcal": 2},
"tea": {"price": 3.99, "weight": 100, "kcal": 1},
"honey": {"price": 4.49, "weight": 500, "kcal": 304},
"jam": {"price": 2.99, "weight": 450, "kcal": 250},
"chocolate": {"price": 1.79, "weight": 100, "kcal": 546},
"cookies": {"price": 2.49, "weight": 200, "kcal": 480},
"cereal": {"price": 3.49, "weight": 500, "kcal": 380},
"oats": {"price": 1.79, "weight": 1000, "kcal": 389},
"nuts": {"price": 5.49, "weight": 200, "kcal": 607},
"almonds": {"price": 5.99, "weight": 200, "kcal": 579},
"walnuts": {"price": 6.49, "weight": 200, "kcal": 654},
"raisins": {"price": 2.49, "weight": 250, "kcal": 299},
"buttermilk": {"price": 1.29, "weight": 1000, "kcal": 42},
"cream cheese": {"price": 1.79, "weight": 200, "kcal": 253},
"cottage cheese": {"price": 1.99, "weight": 200, "kcal": 98},
"quark": {"price": 1.59, "weight": 250, "kcal": 68},
"ice cream": {"price": 3.99, "weight": 500, "kcal": 207},
"frozen pizza": {"price": 3.49, "weight": 400, "kcal": 260},
"frozen vegetables": {"price": 2.99, "weight": 750, "kcal": 50}
}

recipes = [
    {
        "name": "Spaghetti Bolognese",
        "servings": 4,
        "ingredients": {"pasta": 500, "ground beef": 300, "onion": 1, "tomatoes": 3},
    },
    {
        "name": "Pasta Alfredo",
        "servings": 4,
        "ingredients": {"pasta": 500, "butter": 50, "cheese": 100, "milk": 200},
    },
    {
        "name": "Omelette",
        "servings": 2,
        "ingredients": {"eggs": 3, "cheese": 20, "milk": 30},
    },
    {
        "name": "Chicken Salad",
        "servings": 2,
        "ingredients": {"chicken breast": 200, "lettuce": 100, "tomatoes": 50},
    },
    {
        "name": "Veggie Stirfry",
        "servings": 2,
        "ingredients": {"rice": 200, "broccoli": 100, "carrots": 100, "garlic": 5},
    },
    {
        "name": "Bean Stew",
        "servings": 4,
        "ingredients": {"beans": 200, "lentils": 100, "onion": 50, "tomatoes": 100},
    },
    {
        "name": "Salmon with Potatoes",
        "servings": 2,
        "ingredients": {"salmon": 200, "potatoes": 300, "lemon": 10},
    },
]

stock = [{}]

def is_protein(recipe):
    """Überprüft ob es dich buff machen wird"""
    # match keys used in `ingredients` dict
    protein_sources = {"chicken breast", "ground beef", "salmon", "beef steak", "pork chops", "tuna", "eggs", "tofu", "tempeh", "lentils", "chickpeas"}
    return any(item in protein_sources for item in recipe["ingredients"])

def cost_per_recipe(recipe, ingredients):
    """Berechnet rezeptkosten."""
    total = 0
    for name, amount in recipe["ingredients"].items():
        if name in ingredients:
            price_per_unit = ingredients[name]["price"] / ingredients[name]["weight"]
            total += price_per_unit * amount
    return  total

def plan_weekly_meals(recipes, ingredients, stock, weekly_budget):
    """plant 3 Mahlzeiten am Tag für die Woche.

    Uses a dynamic scoring function that penalizes recipes already used on multiple days
    and a lightweight backtracking pass to replace overused recipes when possible.
    """
    plan = []
    budget_left = weekly_budget

    from collections import defaultdict
    usage_days = defaultdict(set)  # recipe name -> set of day indices

    # dynamic selection: before each meal, compute a score = cost + penalty*used_days
    PENALTY_PER_USED_DAY = 0.5

    for day in range(7):
        day_meals = []
        proteins_added = 0

        for meal in range(3):
            # build candidates dynamically with score
            def score_fn(r):
                c = cost_per_recipe(r, ingredients)
                used = len(usage_days[r["name"]])
                return c + PENALTY_PER_USED_DAY * used

            candidates = sorted(recipes, key=score_fn)

            selected = None

            # first try to find a protein if needed
            if proteins_added < 1:
                for recipe in candidates:
                    cost = cost_per_recipe(recipe, ingredients)
                    if cost > budget_left:
                        continue
                    # prefer protein recipes
                    if is_protein(recipe):
                        # avoid creating a 3rd distinct day if an alternative exists
                        name = recipe["name"]
                        adds_new_day = day not in usage_days[name]
                        if adds_new_day and len(usage_days[name]) >= 2:
                            # see if alternative protein exists
                            alt_found = False
                            for alt in candidates:
                                if alt["name"] == name:
                                    continue
                                if cost_per_recipe(alt, ingredients) > budget_left:
                                    continue
                                if is_protein(alt):
                                    alt_found = True
                                    break
                            if alt_found:
                                continue
                        selected = recipe
                        break

            # if still not selected, pick cheapest candidate that fits budget and doesn't violate diversity when possible
            if selected is None:
                for recipe in candidates:
                    cost = cost_per_recipe(recipe, ingredients)
                    if cost > budget_left:
                        continue
                    name = recipe["name"]
                    adds_new_day = day not in usage_days[name]
                    if adds_new_day and len(usage_days[name]) >= 2:
                        # look for alternative; if exists, skip this recipe to improve diversity
                        alt_found = False
                        for alt in candidates:
                            if alt["name"] == name:
                                continue
                            if cost_per_recipe(alt, ingredients) > budget_left:
                                continue
                            alt_found = True
                            break
                        if alt_found:
                            continue
                    selected = recipe
                    break

            if selected:
                day_meals.append(selected)
                sel_name = selected["name"]
                usage_days[sel_name].add(day)
                budget_left -= cost_per_recipe(selected, ingredients)
                if is_protein(selected):
                    proteins_added += 1

        plan.append(day_meals)

    # lightweight backtracking: for recipes used on >2 distinct days, try replacing occurrences
    remaining_budget = budget_left
    occurrence_days = {name: set(days) for name, days in usage_days.items()}

    # iterate over overused recipes and try to replace occurrences
    for name, days in list(occurrence_days.items()):
        while len(days) > 2:
            replaced = False
            # try each day where this recipe appears
            for day_idx in sorted(days):
                # find positions in that day's meals where this recipe is used
                positions = [i for i, m in enumerate(plan[day_idx]) if m["name"] == name]
                if not positions:
                    # should not happen, but guard
                    continue
                pos = positions[0]
                orig_recipe = plan[day_idx][pos]
                orig_cost = cost_per_recipe(orig_recipe, ingredients)

                # try alternatives sorted by cost
                for alt in sorted(recipes, key=lambda r: cost_per_recipe(r, ingredients)):
                    alt_name = alt["name"]
                    if alt_name == name:
                        continue
                    alt_cost = cost_per_recipe(alt, ingredients)
                    # would replacing keep budget non-negative?
                    if alt_cost > orig_cost + remaining_budget:
                        continue
                    # would alt be used on more than 2 days after replacement?
                    alt_days = occurrence_days.get(alt_name, set())
                    adds_new_day = day_idx not in alt_days
                    if adds_new_day and len(alt_days) >= 2:
                        continue
                    # preserve protein requirement: after replacement, the day should still have at least one protein
                    day_other_meals = [m for i, m in enumerate(plan[day_idx]) if i != pos]
                    has_protein = any(is_protein(m) for m in day_other_meals)
                    if not has_protein and not is_protein(alt):
                        continue

                    # perform replacement
                    plan[day_idx][pos] = alt

                    # update occurrence sets
                    # remove day from original name if no other meal of that day uses it
                    still_on_day = any(m["name"] == name for m in plan[day_idx])
                    if not still_on_day:
                        occurrence_days[name].remove(day_idx)
                    # add day to alt occurrence
                    occurrence_days.setdefault(alt_name, set()).add(day_idx)

                    # update remaining budget
                    remaining_budget = remaining_budget + orig_cost - alt_cost
                    days = occurrence_days[name]
                    replaced = True
                    break

                if replaced:
                    break

            if not replaced:
                # cannot reduce further for this recipe
                break

    return plan, round(remaining_budget, 2)

"""Festgelegtes wöchentliches Budget"""
weekly_budget = 100
weekly_plan, remaining_budget = plan_weekly_meals(recipes, ingredients, stock, weekly_budget)

"""Fehlermeldung wenn wochenbudget überschritten wird und nicht an allen Tagen 3 Mahlzeiten gewährleistet sind"""
# Warn if remaining budget is negative or any day has fewer than 3 meals
warning_triggered = (remaining_budget < 0 or any(len(day) < 3 for day in weekly_plan))

# Check for repeated meals (>2 days) where alternatives exist that wouldn't exceed the budget
from collections import defaultdict
occurrence_days = defaultdict(set)
for day_idx, day in enumerate(weekly_plan):
    for recipe in day:
        occurrence_days[recipe["name"]].add(day_idx)

repeat_warnings = []
for name, days in occurrence_days.items():
    if len(days) > 2:
        # find the original recipe object and its cost
        orig_recipe = next((r for r in recipes if r["name"] == name), None)
        if orig_recipe is None:
            continue
        orig_cost = cost_per_recipe(orig_recipe, ingredients)

        # look for any alternative recipe that could replace one occurrence without exceeding budget
        alt_exists = False
        for alt in recipes:
            if alt["name"] == name:
                continue
            alt_cost = cost_per_recipe(alt, ingredients)
            # substitution is possible if alt_cost <= orig_cost + remaining_budget
            if alt_cost <= orig_cost + remaining_budget:
                alt_exists = True
                break

        if alt_exists:
            repeat_warnings.append(f'Note: "{name}" appears on {len(days)} days. Consider replacing some occurrences — budget allows alternatives.')

if warning_triggered:
    print("Warning: The weekly budget was exceeded or not all days have 3 meals planned.")
    print(f"Budget left: {remaining_budget:.2f} €")
else:
    # Print repeat warnings (if any) before the plan
    for w in repeat_warnings:
        print(w)

    #Ausgabe
    for i, day in enumerate(weekly_plan, 1):
        print(f"Tag {i}:")
        for meal in day:
            print("-", meal["name"])
    print(f"Budget left: {remaining_budget:.2f} €")