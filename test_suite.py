import unittest
from warmup_test import TestWarmup
from workout_test import TestWorkout
from planoptions_test import TestPlanOptions
from dietoptions_test import TestDietOptions


def my_suite():
    # workout plan
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(TestWarmup('setUpClass'))
    suite.addTest(TestWarmup('tearDownClass'))
    suite.addTest(TestWarmup('setUp'))
    suite.addTest(TestWarmup('tearDown'))
    suite.addTest(TestWarmup('test_athlete_warmup'))
    suite.addTest(TestWarmup('test_strength_warmup'))
    suite.addTest(TestWarmup('test_bodyweight_warmup'))
    suite.addTest(TestWarmup('test_youtube_links_warmup'))
    suite.addTest(TestWorkout('setUpClass'))
    suite.addTest(TestWorkout('tearDownClass'))
    suite.addTest(TestWorkout('setUp'))
    suite.addTest(TestWorkout('tearDown'))
    suite.addTest(TestWorkout('test_generate_intensity_plan'))
    suite.addTest(TestWorkout('test_generate_powerlifting_plan'))
    suite.addTest(TestWorkout('test_generate_calisthenics_plan'))
    suite.addTest(TestWorkout('test_youtube_links'))

    # Diet plan
    suite.addTest(TestPlanOptions('setUpClass'))
    suite.addTest(TestPlanOptions('tearDownClass'))
    suite.addTest(TestPlanOptions('setUp'))
    suite.addTest(TestPlanOptions('tearDown'))
    suite.addTest(TestPlanOptions('test_calculate_bmr'))
    suite.addTest(TestPlanOptions('test_calculate_tdee'))
    suite.addTest(TestPlanOptions('test_calculate_target_cal'))
    suite.addTest(TestDietOptions('setUpClass'))
    suite.addTest(TestDietOptions('tearDownClass'))
    suite.addTest(TestDietOptions('setUp'))
    suite.addTest(TestDietOptions('tearDown'))
    suite.addTest(TestDietOptions('test_generate_vegan_meal'))
    suite.addTest(TestDietOptions('test_generate_vegetarian_meal'))
    suite.addTest(TestDietOptions('test_generate_meat_meal'))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    
my_suite()