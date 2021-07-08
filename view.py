class Menu:

    def main_menu(self):
        print("Tournament Menu")
        print("1 - Create Tournament")
        print("2 - Add Player ")
        print("0 - Quit")

        answer = input("Choose a number : ")


    def tournament_infos(self):
        tournament_name = input("Entrez le nom du tournois: ")
        tournament_place = input("Entrez le lieu du tournois: ")
        tournament_date = input("Entrez la date du tournois: ")
        tournament_rounds = input("Entrez le nombre de tours: ")
        tournament_players = input("Entrez le nombre de participants: ")
        tournament_type = input("Entrez le style de partie: ")
        return tournament_name, tournament_place, tournament_date, tournament_rounds,
                tournament_players, tournament_type

    def new_player(self):
        player_lastname = input("Entrez le Nom du joueur: ")
        player_firstname = input("Entrez le prénom du joueur: ")
        player_age = input("Entrez l'age du joueur: ")
        player_birthdate = input("Entrez la date de naissance du joueur: ")
        player_gender = input("Entrez le genre du joueur: ")
        player_rank = input("Entrez le rang du joueur: ")
        return (player_lastname, player_firstname, player_age, player_birthdate, player_gender,
                player_rank)


