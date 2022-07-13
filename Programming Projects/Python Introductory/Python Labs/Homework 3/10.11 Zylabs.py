# Andy Luong 1525166
# Zylabs 10.11

class FoodItem:
    def __init__(self, name=None, fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__  == "__main__":

    Food1 = FoodItem()
    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())
    num_servings = float(input())

    Food1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,Food1.get_calories(num_servings)))

    print()

    Food2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
    Food2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, Food2.get_calories(num_servings)))
