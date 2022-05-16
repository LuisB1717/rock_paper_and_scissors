import random

def game_title(string):

    def game (func):
        print(string)

        def wrapper (*args, **kwargs):
        
            points = [0,0,0] 
            while True: 
                hands = func(*args, **kwargs)            
                
                if len(hands) > 1:
                    for i in range(len(hands)):
                        print ("Jugador " + str(i+1) + " ha sacado: " + hands[i])

                    if hands[1] == "piedra" and hands[0] == "papel" or\
                        hands [1] == "papel" and hands[0] == "tijera" or\
                        hands [1] == "tijera" and hands[0] == "piedra" :
                        print ("Ganador: Jugador 1");

                    elif hands[0] == "piedra" and hands[1] == "papel" or\
                        hands [0] == "papel" and hands[1] == "tijera" or\
                        hands [0] == "tijera" and hands[1] == "piedra":
                        print ("Ganador: Jugador 2"); 

                    elif hands[0] == hands[1]:
                        print ("Empate");           

                else:

                    list_options = ["papel", "tijera", "piedra"]
                    jugada_pc = random.choice(list_options)
                    
                    print ("Pc ha sacado: " + jugada_pc)
                    
                    if jugada_pc == "piedra" and hands[0] == "papel" or\
                        jugada_pc == "papel" and hands[0] == "tijera" or\
                        jugada_pc == "tijera" and hands[0] == "piedra" :
                        print ("Ganaste")
                        points[0] += 1

                    elif jugada_pc == hands[0]:
                        print ("Empate")
                        points[1] += 1
                    
                    else :
                        print ("Perdiste sigue intentando")
                        points[2] += 1
                    
                    print ("Ganados: " + str(points[0])+ " Empatados: " + str(points[1]) + " Perdidos: " + str(points[2]))
                    
                aswer = input("\nQuieres seguir jugando? (si/no): ")
                if aswer == "no":
                    break

        return wrapper

    return game

title = """
            ****************************************
            Prueba tu suerte: Piedra, Papel o Tijera
            ****************************************
            """
                
@game_title(title)
def turns():

    list_options = ["papel", "tijera", "piedra"]
    hands = []
    number_of_players = int(input("Ingrese cantidad de jugadores [1(vs CPU) - 2(vs Player)]: "))

    if number_of_players == 1:
        player_hand = ""
        while player_hand not in list_options:
            try:
                player_hand = input ("Ingrese jugada [papel, piedra o tijera]: ").lower()
                if player_hand.isalpha() and player_hand in list_options:
                    hands.append(player_hand)  
                    print ("Tú has sacado: " + hands[0])
                else :
                    raise ValueError

            except ValueError:
                print("Opción o carácter[A-Z, a-z] no válido")
           
        return hands

    elif number_of_players == 2:
        for i in range(number_of_players):
            player_hand = ""
            while player_hand not in list_options:
                try:
                    player_hand = input ("Jugador "+str(i+1) +", ingrese jugada [papel, piedra o tijera]: ").lower()
                    if player_hand.isalpha() and player_hand in list_options:
                        hands.append(player_hand) 
                    else:
                        raise ValueError

                except ValueError:
                    print("Opción o carácter[A-Z, a-z] no válido")   

        return hands

    else:
        print ("Ingrese una cantidad de jugadores válida")
        turns()
        

if __name__ == '__main__':

   turns()
