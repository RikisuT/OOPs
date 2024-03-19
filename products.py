import pickle

products = {
    "Hand Wash": 30,
    "Bar Soap": 100,
    "Hand Sanitizer": 20,
    "Floor Cleaner": 200,
    "Disinfectant": 150,
    "Shampoo": 75,
    "Conditioner": 85,
    "Washing Powder": 120,
    "Liquid Soap": 35,
    "Body Wash": 60,
    "Dish Soap Bar": 10,
    "Detergent Bar": 45,
    "Detergent": 10,
    "Toilet Cleaner": 75,
    "Tissue Paper": 40,
    "Cotton Swabs": 20,
    "Sanitary Napkins": 50,
    "Diapers": 100,
    "Deodorants": 25,
    "Talcum Powder": 20,
    "Toothpaste": 20,
    "Toothbrush": 30,
    "Mouthwash": 60,
    "Air Freshener": 150,
    "Glass Cleaner": 120,
    "Fabric Softener": 70,
    "Refill": 60,
    "Naphthalene Balls": 20,
    "Mosquito Repellent": 45,
    "Nail Polish Remover": 50,
    "Body Lotion": 65,
    "Petroleum Jelly": 25,
    "Face-wash": 20,
    "Nail Polish": 40,
    "Eyeliner": 35,
    "Door Mat": 50,
    "Single Bedsheet": 150,
    "Double Bedsheet": 300,
    "Kitchen Towels": 65,
    "Handkerchief": 50,
    "Womens T-shirt": 120,
    "Mens T-shirt": 140,
    "Watch": 220,
    "Yarn": 75,
    "Sewing Kit": 85,
    "Throw Pillow": 99,
    "Notebook": 50,
    "Planner": 180,
    "Gel Pen": 10,
    "Ball Pen": 5,
    "Pencil": 50,
    "Eraser": 5,
    "Sharpener": 5,
    "Ruler": 10,
    "Sketch Pens": 25,
    "Colour Pencil": 95,
    "Diary": 120,
    "Paint Brushes": 75,
    "Watercolour": 120,
    "Acrylic Paint": 100,
    "Palette": 25,
    "Glitter": 10,
    "Colour Paper": 3,
    "Chart Paper": 15,
    "Folder": 10,
    "Pencil Pouch": 65,
    "Metal Ruler": 30,
    "Geometry Box": 110,
    "Drawing Book": 40,
    "Glue": 40,
    "Clip Board": 30,
    "Potato Chips": 35,
    "Banana Chips": 35,
    "Biscuit": 10,
    "Wafers": 25,
    "Toast": 40,
    "Instant Noodles": 10,
    "Chocolate Box": 80,
    "Chocolate Bar": 25,
    "Popcorn": 20,
    "Cheese": 40,
    "Chikki": 5,
    "Wheat Flour(Atta)": 40,
    "Refined Flour(Atta)": 55,
    "Rice": 10,
    "Channa Dal": 80,
    "Urad Dal": 85,
    "Sugar": 50,
    "Tea Powder": 75,
    "Coffee Powder": 70,
    "Milk": 20,
    "Ketchup": 45,
    "Soy Sauce": 50,
    "Mayonnaise": 35,
    "Red Chilli Sauce": 35,
    "Green Chilli Sauce": 35,
    "Masala": 50,
    "Butter": 25,
    "Paneer": 75,
    "Ice Cream": 110,
    "Salt": 55,
    "Bread": 60,
    "Eggs": 70,
    "Apples": 75,
    "Tomatoes": 80,
    "Soy Milk": 90,
    "Yogurt": 100,
    "Cheese slices": 120,
    "Cereal": 130,
    "Pasta": 125,
    "Rice noodles": 127,
    "Olive oil": 45,
    "Cooking oil": 34,
    "Vinegar": 79,
    "Black": 90,
    "Tuna": 56,
    "Frozen vegetables": 57,
    "Frozen fruits": 89,
    "Frozen meals or entrees": 90,
    "Jam": 99,
    "Honey": 89,
    "Cereal bars": 14,
    "Canned soup": 45,
    "Peanuts": 78,
    "Dried fruits": 89,
    "Granulated sugar": 89,
    "Brown sugar": 78,
    "Wheat": 98,
    "Baking powder": 34,
    "Baking soda": 67,
    "Oats": 45,
    "Almonds": 55,
    "Cashews": 22,
    "Pistachios": 33,
    "Walnuts": 44,
    "Hazelnuts": 55,
    "Sunflower seeds": 66,
    "Pumpkin seeds": 77,
    "Chia seeds": 88,
    "Flaxseeds": 140,
    "Quinoa": 400,
    "Couscous": 248,
    "Barley": 67,
    "Millet": 340,
    "Buckwheat": 78,
    "Farro": 99,
    "Tofu": 89,
    "Tempeh": 110,
    "Seitan": 123,
    "Soy sauce": 90,
    "Fish sauce": 78,
    "Oyster sauce": 65,
    "Hoisin sauce": 56,
    "Worcestershire sauce": 45,
    "Sesame oil": 250,
    "Coconut milk": 245,
    "Almond butter": 600,
    "Cashew butter": 120,
    "Peanut oil": 120,
    "Avocado oil": 560,
    "Grapeseed oil": 400,
    "Flaxseed oil": 240,
    "Safflower oil": 370,
    "Sunflower oil": 90,
    "Hazelnut oil": 123,
    "Pumpkin seed oil": 134,
    "Chia seed oil": 213,
    "Coconut oil": 124,
    "Canola oil": 322,
    "Sesame seeds": 156,
    "Poppy seeds": 180,
    "Hemp seeds": 123,
    "Sesame tahini": 200,
    "Date syrup": 128,
    "Molasses": 130,
    "Agave nectar": 198,
    "Coconut sugar": 189,
    "Maple sugar": 85,
    "Palm sugar": 56,
    "Barbecue sauce": 89,
    "Hot sauce": 187,
    "Teriyaki sauce": 132,
    "Sriracha sauce": 230,
    "Tahini": 76,
    "Pesto sauce": 120,
    "Salsa": 230,
    "Hummus": 30,
    "Guacamole": 288,
    "Tzatziki": 100,
    "Aioli": 78,
    "Marinara sauce": 89,
    "Lemons": 120,
    "Spinach": 456,
    "Broccoli": 45,
    "Cauliflower": 56,
    "Bell peppers": 67,
    "Avocados": 87,
    "Cucumbers": 79,
    "Carrots": 98,
    "Onions": 90,
    "Garlic": 76,
    "Celery": 45,
    "Zucchini": 76,
    "Mushrooms": 120,
    "Green beans": 110,
    "Asparagus": 123,
    "Brussels sprouts": 112,
    "Kale": 120,
    "Radishes": 34,
    "Artichokes": 234,
    "Eggplant": 145,
    "Beets": 130,
    "Sweet potatoes": 160,
    "Potatoes": 140,
    "Oranges": 150,
    "Grapefruits": 160,
    "Berries": 190,
    "Kiwis": 180,
    "Mangoes": 123,
    "Pineapples": 112,
    "Papayas": 123,
    "Lemongrass": 340,
    "Starfruit": 200,
    "Passionfruit": 190,
    "Dragonfruit": 180,
    "Guava": 300,
    "Lychee": 90,
    "Plantains": 100,
    "Ugli fruit": 120,
    "Mango": 140,
    "Kiwi": 150,
    "Persimmon": 123,
    "Pomegranate": 127,
    "Jackfruit": 136,
    "Durian": 178,
    "Rambutan": 177,
    "Longan": 180,
    "Tamarillo": 120,
    "Ackee": 78,
    "Breadfruit": 200,
    "Mulberry": 210,
    "Loganberry": 345,
    "Boysenberry": 230,
    "Elderberry": 67,
    "Gooseberry": 89,
    "Lingonberry": 89,
    "Cloudberry": 98,
    "Cranberry": 56,
    "Bilberry": 129,
    "Saskatoon berry": 139,
    "Marionberry": 179,
    "Artichoke Hearts": 189,
    "Capers": 199,
    "Sun-Dried Tomatoes": 200,
    "Marinated Mushrooms": 159,
    "Roasted Red Peppers": 123,
    "Canned Corn": 56,
    "Dried Lentils": 89,
    "Bulgur": 89,
    "Chia Seeds": 68,
    "Pumpkin Seeds": 390,
    "Sunflower Seeds": 210,
    "Sesame Seeds": 220,
    "Poppy Seeds": 230,
    "Almond Butter": 24,
    "Cashew Butter": 12,
    "Peanut Butter": 45,
    "Coconut Butter": 56,
    "Hazelnut Butter": 98,
    "Pecan Butter": 99,
    "Walnut Butter": 100,
    "Macadamia Butter": 23,
    "Pistachio Butter": 78,
    "Seed Butter": 20,
    "Honey bee basket": 48,
    "Maple Syrup": 38,
    "Agave Syrup": 56,
    "Turmeric Powder": 69,
    "Cumin Seeds": 178,
    "Coriander Powder": 128,
    "Bay Leaves": 98,
    "Fennel Seeds": 68,
    "Mustard Seeds": 48,
    "Asafoetida": 69,
    "Cardamom Pods": 78,
    "Cinnamon Sticks": 99,
    "Cloves": 205,
    "Nutmeg": 45,
    "Dried Thyme": 34,
    "Dried Basil": 78,
    "Dried Oregano": 90,
    "Dried Parsley": 39,
    "Dried Rosemary": 49,
    "Dried Sage": 78,
    "Dried Mint": 37,
    "Ground Ginger": 47,
    "Cayenne Pepper": 65,
    "Paprika": 97,
    "Chili Powder": 98,
    "Black Peppercorns": 78,
    "White Peppercorns": 65,
    "Whole Allspice": 43,
    "Fenugreek Seeds": 34,
    "Saffron Threads": 59,
    "Curry Leaves": 24,
    "Sumac": 34,
    "Ground Turmeric": 89,
}
with open("products.pkl", "wb") as f:
    pickle.dump(products, f)


