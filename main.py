import os
from pathlib import Path
from create_map import *
from show_map import *
from get_map import *
from find_bsq import *
import typer

def show_title(name, color, nbr_equals):
    os.system('clear')
    page = typer.style(name, fg=color)
    print(f"|{'#' * nbr_equals * 2 + '#' * len(name)}|")
    typer.echo(f"|{'=' * nbr_equals}{page}{'=' * nbr_equals}|")
    print(f"|{'#' * nbr_equals * 2 + '#' * len(name)}|")

def home():
    show_title("MENU", "yellow", 20)
    print("1. Générer une map.")
    print("2. Résoudre une map.")
    print("3. Quitter.")
    choix = input("-> ")
    if choix == "1":
        generate_map()
    elif choix == "2":
        show_my_maps()
    elif choix.lower() in ["3", "q", "quit"]:
        typer.secho("\nBye !", fg=typer.colors.YELLOW)#, bg=typer.colors.YELLOW) 
        return
    else:
        home()

def generate_map():
    show_title("GENERATEUR", "blue", 15)
    try:
        nbr_lines = int(input("Nombre de lignes : "))
        nbr_column = int(input("Longueur des lignes : "))
        density = int(input("Densité d'obstacles : "))
        char = input("Charactères utilisées {ex.: '.ox'} : ")
        num_map = create_map(nbr_column, nbr_lines, density, {"empty": char[0], "obstacle": char[1], "full": char[2]})
        show_map(get_full_map(f"maps/map{num_map}"))
        succes = typer.style("succès", fg="bright_green")
        typer.echo(f"Votre map a été généré avec {succes} !")
        input("(Appuyer sur Entrée pour revenir à l'accueil)")
        home()
    except:
        erreur = typer.style("Erreur !", fg="red")
        typer.echo(f"{erreur} Une valeur que vous avez entré est incorrecte.")
        input("(Appuyer sur Entrée pour recommencer)")
        generate_map()

def show_all_colors():
    all_colors = ["bright_black", "black", "bright_red", "red", "bright_green", 
                  "green", "bright_yellow", "yellow", "bright_blue", "blue", 
                  "bright_magenta", "magenta", "bright_cyan", "cyan", "bright_white", "white",]
    print("1. Noir brillant  | 2. Noir  | 3. Rouge Brillant    | 4. Rouge")
    print("5. Vert brillant  | 6. Vert  | 7. Jaune Brillant    | 8. Jaune")
    print("9. Bleu brillant  | 10. Bleu | 11. Magenta Brillant | 12. Magenta")
    print("13. Cyan brillant | 14. Cyan | 15. Blanc Brillant   | 16. Blanc")

def show_my_maps():
    show_title("MAPS", "blue", 20)
    num_map = 0
    cur_dir = Path.cwd()
    print("N° | Dimensions | Motif")
    while (Path(f"{cur_dir}/maps/map{num_map}").is_file()):
        mapfile = f"maps/map{num_map}"
        map = get_full_map(mapfile)
        i_map = get_info_map(map)
        space_dimensions = 11 - len(f"[{i_map['nbr_lines']}x{len(map[1])}]")
        space_num_map = 3 - len(str(num_map))
        print(f"{num_map}{' ' * space_num_map}| [{i_map['nbr_lines']}x{len(map[1])}]{' ' * space_dimensions}| [{i_map['empty']}{i_map['obstacle']}{i_map['full']}]")
        num_map += 1
    try:
        all_colors = ["bright_black", "black", "bright_red", "red", "bright_green", 
                  "green", "bright_yellow", "yellow", "bright_blue", "blue", 
                  "bright_magenta", "magenta", "bright_cyan", "cyan", "bright_white", "white",]
        choix = input("-> ")
        if choix in ["q", "quit", "b", "back", "return"]:
            home()
            return
        elif choix.startswith("rm"):
            if (Path(f"{cur_dir}/maps/map{choix[2:]}").is_file()):
                Path(f"{cur_dir}/maps/map{choix[2:]}").unlink()
                show_my_maps()
                return
        mapfile = f"maps/map{choix}"
        map = get_full_map(mapfile)
        answer = algorithm_to_find(map)
        resolve_map = replace_by_square(map, answer["x"], answer["y"], answer["l"])
        show_all_colors()
        colors = int(input("Indiquez une couleur -> "))
        show_title("SOLUTION", "green", 18)
        compare_map_with_highlight(map, resolve_map, colors)
        dimensions = typer.style(f"{answer['l']}x{answer['l']}", fg=all_colors[colors - 1])
        typer.echo(f"Le plus grand carré de cette map a une dimension de {dimensions}.")
        input("(Appuyer sur Entrée pour revenir en arrière)")
        show_my_maps()
    except:
        erreur = typer.style("Erreur !", fg="red")
        typer.echo(f"{erreur} Une valeur que vous avez entré est incorrecte.")
        input("(Appuyer sur Entrée pour recommencer)")
        show_my_maps()

home()