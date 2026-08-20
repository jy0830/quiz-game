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
        print("\n========================================")
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def get_menu_choice(self):
        while True:
            try:
                user_input = input("선택: ").strip()

                if user_input == "":
                    print("⚠️ 빈 입력입니다. 1~5 사이의 숫자를 입력하세요.")
                    continue

                choice = int(user_input)

                if 1 <= choice <= 5:
                    return choice
                else:
                    print("⚠️ 잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")

            except ValueError:
                print("⚠️ 숫자로 입력해야 합니다. 1~5 사이의 숫자를 입력하세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n⚠️ 입력이 중단되었습니다. 프로그램을 안전하게 종료합니다.")
                return None

    def play_quiz(self):
        print("📝 퀴즈 풀기 기능은 아직 구현 전입니다.")

    def add_quiz(self):
        print("📌 퀴즈 추가 기능은 아직 구현 전입니다.")

    def list_quizzes(self):
        print("📋 퀴즈 목록 기능은 아직 구현 전입니다.")

    def show_best_score(self):
        print("🏆 점수 확인 기능은 아직 구현 전입니다.")

    def load_data(self):
        pass

    def save_data(self):
        pass

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_menu_choice()

            if choice is None:
                break

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_best_score()
            elif choice == 5:
                print("👋 게임을 종료합니다.")
                break


def main():
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()