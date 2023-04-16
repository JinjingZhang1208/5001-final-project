"""
--------------------------
Test Score Manager:
test save_best_score_to_file function, load_best_score_from_file function
class Score could be tested by playing the game
--------------------------
STUDENT: Jinjing Zhang
SEMESTER: Spring 2023
"""
from score_manager import save_best_score_to_file, load_best_score_from_file


def test_save_and_load_list():
    """
    Test saving and loading a list:
    update the best_score to 1, save it in the file called 'Test List.txt' using save_best_score_to_file.
    use load_best_score_from_file to see if now the best score is updated to 1
    """
    save_best_score_to_file("Test List.txt", 1)
    loaded_best_score = load_best_score_from_file("Test List.txt")
    if loaded_best_score == 1:
        return f'All good with save_best_score_to_file(), load_best_score_from_file()'
    else:
        return f'Error with save_best_score_to_file(), load_best_score_from_file()'


def main():
    result = test_save_and_load_list()
    print(result)


if __name__ == '__main__':
    main()
