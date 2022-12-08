import pyautogui

#teamsten otomatik mesaj yolladık
pyautogui.moveTo(799, 466, duration=2, tween=pyautogui.easeInOutQua)
pyautogui.click()
for i in range(100):
    pyautogui.write("evet", interval=0.01)
    pyautogui.press('enter')

