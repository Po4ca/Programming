class Pet():
    """
        state только один за раз:
            is_eating
                min max
                + fullness
                - cheerfulness 
                - activity
                прекратить? 
                портрет + лейбл
            is_sleeping
                + cheerfulness
                - fullness (несильно)
                - activity
                разбудить
                max 
                портрет
            
            is_playing
                + activity 
                - fullness (сильно)
                - cheerfulness 
                max
                портрет + лейбл 
                прекратить 

            idle
                - fullness
                - cheerfulness 
                - activity
            
            health
                health = fullness cheerfulness activity
                min - ded 


    """
    def __init__(
        self,
        portrait="",
        name="",
        fullness=100,
        activity=100,
        cheerfulness=100,
        mood=100,
        fullness_change=1,
        activity_change=1,
        cheerfulness_change=1,
        mood_change=1
    ):
        self.portrait = portrait
        self.name = name
        self.fullness = fullness
        self.activity = activity
        self.cheerfulness = cheerfulness
        self.mood = mood
        self.fullness_change = fullness_change
        self.activity_change = activity_change
        self.cheerfulness_change = cheerfulness_change
        self.mood_change = mood_change

    def decrease_stats(self):
        self.fullness -= self.fullness_change
        self.activity -= self.activity_change
        self.cheerfulness -= self.cheerfulness_change
        self.mood -= self.mood_change

    def feed(self, calories):
        self.fullness += calories
        print(f"{self.name} съел {calories} и теперь у него {self.fullness} сытости")

    def play(self, time):
        self.activity += time
        print(f"{self.name} поиграл {time} и теперь у него {self.activity} активности")

    def sleep(self, time):
        self.cheerfulness += time
        print(f"{self.name} поспал {time} и теперь у него {self.cheerfulness} бодрости")
