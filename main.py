import random

#Crear la función random_number
def random_number():
    #Se usa la función randint
    return random.randint(0, 100)

#Se usa la función input para obtener la entrada del usuario
def user_number(input_func=input):
    return int(input_func("Enter a number: "))

#Calcula el número que la computadora adivina, // sirve para asegura que el resultado es entero
def computer_number(low, high):
    return (low + high) // 2

#Si el número adivinado(user) coincide con el target, retorna un mensaje
def verify_number(player, user, target, guesses):
    #guesses es la lista de intentos que se agrega por cada uno de ellos
    guesses.append(user)
    if user == target:
        return f"{player} congratulations, you guessed the number"
    elif user < target:
        return f"{player}, the number is greater"
    else:
        return f"{player}, the number is less"
    

#Generar número aleatorio usando random_func
def guess_the_number(input_func=input, random_func=random_number, print_func=print):
    #Genera un número aleatorio entre 0 y 100
    target_number = random_func()
    #lista vacía para los intentos del usuario
    user_guesses = []
    #lista vacía para los intentos del computador
    computer_guesses = []
    #Inicializa los limites, tanto inferiores como superiores
    low, high = 0, 100
    #Bucle infinito, hasta encontrar el número correcto
    while True:
        #Llama a la funcion user_numer que utiliza a input_fucn para obtener el número del usuario
        user_num = user_number(input_func)
        #Verifica que el número ingresado por el usuario coincide con el target_number
        result = verify_number("User", user_num, target_number, user_guesses)
        #imprime la verificación
        print_func(result)
        #Si adivina correctamente se acaba el juego, se rompe el bucle
        if "congratulations" in result:
            winner = "User"
            break
        #Verifica el rango actual, si low es menor igual a high
        if low <= high:
            #Llama a la función computer_number para que la computadora de un número dentro del rango (low, high)
            computer_num = computer_number(low, high)
            #Imprime el número de la computadora usando print_func
            print_func(f"Computer guess: {computer_num}")
            result = verify_number("Computer", computer_num, target_number, computer_guesses)
            print_func(result)
            if "congratulations" in result:
                winner = "Computer"
                break
            #Si el número de la computadora (computer_num) es menor que el target_number, ajusta low a computer_num + 1
            if computer_num < target_number:
                low = computer_num + 1
            #Si el número de la computadora (computer_num) es mayor que el target_number, ajusta high a computer_num - 1    
            else:
                high = computer_num - 1

    print_func("End of the game")
    if winner == "User":
        print_func("User's guesses: ", user_guesses)
    else:
        print_func("Computer's guesses: ", computer_guesses)

def main():
    while True:
        guess_the_number()
        #Strip para eliminar espacio al princio y final y lowe para convertir a minus. la respuesta del usuario
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break
    print("Thanks for playing")

if __name__ == "__main__":
    main()






