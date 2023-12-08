import sys
import os
folder_name = 'fitness_diet_tracker'
## Get the current working directory
current_directory = os.getcwd()
## Join the current directory with the folder name
folder_path = os.path.join(current_directory, folder_name)
sys.path.append(folder_path)

import unittest
from fitness_diet_tracker.workout_plan import warmup

class TestWarmup(unittest.TestCase):
    def setUp(self): # Setting up for the test
        self.athlete = warmup.warmUp("athlete")
        self.strength = warmup.warmUp("strength")
        self.body_weight = warmup.warmUp("body weight")
        self.invalid_input = warmup.warmUp("invalid")
    
    @classmethod
    def setUpClass(cls):
        print("This is the setupclass")
    
    @classmethod
    def tearDownClass(cls):
        print("This is the teardown class")
    
    def tearDown(self):
        print("Teardown method for the Warmup Test class")
    
    def test_athlete_warmup(self):
        self.assertEqual(self.athlete.athlete_warmup(), 'Seated hamstring stretch (2 repetitions)\nLight jogging (5 mins)\nAcross Body arm stretch (2 repetitions)\nPull-up bar hang (1 minute)')
        self.assertIsInstance(self.athlete.athlete_warmup(), str)
        self.assertIsNotNone(self.athlete.athlete_warmup())
        self.assertNotIsInstance(self.athlete.athlete_warmup(), int)
    
    def test_strength_warmup(self):
        self.assertEqual(self.strength.strength_warmup(), 'Overhead Tricep Stretch (2 repetitions)\nStanding hamstring stretch (2 repetitions)\nSupine Twist Back Stretch (2 repetitions)\nLightweight squats/deadlifts/bench press/curls')
        self.assertIsInstance(self.strength.strength_warmup(), str)
        self.assertIsNotNone(self.strength.strength_warmup())
        self.assertNotIsInstance(self.strength.strength_warmup(), int)
    
    def test_bodyweight_warmup(self):
        self.assertEqual(self.body_weight.body_weight_warmup(), 'Cobra Stretch (2 repetitions)\nBent arm wall stretch\nStanding quadriceps stretches (2 repetitions)\nIncline push-ups\nBodyweight squats')
        self.assertIsInstance(self.body_weight.body_weight_warmup(), str)
        self.assertIsNotNone(self.body_weight.body_weight_warmup())
        self.assertNotIsInstance(self.body_weight.body_weight_warmup(), int)

        

unittest.main(argv =[''], verbosity=2, exit=False)