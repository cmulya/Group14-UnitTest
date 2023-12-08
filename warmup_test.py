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
        
        self.youtube_invalid_warmup = warmup.warmUp("invalid")
        self.youtube_athlete_warmup = warmup.warmUp("athlete")
        self.youtube_strength_warmup = warmup.warmUp("strength")
        self.youtube_body_weight_warmup = warmup.warmUp("body weight")
        
    
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

    def test_youtube_links_warmup(self):
        self.assertEqual(self.youtube_invalid_warmup.youtube_links_warmup(), None)
        
        seated_hamstring_stretch = "https://www.youtube.com/watch?v=HFPbNaMzW3M"
        across_body_arm_stretch = "https://www.youtube.com/watch?v=-1K0m5ywRcY"
        self.assertEqual(self.youtube_athlete_warmup.youtube_links_warmup(), f'{seated_hamstring_stretch}\n{across_body_arm_stretch}')
        
        overhead_tricep_stretch = "https://www.youtube.com/watch?v=Uvk1Y8O1_yM"
        standing_hamstring_stretch = "https://www.youtube.com/watch?v=LVY692zJK0A"
        supine_twist_back_stretch = "https://www.youtube.com/watch?v=mNdJti7ZwKI"
        self.assertEqual(self.youtube_strength_warmup.youtube_links_warmup(), f'{overhead_tricep_stretch}\n{standing_hamstring_stretch}\n{supine_twist_back_stretch}')
        
        cobra_stretch = "https://www.youtube.com/watch?v=JDcdhTuycOI"
        bent_arm_wall_stretch = "https://www.youtube.com/watch?v=3MuMu3Q4r68"
        standing_quadriceps_stretch = "https://www.youtube.com/watch?v=g4v_QK893eI"
        self.assertEqual(self.youtube_body_weight_warmup.youtube_links_warmup(), f'{cobra_stretch}\n{bent_arm_wall_stretch}\n{standing_quadriceps_stretch}')
        

unittest.main(argv =[''], verbosity=2, exit=False)