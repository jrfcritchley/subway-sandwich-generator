import itertools

bread = ["Wheat Bread ","White Bread ","Italian Herb & Cheese ","Malted Rye ","Plain Wrap ","Gluten Free Wrap ","Multigrain Wrap "]
cheese = ["Natural Cheddar Cheese ","Mozzarella Cheese ","Old English Cheese "]
veg = ["Avocado ","Capsicum ","Carrots ","Cucumbers ","Lettuce ","Onions ","Spinach ","Jalapeno ","Olives ","Pickles "]
sauce = ["Habanero Hot Sauce ","Blue Cheese Dressing ","Smoky BBQ ","Chipotle Southwest ","Mayonnaise ","Garlic Aioli ","Sweet Onion ","Honey Mustard ","Ranch Dressing ","Tomato Sauce ","Spicy Mayo "] 
extras = ["Crispy Onions ","Chilli Flakes ","Mixed Seeds ","Sea Salt ","Mixed Peppercorns "]

ing = bread+cheese+veg+sauce+extras
#print(len(ing))
for i in range(len(ing) + 1):
    for subset in itertools.combinations(ing, i):
        print(subset)
    
