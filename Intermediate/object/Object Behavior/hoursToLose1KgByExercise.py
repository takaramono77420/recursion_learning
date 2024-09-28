import math
def hoursToLose1KgByExercise(typeOfExercise):
    # 関数を完成させてください 
    instance = exercise(typeOfExercise)
    intensiy = instance.intensiy()
    return math.floor ((7700 / (intensiy * 3.5 * 85.5 / 200)) / 60 * 10) / 10

class exercise:
    exercise_name = ""
    def __init__(self, exercise):
        self.exercise_name = exercise

    def intensiy(self):
        if self.exercise_name == "running":
            return 8
        elif self.exercise_name == "walking":
            return 3
        elif self.exercise_name == "tennis":
            return 5
        elif self.exercise_name == "rope jump":
            return 9
        else:
            return 0