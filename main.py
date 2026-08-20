import json


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

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["question"],
            data["choices"],
            data["answer"]
        )


class QuizGame:
    def __init__(self):
        self.state_file = "state.json"
        self.quizzes = []
        self.best_score = None
        self.load_data()

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
                raise

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
                raise   

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

            if quiz.check_answer(user_answer):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")

        score = int((correct_count / total_count) * 100)

        print("\n========================================")
        print(f"🏆 결과: {total_count}문제 중 {correct_count}문제 정답! ({score}점)")

        if self.best_score is None:
            self.best_score = score
            self.save_data()
            print("🎉 첫 번째 점수가 최고 점수로 저장되었습니다!")
        elif score > self.best_score:
            self.best_score = score
            self.save_data()
            print("🎉 새로운 최고 점수입니다!")
        else:
            print(f"📌 현재 최고 점수는 {self.best_score}점입니다.")

        print("========================================")

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")

        question = self.get_non_empty_input("문제를 입력하세요: ")

        choices = []
        for i in range(1, 5):
            choice = self.get_non_empty_input(f"선택지 {i}: ")
            choices.append(choice)

        answer = self.get_answer_input()

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_data()

        print("✅ 퀴즈가 추가되었습니다!")

    def list_quizzes(self):
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("----------------------------------------")

        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")

        print("----------------------------------------")

    def show_best_score(self):
        if self.best_score is None:
            print("\n📌 아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"\n🏆 현재 최고 점수: {self.best_score}점")

    def load_data(self):
        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.quizzes, self.best_score = self.validate_loaded_data(data)
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개)")

        except FileNotFoundError:
            print("📂 저장 파일이 없습니다. 기본 퀴즈 데이터를 사용합니다.")
            self.quizzes = self.create_default_quizzes()
            self.best_score = None

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("⚠️ 저장 파일이 손상되었거나 형식이 올바르지 않습니다. 기본 퀴즈 데이터로 복구합니다.")
            self.quizzes = self.create_default_quizzes()
            self.best_score = None
            self.save_data()

        except OSError:
            print("⚠️ 파일을 읽는 중 오류가 발생했습니다. 기본 퀴즈 데이터를 사용합니다.")
            self.quizzes = self.create_default_quizzes()
            self.best_score = None

    def save_data(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }

        try:
            with open(self.state_file, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except OSError:
            print("⚠️ 데이터를 저장하는 중 오류가 발생했습니다.")

    def run(self):
        try:
            while True:
                self.show_menu()
                choice = self.get_menu_choice()

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

        except (KeyboardInterrupt, EOFError):
            print("\n⚠️ 입력이 중단되었습니다. 저장 후 안전하게 종료합니다.")

        finally:
            self.save_data()

    def get_non_empty_input(self, prompt):
        while True:
            try:
                user_input = input(prompt).strip()

                if user_input == "":
                    print("⚠️ 빈 입력입니다. 다시 입력하세요.")
                    continue

                return user_input

            except (KeyboardInterrupt, EOFError):
                raise

    def validate_loaded_data(self, data):
        if not isinstance(data, dict):
            raise TypeError("저장 데이터는 딕셔너리여야 합니다.")

        if "quizzes" not in data:
            raise KeyError("quizzes 키가 없습니다.")

        quiz_data_list = data["quizzes"]
        if not isinstance(quiz_data_list, list):
            raise TypeError("quizzes는 리스트여야 합니다.")

        quizzes = [Quiz.from_dict(quiz_data) for quiz_data in quiz_data_list]

        best_score = data.get("best_score", None)
        if best_score is not None:
            if not isinstance(best_score, int):
                raise TypeError("best_score는 정수 또는 None이어야 합니다.")
            if not (0 <= best_score <= 100):
                raise ValueError("best_score는 0~100 사이여야 합니다.")

        return quizzes, best_score

def main():
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()