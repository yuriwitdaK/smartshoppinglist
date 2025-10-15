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

recipes = [ {
        "name": "Spaghetti Bolognese",
        "servings": 4,
        "ingredients": {
            "pasta": 500,
            "ground beef": 300,
            "onion": 1,
            "tomatoes": 3
        }
    },
    {
        "name": "Pasta Alfredo",
        "servings": 4,
        "ingredients": {
            "pasta": 500,
            "butter": 50,
            "cheese": 100,
            "milk": 200
        }
    }]

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
    """plant 3 Mahlzeiten am Tag für die Woche."""
    plan = []
    budget_left = weekly_budget

    #sortiert pro portion (günstig -> teuer)
    recipes_sorted = sorted(recipes, key=lambda r: cost_per_recipe(r, ingredients))

    for day in range(7):
        day_meals = []
        proteins_added = 0
        for meal in range(3):
            for recipe in recipes_sorted:
                cost = cost_per_recipe(recipe, ingredients)
                if cost <= budget_left:
                   #eiweißquelle: min 1 pro Tag
                    if proteins_added < 1 and is_protein(recipe):
                        day_meals.append(recipe)
                        budget_left -= cost
                        proteins_added += 1
                        break
                    elif not is_protein(recipe):
                        day_meals.append(recipe)
                        budget_left -= cost
                        break
        plan.append(day_meals)

    return plan, round(budget_left, 2)

"""Festgelegtes wöchentliches Budget"""
weekly_budget = 50
weekly_plan, remaining_budget = plan_weekly_meals(recipes, ingredients, stock, weekly_budget)

#Ausgabe
for i, day in enumerate(weekly_plan, 1):
    print(f"Tag {i}:")
    for meal in day:
        print("-", meal["name"])
print(f"Budget left: {remaining_budget:.2f} €")