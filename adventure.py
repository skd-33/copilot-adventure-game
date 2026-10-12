STORY = {
    "start": {
        "text": "You wake at the edge of an enchanted forest with a worn map.",
        "choices": {
            "1": ("Follow the moonlit path", "forest", "lantern"),
            "2": ("Enter the silent cave", "cave", "rope"),
        },
    },
    "forest": {
        "text": "A silver fox blocks the path and points toward a crumbling tower.",
        "choices": {
            "1": ("Offer the fox a kind word", "tower", "charm"),
            "2": ("Climb a strange stone staircase", "ravine", None),
        },
    },
    "cave": {
        "text": "The cave splits in two. A cold breeze whispers from the left.",
        "choices": {
            "1": ("Follow the breeze", "underground", None),
            "2": ("Take the warm tunnel", "dragon", None),
        },
    },
    "tower": {
        "text": "At the tower roof, a trapped star begs you to open its crystal cage.",
        "choices": {
            "1": ("Use the charm to free the star", "star_win", None),
            "2": ("Take the glowing crystal", "tower_fall", None),
        },
    },
    "underground": {
        "text": "You find an ancient boat and a river flowing beneath the mountain.",
        "choices": {
            "1": ("Cross the river", "river_win", None),
            "2": ("Sail into the black waterfall", "waterfall", None),
        },
    },
    "dragon": {
        "text": "A sleepy dragon guards the only exit. Your lantern flickers.",
        "choices": {
            "1": ("Sing it a lullaby", "dragon_sleep", None),
            "2": ("Try to sneak past", "dragon_lose", None),
        },
    },
    "ravine": {"text": "The stairs crumble beneath you. The ravine claims another traveler.", "end": "LOSE"},
    "tower_fall": {"text": "The crystal shatters. The tower collapses into the dark.", "end": "LOSE"},
    "waterfall": {"text": "The waterfall carries you into an endless underground sea.", "end": "LOSE"},
    "dragon_sleep": {"text": "The dragon snores peacefully. You escape with its treasure!", "end": "WIN"},
    "star_win": {"text": "The star bursts free and grants you a wish: you are home, victorious!", "end": "WIN"},
    "river_win": {"text": "The river delivers you to a hidden city where you are crowned explorer.", "end": "WIN"},
    "dragon_lose": {"text": "The dragon wakes and mistakes your footsteps for dinner.", "end": "LOSE"},
}
def play():
    scene, inventory = "start", []
    while True:
        current = STORY[scene]
        print("\n" + current["text"])
        if inventory: print("Inventory:", ", ".join(inventory))
        if "end" in current:
            print("You " + current["end"].lower() + "!")
            return
        for key, choice in current["choices"].items():
            print(f"{key}. {choice[0]}")
        answer = input("> ").strip()
        if answer not in current["choices"]:
            print("Choose one of the numbered options.")
            continue
        _, scene, item = current["choices"][answer]
        if item and item not in inventory: inventory.append(item)
if __name__ == "__main__":
    print("THE STARFALL MAP")
    while True:
        play()
        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break
