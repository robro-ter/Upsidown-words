from pynput import keyboard
from pynput.keyboard import Key, Controller
import threading
import keyboard as no
import time
print('close the python window to stop program\nwords of advice: backspace is supper laggy when this is running, also it is not optimized well and... may lag')
global rate
rate=0
def this():
    while 1:
        global rate
        time.sleep(.00001)
        rate=0

rate1 = threading.Thread(target=this)
rate1.start()

thing = Controller()
def second_this():
    while 1:
        global rate
        if no.is_pressed('1') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('⇂')
            thing.release('⇂')
            rate += 1
        if no.is_pressed('2') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('↊')
            thing.release('↊')
            rate += 1
        if no.is_pressed('3') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('↋')
            thing.release('↋')
            rate += 1
        if no.is_pressed('6') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('9')
            thing.release('9')
            rate += 1
        if no.is_pressed('7') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('𝘓')
            thing.release('𝘓')
            rate += 1
        if no.is_pressed('9') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('6')
            thing.release('6')
            rate += 1
        if no.is_pressed('!') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('¡')
            thing.release('¡')
            rate += 1
        if no.is_pressed('&') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('⅋')
            thing.release('⅋')
            rate += 1
        if no.is_pressed('_') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('‾')
            thing.release('‾')
            rate += 1
        if no.is_pressed('(') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press(')')
            thing.release(')')
            rate += 1
        if no.is_pressed(')') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('(')
            thing.release('(')
            rate += 1
        if no.is_pressed('q') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('b')
            thing.release('b')
            rate += 1
        if no.is_pressed('w') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ʍ')
            thing.release('ʍ')
            rate += 1
        if no.is_pressed('e') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ǝ')
            thing.release('ǝ')
            rate += 1
        if no.is_pressed('r') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ɹ')
            thing.release('ɹ')
            rate += 1
        if no.is_pressed('t') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ʇ')
            thing.release('ʇ')
            rate += 1
        if no.is_pressed('y') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ʎ')
            thing.release('ʎ')
            rate += 1
        if no.is_pressed('u') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('n')
            thing.release('n')
            rate += 1
        if no.is_pressed('i') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ᴉ')
            thing.release('ᴉ')
            rate += 1
        if no.is_pressed('o') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ᴏ')
            thing.release('ᴏ')
            rate += 1
        if no.is_pressed('p') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('d')
            thing.release('d')
            rate += 1
        if no.is_pressed('a') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ɐ')
            thing.release('ɐ')
            rate += 1
        if no.is_pressed('d') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('p')
            thing.release('p')
            rate += 1
        if no.is_pressed('f') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ⅎ')
            thing.release('ⅎ')
            rate += 1
        if no.is_pressed('g') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ƃ')
            thing.release('ƃ')
            rate += 1
        if no.is_pressed('h') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ɥ')
            thing.release('ɥ')
            rate += 1
        if no.is_pressed('j') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ɾ')
            thing.release('ɾ')
            rate += 1
        if no.is_pressed('k') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ʞ')
            thing.release('ʞ')
            rate += 1
        if no.is_pressed('l') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ʅ')
            thing.release('ʅ')
            rate += 1
        if no.is_pressed('c') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ɔ')
            thing.release('ɔ')
            rate += 1
        if no.is_pressed('v') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ʌ')
            thing.release('ʌ')
            rate += 1
        if no.is_pressed('b') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('q')
            thing.release('q')
            rate += 1
        if no.is_pressed('n') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('u')
            thing.release('u')
            rate += 1
        if no.is_pressed('m') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('ɯ')
            thing.release('ɯ')
            rate += 1
        if no.is_pressed("'") and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press('╻')
            thing.release('╻')
            rate += 1
        if no.is_pressed(',') and rate==0:
            thing.press(Key.backspace)
            thing.release(Key.backspace)
            thing.press("'")
            thing.release("'")
            rate += 1
main = threading.Thread(target=second_this)
main.start()
