import keyboard
import random


active = True
cursed_list = ["uwu", ":3", "owo", "nya~", "*blush*", "<3"]


def add_uwu(arg):
    if not active: return
    if str(arg) == "KeyboardEvent(space up)": return

    rand = random.randint(1, 3)
    if rand == 1:
        keyboard.write(f"{random.choice(cursed_list)} ")


def activate():
    global active
    active = not active


def main():
    keyboard.hook_key("space", add_uwu)
    keyboard.add_hotkey("f21", activate)
    keyboard.wait()


if __name__ == "__main__":
    main()
