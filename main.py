class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question          # 문제 내용
        self.choices = choices            # 선택지 4개가 들어있는 리스트
        self.answer = answer              # 정답 번호(1~4)

    def display(self):
        print("\n----------------------------------------")
        print(f"문제: {self.question}")
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}. {choice}")

    def check_answer(self, user_answer):
        return user_answer == self.answer

class QuizGame:
    def __init__(self):
        self.quizzes = self.create_default_quizzes()
        self.best_score = 0
        self.state_file = "state.json"

    def create_default_quizzes(self):
        return [
            Quiz(
                "Python의 창시자는 누구인가요?",
                ["Guido van Rossum", "Linus Torvalds", "James Gosling", "Dennis Ritchie"],
                1
            ),
            Quiz(
                "Python에서 리스트에 값을 하나 추가할 때 사용하는 메서드는?",
                ["add()", "append()", "insert()", "push()"],
                2
            ),
            Quiz(
                "다음 중 불리언(bool) 값은 무엇인가요?",
                ["0", "'True'", "True", "1"],
                3
            ),
            Quiz(
                "문자열 'python'의 길이는 얼마인가요?",
                ["5", "6", "7", "8"],
                2
            ),
            Quiz(
                "조건에 따라 다른 코드를 실행할 때 사용하는 문법은?",
                ["for", "while", "if", "def"],
                3
            ),
            Quiz(
                "key와 value 형태로 데이터를 저장하는 자료형은?",
                ["list", "tuple", "dict", "set"],
                3
            ),
        ]

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

    def get_answer_input(self):
        while True:
            try:
                user_input = input("정답 입력 (1~4): ").strip()

                if user_input == "":
                    print("⚠️ 빈 입력입니다. 1~4 사이의 숫자를 입력하세요.")
                    continue

                answer = int(user_input)

                if 1 <= answer <= 4:
                    return answer
                else:
                    print("⚠️ 잘못된 입력입니다. 1~4 사이의 숫자를 입력하세요.")

            except ValueError:
                print("⚠️ 숫자로 입력해야 합니다. 1~4 사이의 숫자를 입력하세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n⚠️ 입력이 중단되었습니다. 퀴즈를 종료하고 메뉴로 돌아갑니다.")
                return None

    def play_quiz(self):
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return

        correct_count = 0
        total_count = len(self.quizzes)

        print(f"\n📝 퀴즈를 시작합니다! (총 {total_count}문제)")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[문제 {index}]")
            quiz.display()

            user_answer = self.get_answer_input()

            if user_answer is None:
                print("📌 퀴즈를 중단하고 메뉴로 돌아갑니다.")
                return

            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")

        score = int((correct_count / total_count) * 100)

        print("\n========================================")
        print(f"🏆 결과: {total_count}문제 중 {correct_count}문제 정답! ({score}점)")
        print("========================================")

    def add_quiz(self):
        print("📌 퀴즈 추가 기능은 아직 구현 전입니다.")

    def list_quizzes(self):
        print("\n📋 현재 등록된 퀴즈 목록")
        print("----------------------------------------")
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"{index}. {quiz.question}")

    def show_best_score(self):
        print(f"🏆 현재 최고 점수: {self.best_score}")

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