"""
--------------------------
Test Elements:
test the Food class and Snake class,
including add_body, build_snake, enlarge, move, up, down, left, right, reset, replenish_food
--------------------------
STUDENT: Jinjing Zhang
SEMESTER: Spring 2023
"""
import unittest
from elements import Snake, Food


class TestSnake(unittest.TestCase):
    """test the class Snake, including add_body, build_snake, enlarge, move, up, down, left, right, reset method """
    def setUp(self):
        """use the class Snake"""
        self.snake = Snake()

    def test_add_body(self):
        """
        test the add_body method, starting_points = [(20, 0), (0, 0), (-20, 0)], default size 20 * 20,
        one more body point could be at point (40, 0).
        Should receive original length + 1 as the new length of the snake body.
        """
        original_len = len(self.snake.snake_body)
        self.snake.add_body((40, 0))
        new_len = len(self.snake.snake_body)
        self.assertEqual(new_len, original_len + 1)

    def test_build_snake(self):
        """test the build_snake method. should receive 3"""
        self.assertEqual(len(self.snake.snake_body), 3)

    def test_enlarge(self):
        """test the enlarge method. should receive original length + 1"""
        original_len = len(self.snake.snake_body)
        self.snake.enlarge()
        new_len = len(self.snake.snake_body)
        self.assertEqual(new_len, original_len + 1)

    def test_move(self):
        """test the move method. starting_position should not equal to new_position"""
        starting_position = self.snake.snake_body[0].position()
        self.snake.move()
        new_position = self.snake.snake_body[0].position()
        self.assertNotEqual(starting_position, new_position)

    def test_up(self):
        """test up method. up - 90 degree"""
        self.snake.up()
        self.assertEqual(self.snake.snake_body[0].heading(), 90)

    def test_down(self):
        """test down method. down - 270 degree"""
        self.snake.down()
        self.assertEqual(self.snake.snake_body[0].heading(), 270)

    def test_left(self):
        """
        test left method. left - 180 degree.
        here consider the edge case: cannot turn opposite direction
        should get 0 instead of 180.
        """
        self.snake.left()
        self.assertEqual(self.snake.snake_body[0].heading(), 0)

    def test_right(self):
        """test right method. right - 0 degree"""
        self.snake.right()
        self.assertEqual(self.snake.snake_body[0].heading(), 0)

    def test_reset(self):
        """test reset method. snake_body length should be 3"""
        self.snake.reset()
        self.assertEqual(len(self.snake.snake_body), 3)


class TestFood(unittest.TestCase):
    """test the class Food, including replenish_food"""
    def setUp(self):
        """use the class Food"""
        self.food = Food()

    def test_replenish_food(self):
        """test the replenish_food. The original+point should not be equal to the new_point."""
        original_point = self.food.position()
        self.food.replenish_food()
        new_point = self.food.position()
        self.assertNotEqual(original_point, new_point)


if __name__ == '__main__':
    unittest.main()
