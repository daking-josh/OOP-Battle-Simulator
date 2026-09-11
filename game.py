from goblin import Goblin


<<<<<<< HEAD
ARENA_NAME = "MetLife stadium"
=======
ARENA_NAME = "The Iron Lung"
>>>>>>> feature/second-goblin


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gaints")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")

    goblin = Goblin("rat")
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print("But no hero has answered the call... yet.")

if __name__ == "__main__":
    main()
