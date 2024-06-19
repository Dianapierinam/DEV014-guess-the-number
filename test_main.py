#biblioteca estándar de Python para escribir y ejecutar pruebas.
import unittest
from unittest.mock import patch
#funciones que se están probando
from main import guess_the_number, verify_number

class TestGuessTheNumber(unittest.TestCase):

    #Uso del decorado @patch 

    #la primera vez que se llame a input, devolverá '50', y la segunda vez devolverá '75'
    @patch('main.input', side_effect=['50', '75'])
    #parchea la función random_number en el módulo main
    #return_value=75 indica que cada vez que se llame a random_number durante la prueba, devolverá 75
    @patch('main.random_number', return_value=75)
    #reemplaza la función print con un objeto mock, para la verificación de las llamadas a print
    @patch('builtins.print')
    def test_user_wins(self, mock_print, mock_random, mock_input):
        guess_the_number(input_func=mock_input, random_func=mock_random, print_func=mock_print)
        self.assertEqual(mock_input.call_count, 2) 
        mock_print.assert_any_call("User congratulations, you guessed the number")

    @patch('main.input', side_effect=['50', '25'])
    @patch('main.random_number', return_value=25)
    @patch('builtins.print') 
    def test_user_guesses_correctly_on_second_try(self, mock_print, mock_random, mock_input):
        guess_the_number(input_func=mock_input, random_func=mock_random, print_func=mock_print)
        self.assertEqual(mock_input.call_count, 2) 
        mock_print.assert_any_call("User congratulations, you guessed the number")

    def test_verify_number(self):
        cases = [
            (50, 50, "congratulations", True),
            (50, 75, "User, the number is greater", False),
            (50, 25, "User, the number is less", False),
        ]

        # Itera sobre cada caso de prueba definido en la lista cases
        for user_guess, correct_number, expected_message, is_correct in cases:
            with self.subTest(user_guess=user_guess, correct_number=correct_number):
                #Inicialización de guesses
                guesses = []
                #Llama a la función verify_number con sus argumentos
                result = verify_number("User", user_guess, correct_number, guesses)
                #Verifica que el expected_message esté contenido en result
                self.assertIn(expected_message, result)
                #Verifica que user_guess esté contenido en la lista guesses
                self.assertIn(user_guess, guesses)
                if is_correct:
                    self.assertTrue("congratulations" in result)
                #Si is_correct es False, verifica que "congratulations" no esté en result.
                else:
                    self.assertFalse("congratulations" in result)
#Eejcución de la prueba
if __name__ == '__main__':
    unittest.main()












