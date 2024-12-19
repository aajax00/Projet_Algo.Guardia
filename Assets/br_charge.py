import sys
import time

GREEN = "\033[1;32m"
END = "\033[0m" 

# barre de chargement
def br_charge():
    for i in range(1, 21):
        sys.stdout.write(f"\rChargement : [{GREEN}{'#' * i}{'.' * (20 - i)}{END}] {GREEN}{i * 5}%{END}")
        sys.stdout.flush()
        time.sleep(0.02)
    print()