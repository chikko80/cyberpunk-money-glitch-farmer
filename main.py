import pydirectinput
from imagesearch import *
import time

import win32api, win32con

delay = 0.3

def main():
    time.sleep(3)
    def start():
        close_shop()
        open_shop()
        click_category()
        def inner():
            click_item_relative_to_category()
            close_shop()
            open_shop()
            click_item_relative_to_start_pos()
            if automat_empty():
                close_shop()
                restock_automat()
                return True
            click_category_rel_to_buy_item()
        while True:
            restocked = inner()
            if restocked:
                break
    while True:
        start()


def check():
    while True:
        print(pydirectinput.position())
        time.sleep(1)

def open_shop():
    print('open shop')
    pydirectinput.press('r')
    time.sleep(delay)

def close_shop():
    print('close shop')
    def still_in_store():
        pos = imagesearch("images\\in_store.png")
        if pos[0] != -1:
            return True
        return False
    if still_in_store(): #checks if in store
        pydirectinput.press('esc')
        time.sleep(0.5)
    if still_in_store():
        pydirectinput.press('esc')
    time.sleep(delay)


def click_category():
    find_image_and_click("images\\all_items.png")

def click_item_relative_to_start_pos():
    find_image_and_click("images\\item.png")

def click_item_relative_to_category():
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -130, 100, 0, 0)
    pydirectinput.click()
    # time.sleep(wait_for_empty) #wait for message if shop is empty
    time.sleep(delay)

def click_category_rel_to_buy_item():
    print("rel to buyitem")
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -640, -30, 0, 0)
    pydirectinput.click()
    time.sleep(delay)

def automat_empty():
    pos = imagesearch("images\\empty.png",precision=0.90)
    if pos[0] != -1:
        print("empty")
        return True
    return False

def restock_automat():
    print('restock')
    open_menu()
    find_image_and_click("images\\wait.png")
    reset_time()

def reset_time():
    print('reset_time')
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 400, -290, 0, 0)
    time.sleep(0.1)
    pydirectinput.click()
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 50, 0, 0)
    time.sleep(0.1)
    pydirectinput.press("f")
    time.sleep(delay)
    close_menu()
    time.sleep(delay)

def open_menu():
    print('open menu')
    pydirectinput.press('i')
    time.sleep(delay)

def close_menu():
    print('close menu')
    def still_in_menu():
        pos = imagesearch("images\\warten.png")
        if pos[0] != -1:
            return True
        return False
    pydirectinput.press('esc')
    time.sleep(0.5)
    if still_in_menu():
        pydirectinput.press('esc')

def move_mouse(os_x,os_y):
    ingame_x = os_x - 960
    ingame_y = os_y - 540

    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, ingame_x, ingame_y, 0, 0)

def find_image_and_click(img_path):
    while True:
        pos = imagesearch(img_path)
        if pos[0] != -1:
            print("position : ",pos[0], pos[1])
            x = pos[0] + 50
            y = pos[1] + 20
            move_mouse(x,y)
            time.sleep(0.3)
            pydirectinput.click()
            break
        else:
            print("not found")
        pass
    time.sleep(delay)


if __name__ == "__main__":
    # main()
    main()
