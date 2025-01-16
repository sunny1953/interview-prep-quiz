class Question:
    def __init__(self, content, options, correct_answer, difficulty, topic):
        self.content = content
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty  # easy, medium, hard
        self.topic = topic
        self.times_asked = 0
        self.times_correct = 0

    def __str__(self):
        return f"Question: {self.content}"
