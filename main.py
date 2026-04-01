import curses
import time
import random

# starting window
def start(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin...")
    stdscr.refresh()
    stdscr.getkey()


# Load the typing text
def load_test():
    with open("text.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

# test WORD PER MINUTE and show it on screen
def wpm_test(stdscr):
    target_text = load_test()
    user_text = []
    wpm =0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time,1)

        wpm = round((len(user_text) / (time_elapsed/60)) /5)

        stdscr.clear()
        stdscr.addstr(target_text)
        stdscr.addstr(1,0,f"WPM : {wpm} ")
        for i, char in enumerate(user_text):
            correct_char = target_text[i]
            color = curses.color_pair(1)
            if char != correct_char:
                color = curses.color_pair(2)
            stdscr.addstr(0,i,char, color)

        if "".join(user_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        # for exit
        if ord(key)==27:
            break

        # backspace
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(user_text)>0:
                user_text.pop()

        # adds the user text
        elif len(user_text)<len(target_text):
            user_text.append(key)


        stdscr.refresh()
    
        

def main(stdscr):
    curses.curs_set(0)
    
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    start(stdscr)
    while True:
        wpm_test(stdscr)

        # After the test
        stdscr.addstr(3,0,"You completed the test! Press any key to continue (Esc to exit)",curses.color_pair(3))
        key = stdscr.getkey()
        if ord(key)==27:
            break



curses.wrapper(main)