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
    # breakfast recipes (quick/light)
    {
        "name": "Pancakes",
        "servings": 2,
        "prep_time": 15,
        "is_breakfast": True,
        "ingredients": {"flour": 150, "milk": 150, "eggs": 1, "butter": 10},
    },
    {
        "name": "Granola Yogurt",
        "servings": 1,
        "prep_time": 5,
        "is_breakfast": True,
        "ingredients": {"yogurt": 150, "oats": 50, "honey": 10},
    },
    {
        "name": "Avocado Toast",
        "servings": 1,
        "prep_time": 5,
        "is_breakfast": True,
        "ingredients": {"bread": 50, "avocado": 50, "lemon": 5},
    },
    {
        "name": "Breakfast Burrito",
        "servings": 1,
        "prep_time": 12,
        "is_breakfast": True,
        "ingredients": {"eggs": 2, "cheese": 20, "bread": 50},
    },
    {
        "name": "Smoothie",
        "servings": 1,
        "prep_time": 5,
        "is_breakfast": True,
        "ingredients": {"banana": 150, "milk": 150, "yogurt": 50},
    },
    # weekend heftier recipes
    {
        "name": "Roast Beef",
        "servings": 4,
        "prep_time": 120,
        "weekend": True,
        "ingredients": {"beef steak": 800, "potatoes": 1000, "carrots": 300},
    },
    {
        "name": "Lasagna",
        "servings": 6,
        "prep_time": 90,
        "weekend": True,
        "ingredients": {"pasta": 300, "ground beef": 400, "cheese": 200, "tomatoes": 200},
    },
]

stock = [{}]

# diagnostic flag: when True print per-meal per-ingredient kcal breakdown
DEBUG_KCAL = False

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


def kcal_per_recipe(recipe, ingredients):
    """Compute total kcal for the recipe using ingredient kcal metadata."""
    total = 0
    for name, amount in recipe["ingredients"].items():
        if name in ingredients and "kcal" in ingredients[name]:
            meta = ingredients[name]
            pkg_weight = meta.get("weight", 0)
            kcal_meta = meta.get("kcal", 0)
            # Heuristic: if package weight is small (e.g. <100) treat kcal as per-item (piece)
            # otherwise treat kcal as kcal per 100g and scale accordingly.
            if pkg_weight > 0 and pkg_weight < 100:
                # per-item kcal
                kcal_per_unit = kcal_meta
            elif pkg_weight >= 100:
                # assume kcal_meta is per 100g if weight looks like grams per package
                # convert to per-gram then multiply
                kcal_per_unit = (kcal_meta / 100.0)
            else:
                kcal_per_unit = kcal_meta
            total += kcal_per_unit * amount
    return total


