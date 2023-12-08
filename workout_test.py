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
from fitness_diet_tracker.workout_plan import workout

class TestWorkout(unittest.TestCase):
    def setUp(self): # Setting up for the test
        self.athlete_workout_fifteen = workout.WorkOut(15, "athlete") # shortest plan
        self.athlete_workout_thirtyfive = workout.WorkOut(35, "athlete") # regular plan
        self.athlete_workout_sixty = workout.WorkOut(60, "athlete") #longest plan
        self.athlete_workout_sixty_two = workout.WorkOut(62, "athlete") # over the duration limit
        self.athlete_workout_negative = workout.WorkOut(-5, "athlete") # under the duration limit
        
        self.powerlifting_workout_fifteen = workout.WorkOut(15, "strength")
        self.powerlifting_workout_thirtyfive = workout.WorkOut(35, "strength")
        self.powerlifting_workout_sixty = workout.WorkOut(60, "strength")
        self.powerlifting_workout_sixty_two = workout.WorkOut(62, "strength")
        self.powerlifting_workout_negative = workout.WorkOut(-5, "strength")
        
        self.calisthenics_workout_fifteen = workout.WorkOut(15, "body weight")
        self.calisthenics_workout_thirtyfive = workout.WorkOut(35, "body weight")
        self.calisthenics_workout_sixty = workout.WorkOut(60, "body weight")
        self.calisthenics_workout_sixty_two = workout.WorkOut(62, "body weight")
        self.calisthenics_workout_negative = workout.WorkOut(-5, "body weight")
        
        self.youtube_invalid_workout = workout.WorkOut(32, "invalid")
        self.youtube_athlete = workout.WorkOut(32, "athlete")
        self.youtube_powerlifting = workout.WorkOut(52, "strength")
        self.youtube_calisthenics = workout.WorkOut(23, "body weight")
    
    @classmethod
    def setUpClass(cls):
        print("This is the setupclass")
    
    @classmethod
    def tearDownClass(cls):
        print("This is the teardown class")
    
    def tearDown(self):
        print("Teardown method for the Warmup Test class")
    
    def test_generate_intensity_plan(self):
        self.assertEqual(self.athlete_workout_fifteen.generate_intensity_plan(), '3 sets of push press until failure\n3 sets of half squat jumps until failure\n3 sets of pull ups until failure\nAtleast 1 minute of rest between each set is recommended')
        self.assertEqual(self.athlete_workout_thirtyfive.generate_intensity_plan(), '4 sets of push press until failure\n4 sets of half squat jumps until failure\n4 sets of pull ups until failure\nAtleast 1.5 minute of rest between each set is recommended')
        self.assertEqual(self.athlete_workout_sixty.generate_intensity_plan(), '5 sets of push press until failure\n5 sets of half squat jumps until failure\n5 sets of pull ups until failure\nAtleast 1.5 minute of rest between each set is recommended')
        self.assertEqual(self.athlete_workout_sixty_two.generate_intensity_plan(), None)
        self.assertEqual(self.athlete_workout_negative.generate_intensity_plan(), None)
    
    def test_generate_powerlifting_plan(self):
        self.assertEqual(self.powerlifting_workout_fifteen.generate_powerlifting_plan(), '2 sets of bench press until failure\n2 sets of barbell squats until failure\n2 sets of deadlifts until failure\nAtleast 2 minute of rest between each set is recommended')
        self.assertEqual(self.powerlifting_workout_thirtyfive.generate_powerlifting_plan(), '3 sets of bench press until failure\n3 sets of barbell squats until failure\n3 sets of deadlifts until failure\nAtleast 2 minute of rest between each set is recommended')
        self.assertEqual(self.powerlifting_workout_sixty.generate_powerlifting_plan(), '4 sets of bench press until failure\n4 sets of barbell squats until failure\n4 sets of deadlifts until failure\nAtleast 2.5 minute of rest between each set is recommended')
        self.assertEqual(self.powerlifting_workout_sixty_two.generate_powerlifting_plan(), None)
        self.assertEqual(self.powerlifting_workout_negative.generate_powerlifting_plan(), None)
    
    def test_generate_calisthenics_plan(self):
        self.assertEqual(self.calisthenics_workout_fifteen.generate_calisthenics_plan(), '3 sets of push ups until failure\n3 sets of pistol squats until failure\n3 sets of pull ups until failure\nAtleast 1 minute of rest between each set is recommended')
        self.assertEqual(self.calisthenics_workout_thirtyfive.generate_calisthenics_plan(), '4 sets of push ups until failure\n4 sets of pistol squats until failure\n4 sets of pull ups until failure\nAtleast 1.5 minute of rest between each set is recommended')
        self.assertEqual(self.calisthenics_workout_sixty.generate_calisthenics_plan(), '5 sets of push ups until failure\n5 sets of pistol squats until failure\n5 sets of pull ups until failure\nAtleast 1.5 minute of rest between each set is recommended')
        self.assertEqual(self.calisthenics_workout_sixty_two.generate_calisthenics_plan(), None)
        self.assertEqual(self.calisthenics_workout_negative.generate_calisthenics_plan(), None)
    
    def test_youtube_links(self):
        self.assertEqual(self.youtube_invalid_workout.youtube_links(), None)
        push_press = "https://www.youtube.com/watch?v=iaBVSJm78ko"
        squat_jumps = "https://www.youtube.com/watch?v=YGGq0AE5Uyc"
        pull_ups = "https://www.youtube.com/watch?v=XB_7En-zf_M"
        self.assertEqual(self.youtube_athlete.youtube_links(), f'{push_press}\n{squat_jumps}\n{pull_ups}')
        bench_press = "https://www.youtube.com/shorts/EdDqD4aKwxM"
        barbell_squats = "https://www.youtube.com/shorts/gslEzVggur8"
        deadlifts = "https://www.youtube.com/shorts/McCDaAsSeRc"
        self.assertEqual(self.youtube_powerlifting.youtube_links(), f'{bench_press}\n{barbell_squats}\n{deadlifts}')
        push_ups = "https://www.youtube.com/watch?v=IODxDxX7oi4"
        pistol_squats = "https://www.youtube.com/shorts/5R3wjhmjhgU"
        pull_ups = "https://www.youtube.com/watch?v=XB_7En-zf_M"
        self.assertEqual(self.youtube_calisthenics.youtube_links(), f'{push_ups}\n{pistol_squats}\n{pull_ups}')
    
    
       
unittest.main(argv =[''], verbosity=2, exit=False)