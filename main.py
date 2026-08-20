class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self):
        pass

    def check_answer(self, user_answer):
        pass


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.state_file = "state.json"

    def show_menu(self):
        pass

    def play_quiz(self):
        pass

    def add_quiz(self):
        pass

    def list_quizzes(self):
        pass

    def show_best_score(self):
        pass

    def load_data(self):
        pass

    def save_data(self):
        pass

    def run(self):
        print("퀴즈 게임 구조가 준비되었습니다.")


def main():
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()