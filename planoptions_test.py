import unittest
from fitness_diet_tracker.diet_package import planoptions

class TestPlanOptions(unittest.TestCase):    
    @classmethod
    def setUpClass(cls):
        # Shared setup for the entire test class
        print("Setting up resources for TestDietOptions class")

    @classmethod
    def tearDownClass(cls):
        # Shared teardown for the entire test class
        print("Tearing down resources for TestDietOptions class")
        
    def setUp(self):
        self.plan1 = planoptions.PlanOptions(176, 69, 23, "male", "high", "gain")
        self.plan2 = planoptions.PlanOptions(175, 70, 30, "male", "invalid", "loss")#simulate when user inputs invalid activity level
        self.plan3 = planoptions.PlanOptions(175, 70, 30, "invalid", "high", "loss")#simulate when user inputs invalid gender
        self.plan4 = planoptions.PlanOptions(170, 70, 27, "female", "high", "invalid")#simulate when user inputs invalid weight goal
        self.plan5 = planoptions.PlanOptions(150, 54, 40, "female", "moderate", "gain")
        self.plan6 = planoptions.PlanOptions(180, 94, 35, "male", "low", "loss")
    
    def tearDown(self):
        pass
    
    def test_calculate_bmr(self):
        self.assertEqual(self.plan1.calculate_bmr(), 1740.383)
        self.assertEqual(self.plan2.calculate_bmr(), 1701.8449999999998)
        self.assertEqual(self.plan3.calculate_bmr(), None)
        self.assertEqual(self.plan4.calculate_bmr(), 1512.7580000000003)
    
    def test_calculate_tdee(self):
        self.plan1.calculate_bmr()
        self.assertEqual(self.plan1.calculate_tdee(), 3306.7277)
        self.plan2.calculate_bmr()
        self.assertIsNone(self.plan2.calculate_tdee())
        self.plan4.calculate_bmr()
        self.assertEqual(self.plan4.calculate_tdee(), 2874.2402)
        self.plan5.calculate_bmr()
        self.assertEqual(self.plan5.calculate_tdee(), 1956.0411000000001)
    
    def test_calculate_target_cal(self):
        self.plan1.calculate_bmr()
        self.plan1.calculate_tdee()
        self.assertEqual(self.plan1.calculate_target_cal(), 3637.40047)
        self.plan4.calculate_bmr()
        self.plan4.calculate_tdee()
        self.assertIsNone(self.plan4.calculate_target_cal())
        self.plan5.calculate_bmr()
        self.plan5.calculate_tdee()
        self.assertEqual(self.plan5.calculate_target_cal(), 2151.64521)
        self.plan6.calculate_bmr()
        self.plan6.calculate_tdee()
        self.assertEqual(self.plan6.calculate_target_cal(), 2184.9318000000003)


unittest.main(argv =[''], verbosity=2, exit=False)