import sys
import os
folder_name = 'fitness_diet_tracker'
## Get the current working directory
current_directory = os.getcwd()
## Join the current directory with the folder name
folder_path = os.path.join(current_directory, folder_name)
sys.path.append(folder_path)

import unittest
from fitness_diet_tracker.diet_package import planoptions
from fitness_diet_tracker.diet_package import dietoptions

class TestDietOptions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Shared setup for the entire test class
        print("Setting up resources for TestDietOptions class")

    @classmethod
    def tearDownClass(cls):
        # Shared teardown for the entire test class
        print("Tearing down resources for TestDietOptions class")
        
    def setUp(self):
        self.d1 = dietoptions.DietOptions(176, 69, 23, "male", "moderate", "gain")
        self.str0 = "miscellaneous"
        self.vegan1 = "tofu"
        self.vegan2 = "soy_curls"
        self.vegan3 = "tempeh"
        self.vegetarian1 = "cranberry_beans"
        self.vegetarian2 = "black_beans"
        self.vegetarian3 = "chickpea"
        self.meat1 = "beef"
        self.meat2 = "chicken"
        self.meat3 = "fish"
        
    def tearDown(self):
        pass
        
    def test_generate_vegan_meal(self):
        self.d1.calculate_bmr()
        self.d1.calculate_tdee()
        self.d1.calculate_target_cal()
        self.assertIsNone(self.d1.generate_vegan_meal(self.vegan1))
        self.assertIsNone(self.d1.generate_vegan_meal(self.vegan2))
        self.assertIsNone(self.d1.generate_vegan_meal(self.vegan3))
        self.assertEqual(self.d1.generate_vegan_meal(self.str0), "Invalid protein option for a vegan diet.")
    
    def test_generate_vegetarian_meal(self):
        self.d1.calculate_bmr()
        self.d1.calculate_tdee()
        self.d1.calculate_target_cal()
        self.assertIsNone(self.d1.generate_vegetarian_meal(self.vegetarian1))
        self.assertIsNone(self.d1.generate_vegetarian_meal(self.vegetarian2))
        self.assertIsNone(self.d1.generate_vegetarian_meal(self.vegetarian3))
        self.assertEqual(self.d1.generate_vegetarian_meal(self.str0), "Invalid protein option for a vegetarian diet.")
        
    def test_generate_meat_meal(self):
        self.d1.calculate_bmr()
        self.d1.calculate_tdee()
        self.d1.calculate_target_cal()
        self.assertIsNone(self.d1.generate_meat_meal(self.meat1))
        self.assertIsNone(self.d1.generate_meat_meal(self.meat2))
        self.assertIsNone(self.d1.generate_meat_meal(self.meat3))
        self.assertEqual(self.d1.generate_meat_meal(self.str0), "Invalid protein option for a meat diet.")

unittest.main(argv =[''], verbosity=2, exit=False)