def meals_from_packages(recipe, ingredients):
    """Estimate how many servings of this recipe you can make from standard package sizes.

    For each ingredient, compute how many whole recipe-amounts fit into one package and
    return the minimum across ingredients (floor). Then multiply by servings to get
    approximate number of individual servings (meals) per package set.
    """
    import math
    counts = []
    for name, amount in recipe["ingredients"].items():
        if name in ingredients and ingredients[name]["weight"] > 0:
            pkg_weight = ingredients[name]["weight"]
            # how many recipe-amounts fit in one package
            counts.append(math.floor(pkg_weight / amount) if amount > 0 else 0)
        else:
            # unknown ingredient: assume at least 1
            counts.append(1)
    if not counts:
        return 1
    # servings in the recipe means how many individual plates are produced
    per_package_recipe_counts = min(counts)
    return max(1, per_package_recipe_counts * recipe.get("servings", 1))

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
        # track breakfast recipes used earlier in this week to encourage variety
        if 'breakfast_used_names' not in locals():
            breakfast_used_names = set()
        # reserved multi-day meals created by earlier long-prep selections
        if 'reserved_slots' not in locals():
            reserved_slots = {}

        for meal in range(3):
            # check if this slot was reserved by a previous long-prep cooking
            reserved_key = (day, meal)
            reserved_entry = reserved_slots.get(reserved_key)
            if reserved_entry:
                # use reserved recipe without charging cost again
                selected = reserved_entry['recipe']
                name = selected['name']
                day_meals.append(selected)
                usage_days[name].add(day)
                if is_protein(selected):
                    proteins_added += 1
                # if this was a breakfast slot, mark recipe as used for breakfast variety
                if meal == 0 and selected.get('is_breakfast'):
                    breakfast_used_names.add(name)
                # mark as used and continue to next meal (no selection logic)
                continue
            # build candidates dynamically with score
            def score_fn(r):
                c = cost_per_recipe(r, ingredients)
                used = len(usage_days[r["name"]])
                return c + PENALTY_PER_USED_DAY * used

            # make breakfast a soft preference: don't restrict pool, but bias breakfast recipes
            pool = recipes

            def score_fn(r):
                # New scoring: 50% based on cost-effectiveness (kcal per euro, higher better)
                # and 50% based on how many meals can be prepared from packages (higher better).
                # We invert the combined metric to produce a sort key where lower is better.
                cost = cost_per_recipe(r, ingredients)
                kcal = kcal_per_recipe(r, ingredients)
                kcal_per_euro = (kcal / cost) if cost > 0 else kcal
                meals_pkg = meals_from_packages(r, ingredients)

                # normalize components: we want higher is better for both, combine equally
                # combined_score_raw: higher is better
                combined_raw = 0.5 * kcal_per_euro + 0.5 * meals_pkg

                # penalize by number of days used
                used = len(usage_days[r["name"]])
                penalty = PENALTY_PER_USED_DAY * used

                # weekend preference: on day 5-6 (0-based), prefer weekend recipes (improve score)
                weekend_bonus = -1.0 if (day >= 5 and r.get("weekend")) else 0.0
                # breakfast soft preference: for the first meal, slightly boost breakfast recipes
                breakfast_bonus = -0.5 if (meal == 0 and r.get("is_breakfast")) else 0.0

                # We want a sort key where lower is better, so invert combined_raw and add penalties
                # Add a tiny constant to avoid division by zero
                sort_key = -combined_raw + penalty + weekend_bonus + breakfast_bonus
                return sort_key

            candidates = sorted(pool, key=score_fn)

            selected = None

            # first try to find a protein if needed
            if proteins_added < 1:
                # detect if there exists an unused breakfast candidate (affordable)
                breakfast_nonused_exists = False
                if meal == 0:
                    for b in candidates:
                        if b.get('is_breakfast') and b['name'] not in breakfast_used_names and cost_per_recipe(b, ingredients) <= budget_left:
                            breakfast_nonused_exists = True
                            break
                for recipe in candidates:
                    cost = cost_per_recipe(recipe, ingredients)
                    if cost > budget_left:
                        continue
                    # prefer protein recipes
                    if is_protein(recipe):
                        # avoid creating a 3rd distinct day if an alternative exists
                        name = recipe["name"]
                        # don't schedule same recipe more than once per day unless allowed
                        if any(m["name"] == name for m in day_meals):
                            if not (recipe.get("allow_multi_meal") or recipe.get("prep_time", 0) > 30):
                                continue
                        # if this is breakfast and there is an unused breakfast candidate, avoid repeats
                        if meal == 0 and recipe.get('is_breakfast') and recipe['name'] in breakfast_used_names and breakfast_nonused_exists:
                            continue
                        adds_new_day = day not in usage_days[name]
                        if adds_new_day and len(usage_days[name]) >= 2:
                            # see if alternative protein exists
                                alt_found = False
                                for alt in candidates:
                                    if alt["name"] == name:
                                        continue
                                    if cost_per_recipe(alt, ingredients) > budget_left:
                                        continue
                                    # alt would add a new day for alt_name?
                                    alt_adds_new_day = day not in usage_days[alt["name"]]
                                    # prefer alternatives that would NOT create a 3rd distinct day
                                    if not alt_adds_new_day or len(usage_days[alt["name"]]) < 2:
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
                    # don't schedule same recipe more than once per day unless allowed
                    name = recipe["name"]
                    if any(m["name"] == name for m in day_meals):
                        if not (recipe.get("allow_multi_meal") or recipe.get("prep_time", 0) > 30):
                            continue
                    # if this is breakfast and there is an unused breakfast candidate, avoid repeats
                    if meal == 0:
                        # recompute breakfast_nonused_exists for this loop
                        breakfast_nonused_exists = any(
                            (b.get('is_breakfast') and b['name'] not in breakfast_used_names and cost_per_recipe(b, ingredients) <= budget_left)
                            for b in candidates
                        )
                        if recipe.get('is_breakfast') and recipe['name'] in breakfast_used_names and breakfast_nonused_exists:
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
                            alt_adds_new_day = day not in usage_days[alt["name"]]
                            if not alt_adds_new_day or len(usage_days[alt["name"]]) < 2:
                                alt_found = True
                                break
                        if alt_found:
                            continue
                    # Prevent scheduling the same recipe 4 times in a row across meals
                    # Count consecutive occurrences ending at the previous meal
                    consecutive = 0
                    # check previous meals in this day
                    for prev_i in range(len(day_meals)-1, max(-1, len(day_meals)-4), -1):
                        if prev_i < 0:
                            break
                        if day_meals[prev_i]["name"] == name:
                            consecutive += 1
                        else:
                            break
                    # if we need to look into previous day meals to reach 4
                    if consecutive < 3 and day > 0:
                        # look at previous day's last meals
                        prev_day = plan[day-1] if day-1 < len(plan) else []
                        for prev_i in range(len(prev_day)-1, max(-1, len(prev_day)-4), -1):
                            if prev_i < 0:
                                break
                            if prev_day[prev_i]["name"] == name:
                                consecutive += 1
                            else:
                                break

                    if consecutive >= 3:
                        # selecting this would create 4 identical meals in a row; skip
                        continue

                    selected = recipe
                    break

            if selected is None:
                # debug: show why no candidate was chosen
                print(f"DEBUG: no selection for day {day} meal {meal}; budget_left={budget_left:.2f}")
                print("DEBUG: candidates and costs:")
                for r in candidates:
                    c = cost_per_recipe(r, ingredients)
                    print(f"  - {r['name']}: cost={c:.2f}, used_days={len(usage_days[r['name']])}, is_breakfast={r.get('is_breakfast')}, weekend={r.get('weekend')}")

            if selected:
                day_meals.append(selected)
                sel_name = selected["name"]
                usage_days[sel_name].add(day)
                # charge cost for this cooking session. If this recipe is a long-prep and
                # we reserve future slots, we only charge once here (future uses are free).
                budget_left -= cost_per_recipe(selected, ingredients)
                if is_protein(selected):
                    proteins_added += 1
                # if this recipe takes long to prepare, reserve same meal slot for next 2 days (max)
                if selected.get("prep_time", 0) > 30:
                    servings = selected.get("servings", 1)
                    # attempt to cover up to 3 days total (origin + up to 2 more days),
                    # but don't allocate more servings than the recipe provides
                    max_total_meals = min(3, servings)
                    extra_days = max_total_meals - 1
                    for fd in range(1, extra_days + 1):
                        future_day = day + fd
                        if future_day >= 7:
                            break
                        key = (future_day, meal)
                        if key not in reserved_slots:
                            reserved_slots[key] = {"recipe": selected, "origin": day}
                # record breakfast usage for variety
                if meal == 0 and selected.get('is_breakfast'):
                    breakfast_used_names.add(sel_name)

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