"""products = products = {
    "a3001": ["Hand Wash", 30],
    "a3002": ["Bar Soap", 100],
    "a3003": ["Hand Sanitizer", 20],
    "a3004": ["Floor Cleaner", 200],
    "a3005": ["Disinfectant", 150],
    "a3006": ["Shampoo", 75],
    "a3007": ["Conditioner", 85],
    "a3008": ["Washing Powder", 120],
    "a3009": ["Liquid Soap", 35],
    "a3010": ["Body Wash", 60],
    "a3011": ["Dish Soap Bar", 10],
    "a3012": ["Detergent Bar", 45],
    "a3013": ["Detergent", 10],
    "a3014": ["Toilet Cleaner", 75],
    "a3015": ["Tissue Paper", 40],
    "a3016": ["Cotton Swabs", 20],
    "a3017": ["Sanitary Napkins", 50],
    "a3018": ["Diapers", 100],
    "a3019": ["Deodorants", 25],
    "a3020": ["Talcum Powder", 20],
    "a3021": ["Toothpaste", 20],
    "a3022": ["Toothbrush", 30],
    "a3023": ["Mouthwash", 60],
    "a3024": ["Air Freshener", 150],
    "a3025": ["Glass Cleaner", 120],
    "a3026": ["Fabric Softener", 70],
    "a3027": ["Refill", 60],
    "a3028": ["Naphthalene Balls", 20],
    "a3029": ["Mosquito Repellent", 45],
    "a3030": ["Nail Polish Remover", 50],
    "a3031": ["Body Lotion", 65],
    "a3032": ["Petroleum Jelly", 25],
    "a3033": ["Face-wash", 20],
    "a3034": ["Nail Polish", 40],
    "a3035": ["Eyeliner", 35],
    "b3001": ["Door Mat", 50],
    "b3002": ["Single Bedsheet", 150],
    "b3003": ["Double Bedsheet", 300],
    "b3004": ["Kitchen Towels", 65],
    "b3005": ["Handkerchief", 50],
    "b3006": ["Womens T-shirt", 120],
    "b3007": ["Mens T-shirt", 140],
    "b3008": ["Watch", 220],
    "b3009": ["Yarn", 75],
    "b3010": ["Sewing Kit", 85],
    "b3011": ["Throw Pillow", 99],
    "c3001": ["Notebook", 50],
    "c3002": ["Planner", 180],
    "c3003": ["Gel Pen", 10],
    "c3004": ["Ball Pen", 5],
    "c3005": ["Pencil", 50],
    "c3006": ["Eraser", 5],
    "c3007": ["Sharpener", 5],
    "c3008": ["Ruler", 10],
    "c3009": ["Sketch Pens", 25],
    "c3010": ["Colour Pencil", 95],
    "c3011": ["Diary", 120],
    "c3012": ["Paint Brushes", 75],
    "c3013": ["Watercolour", 120],
    "c3014": ["Acrylic Paint", 100],
    "c3015": ["Palette", 25],
    "c3016": ["Glitter", 10],
    "c3017": ["Colour Paper", 3],
    "c3018": ["Chart Paper", 15],
    "c3019": ["Folder", 10],
    "c3020": ["Pencil Pouch", 65],
    "c3021": ["Metal Ruler", 30],
    "c3022": ["Geometry Box", 110],
    "c3023": ["Drawing Book", 40],
    "c3024": ["Glue", 40],
    "c3025": ["Clip Board", 30],
    "d3001": ["Potato Chips", 35],
    "d3002": ["Banana Chips", 35],
    "d3003": ["Biscuit", 10],
    "d3004": ["Wafers", 25],
    "d3005": ["Toast", 40],
    "d3006": ["Instant Noodles", 10],
    "d3007": ["Chocolate Box", 80],
    "d3008": ["Chocolate Bar", 25],
    "d3009": ["Popcorn", 20],
    "d3010": ["Cheese", 40],
    "d3011": ["Chikki", 5],
    "d3012": ["Wheat Flour(Atta)", 40],
    "d3013": ["Refined Flour(Atta)", 55],
    "d3014": ["Rice", 10],
    "d3015": ["Channa Dal", 80],
    "d3016": ["Urad Dal", 85],
    "d3017": ["Sugar", 50],
    "d3018": ["Tea Powder", 75],
    "d3019": ["Coffee Powder", 70],
    "d3020": ["Milk", 20],
    "d3021": ["Ketchup", 45],
    "d3022": ["Soy Sauce", 50],
    "d3023": ["Mayonnaise", 35],
    "d3024": ["Red Chilli Sauce", 35],
    "d3025": ["Green Chilli Sauce", 35],
    "d3026": ["Masala", 50],
    "d3027": ["Butter", 25],
    "d3028": ["Paneer", 75],
    "d3029": ["Ice Cream", 110],
    "d3030": ["Salt", 55],
    "e3001": ["Bread", 60],
    "e3002": ["Eggs", 70],
    "e3003": ["Apples", 75],
    "e3004": ["Tomatoes", 80],
    "e3005": ["Soy Milk", 90],
    "e3006": ["Yogurt", 100],
    "e3007": ["Cheese slices", 120],
    "e3008": ["Cereal", 130],
    "e3009": ["Pasta", 125],
    "e3010": ["Rice noodles", 127],
    "e3011": ["Olive oil", 45],
    "e3012": ["Cooking oil", 34],
    "e3013": ["Vinegar", 79],
    "e3014": ["Black", 90],
    "e3015": ["Tuna", 56],
    "e3016": ["Frozen vegetables", 57],
    "e3017": ["Frozen fruits", 89],
    "e3018": ["Frozen meals or entrees", 90],
    "e3019": ["Jam", 99],
    "e3020": ["Honey", 89],
    "e3021": ["Cereal bars", 14],
    "e3022": ["Canned soup", 45],
    "e3023": ["Peanuts", 78],
    "e3024": ["Dried fruits", 89],
    "e3025": ["Granulated sugar", 89],
    "e3026": ["Brown sugar", 78],
    "e3027": ["Wheat", 98],
    "e3028": ["Baking powder", 34],
    "e3029": ["Baking soda", 67],
    "e3030": ["Oats", 45],
    "f3001": ["Almonds", 55],
    "f3002": ["Cashews", 22],
    "f3003": ["Pistachios", 33],
    "f3004": ["Walnuts", 44],
    "f3005": ["Hazelnuts", 55],
    "f3006": ["Sunflower seeds", 66],
    "f3007": ["Pumpkin seeds", 77],
    "f3008": ["Chia seeds", 88],
    "f3009": ["Flaxseeds", 55],
    "f3010": ["Quinoa", 123],
    "f3011": ["Couscous", 45],
    "f3012": ["Barley", 67],
    "f3013": ["Millet", 340],
    "f3014": ["Buckwheat", 78],
    "f3015": ["Farro", 99],
    "f3016": ["Tofu", 89],
    "f3017": ["Tempeh", 110],
    "f3018": ["Seitan", 123],
    "f3019": ["Soy sauce", 90],
    "f3020": ["Fish sauce", 78],
    "f3021": ["Oyster sauce", 65],
    "f3022": ["Hoisin sauce", 56],
    "f3023": ["Worcestershire sauce", 45],
    "f3024": ["Sesame oil", 250],
    "f3025": ["Coconut milk", 245],
    "f3026": ["Almond butter", 600],
    "f3027": ["Cashew butter", 120],
    "f3028": ["Peanut oil", 120],
    "f3029": ["Avocado oil", 560],
    "f3030": ["Grapeseed oil", 400],
    "g3001": ["Flaxseed oil", 240],
    "g3002": ["Safflower oil", 370],
    "g3003": ["Sunflower oil", 90],
    "g3004": ["Hazelnut oil", 123],
    "g3005": ["Pumpkin seed oil", 134],
    "g3006": ["Chia seed oil", 213],
    "g3007": ["Coconut oil", 124],
    "g3008": ["Canola oil", 322],
    "g3009": ["Sesame seeds", 156],
    "g3010": ["Poppy seeds", 180],
    "g3011": ["Hemp seeds", 123],
    "g3012": ["Sesame tahini", 200],
    "g3013": ["Date syrup", 128],
    "g3014": ["Molasses", 130],
    "g3015": ["Agave nectar", 198],
    "g3016": ["Coconut sugar", 189],
    "g3017": ["Maple sugar", 85],
    "g3018": ["Palm sugar", 56],
    "g3019": ["Barbecue sauce", 89],
    "g3020": ["Hot sauce", 187],
    "g3021": ["Teriyaki sauce", 132],
    "g3022": ["Sriracha sauce", 230],
    "g3023": ["Tahini", 230],
    "g3024": ["Pesto sauce", 120],
    "g3025": ["Salsa", 230],
    "g3026": ["Hummus", 30],
    "g3027": ["Guacamole", 288],
    "g3028": ["Tzatziki", 100],
    "g3029": ["Aioli", 78],
    "g3030": ["Marinara sauce", 89],
    "h3001": ["Lemons", 120],
    "h3002": ["Spinach", 456],
    "h3003": ["Broccoli", 45],
    "h3004": ["Cauliflower", 56],
    "h3005": ["Bell peppers", 67],
    "h3006": ["Avocados", 87],
    "h3007": ["Cucumbers", 79],
    "h3008": ["Carrots", 98],
    "h3009": ["Onions", 90],
    "h3010": ["Garlic", 76],
    "h3011": ["Celery", 45],
    "h3012": ["Zucchini", 76],
    "h3013": ["Mushrooms", 120],
    "h3014": ["Green beans", 110],
    "h3015": ["Asparagus", 123],
    "h3016": ["Brussels sprouts", 112],
    "h3017": ["Kale", 120],
    "h3018": ["Radishes", 34],
    "h3019": ["Artichokes", 234],
    "h3020": ["Eggplant", 145],
    "h3021": ["Beets", 130],
    "h3022": ["Sweet potatoes", 160],
    "h3023": ["Potatoes", 140],
    "h3024": ["Oranges", 150],
    "h3025": ["Grapefruits", 160],
    "h3026": ["Berries", 190],
    "h3027": ["Kiwis", 180],
    "h3028": ["Mangoes", 123],
    "h3029": ["Pineapples", 112],
    "h3030": ["Papayas", 123],
    "i3001": ["Lemongrass", 340],
    "i3002": ["Starfruit", 200],
    "i3003": ["Passionfruit", 190],
    "i3004": ["Dragonfruit", 180],
    "i3005": ["Guava", 300],
    "i3006": ["Lychee", 90],
    "i3007": ["Plantains", 100],
    "i3008": ["Ugli fruit", 120],
    "i3009": ["Mango", 140],
    "i3010": ["Kiwi", 150],
    "i3011": ["Persimmon", 123],
    "i3012": ["Pomegranate", 127],
    "i3013": ["Jackfruit", 136],
    "i3014": ["Durian", 178],
    "i3015": ["Rambutan", 177],
    "i3016": ["Longan", 180],
    "i3017": ["Tamarillo", 120],
    "i3018": ["Ackee", 78],
    "i3019": ["Breadfruit", 200],
    "i3020": ["Mulberry", 210],
    "i3021": ["Loganberry", 345],
    "i3022": ["Boysenberry", 230],
    "i3023": ["Elderberry", 67],
    "i3024": ["Gooseberry", 89],
    "i3025": ["Lingonberry", 89],
    "i3026": ["Cloudberry", 98],
    "i3027": ["Cranberry", 56],
    "i3028": ["Bilberry", 129],
    "i3029": ["Saskatoon berry", 139],
    "i3030": ["Marionberry", 179],
    "j3001": ["Artichoke Hearts", 189],
    "j3002": ["Capers", 199],
    "j3003": ["Sun-Dried Tomatoes", 200],
    "j3004": ["Marinated Mushrooms", 159],
    "j3005": ["Roasted Red Peppers", 123],
    "j3006": ["Canned Corn", 56],
    "j3007": ["Dried Lentils", 89],
    "j3008": ["Couscous", 248],
    "j3009": ["Bulgur", 89],
    "j3010": ["Quinoa", 400],
    "j3011": ["Chia Seeds", 68],
    "j3012": ["Flaxseeds", 140],
    "j3013": ["Pumpkin Seeds", 390],
    "j3014": ["Sunflower Seeds", 210],
    "j3015": ["Sesame Seeds", 220],
    "j3016": ["Poppy Seeds", 230],
    "j3017": ["Tahini", 76],
    "j3018": ["Almond Butter", 24],
    "j3019": ["Cashew Butter", 12],
    "j3020": ["Peanut Butter", 45],
    "j3021": ["Coconut Butter", 56],
    "j3022": ["Hazelnut Butter", 98],
    "j3023": ["Pecan Butter", 99],
    "j3024": ["Walnut Butter", 100],
    "j3025": ["Macadamia Butter", 23],
    "j3026": ["Pistachio Butter", 78],
    "j3027": ["Seed Butter", 20],
    "j3028": ["Honey bee basket", 48],
    "j3029": ["Maple Syrup", 38],
    "j3030": ["Agave Syrup", 56],
    "k3001": ["Turmeric Powder", 69],
    "k3002": ["Cumin Seeds", 178],
    "k3003": ["Coriander Powder", 128],
    "k3004": ["Bay Leaves", 98],
    "k3005": ["Fennel Seeds", 68],
    "k3006": ["Mustard Seeds", 48],
    "k3007": ["Asafoetida", 69],
    "k3008": ["Cardamom Pods", 78],
    "k3009": ["Cinnamon Sticks", 99],
    "k3010": ["Cloves", 205],
    "k3011": ["Nutmeg", 45],
    "k3012": ["Dried Thyme", 34],
    "k3013": ["Dried Basil", 78],
    "k3014": ["Dried Oregano", 90],
    "k3015": ["Dried Parsley", 39],
    "k3016": ["Dried Rosemary", 49],
    "k3017": ["Dried Sage", 78],
    "k3018": ["Dried Mint", 37],
    "k3019": ["Ground Ginger", 47],
    "k3020": ["Cayenne Pepper", 65],
    "k3021": ["Paprika", 97],
    "k3022": ["Chili Powder", 98],
    "k3023": ["Black Peppercorns", 78],
    "k3024": ["White Peppercorns", 65],
    "k3025": ["Whole Allspice", 43],
    "k3026": ["Fenugreek Seeds", 34],
    "k3027": ["Saffron Threads", 59],
    "k3028": ["Curry Leaves", 24],
    "k3029": ["Sumac", 34],
    "k3030": ["Ground Turmeric", 89],
}"""
