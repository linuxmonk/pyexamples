from upper import make_it_uppercase, get_first_word_from_sentence
import unittest


class TestGreeting(unittest.TestCase):
    def test_make_it_uppercase(self):
        text = "hello world"
        expected = "HELLO WORLD"
        output = make_it_uppercase(text)
        self.assertEqual(output, expected)

    def test_first_word(self):
        sentence = "A quick brown fox jumped over a lazy dog"
        firstword = get_first_word_from_sentence(sentence)
        self.assertEqual(firstword, "A")


if __name__ == "__main__":
    unittest.main()