def simulate_month(recipes, ingredients, stock, base_weekly_budget, weeks=4):
    """Simulate multiple weeks (default 4) and carry forward positive remaining budget as savings.

    Rules:
    - Start each week with base_weekly_budget + accumulated_savings
    - If a week finishes with remaining_budget > 0, add the positive amount to accumulated_savings
    - After `weeks` weeks (a month), reset accumulated_savings to 0 and report the total saved during the month
    """
    calendar = []
    accumulated = 0.0
    total_saved = 0.0
    for w in range(1, weeks + 1):
        start_budget = base_weekly_budget + accumulated
        plan, rem = plan_weekly_meals(recipes, ingredients, stock, start_budget)
        calendar.append((start_budget, plan, rem))
        if rem > 0:
            accumulated += rem
            total_saved += rem
        # if rem negative, do not deduct from accumulated (we don't borrow)

    # end of month: we reset accumulated (savings used or banked elsewhere)
    return calendar, round(total_saved, 2)


def print_month_calendar(calendar, total_saved):
    print("\nMonthly simulation:")
    for i, (start_budget, plan, rem) in enumerate(calendar, 1):
        print(f"Week {i}: start budget {start_budget:.2f} €, remaining {rem:.2f} €")
        for d, day in enumerate(plan, 1):
            day_kcal = sum(kcal_per_recipe(m, ingredients) for m in day)
            seen = set()
            day_prep = 0
            for m in day:
                if m["name"] in seen:
                    continue
                seen.add(m["name"])
                day_prep += m.get("prep_time", 0)
            print(f"  Day {d}: { [m['name'] for m in day]} (kcal: {int(day_kcal)}, prep: {int(day_prep)}min)")
    print(f"Total saved during month: {total_saved:.2f} €")

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
    # Debug: print per-day meal counts to diagnose incomplete days
    print("\nDebug: per-day meal counts (warning state):")
    for i, day in enumerate(weekly_plan, 1):
        # compute total calories for the day
        day_kcal = sum(kcal_per_recipe(m, ingredients) for m in day)
        # compute total prep time for the day, count each recipe's prep_time once
        seen = set()
        day_prep = 0
        for m in day:
            if m["name"] in seen:
                continue
            seen.add(m["name"])
            day_prep += m.get("prep_time", 0)
        print(f"Day {i}: {len(day)} meals -> {[m['name'] for m in day]} (kcal: {int(day_kcal)}, prep_time: {int(day_prep)} min)")
else:
    # Print repeat warnings (if any) before the plan
    for w in repeat_warnings:
        print(w)

    #Ausgabe
    for i, day in enumerate(weekly_plan, 1):
        day_kcal = sum(kcal_per_recipe(m, ingredients) for m in day)
        # compute prep time (count each recipe once per day)
        seen = set()
        day_prep = 0
        for m in day:
            if m["name"] in seen:
                continue
            seen.add(m["name"])
            day_prep += m.get("prep_time", 0)
        print(f"Tag {i}: (kcal total: {int(day_kcal)}, prep_time: {int(day_prep)} min)")
        for meal in day:
            print("-", meal["name"]) 
        # debug per-meal kcal breakdown
        if DEBUG_KCAL:
            for meal in day:
                kcal_total = kcal_per_recipe(meal, ingredients)
                print(f"  MEAL DEBUG: {meal['name']} -> total kcal: {kcal_total:.2f}")
                for ing, amt in meal['ingredients'].items():
                    if ing in ingredients and 'kcal' in ingredients[ing]:
                        per_unit = ingredients[ing]['kcal'] / ingredients[ing]['weight']
                        print(f"    - {ing}: {amt} units * {per_unit:.4f} kcal/unit = {per_unit*amt:.2f}")
    print(f"Budget left: {remaining_budget:.2f} €")