import pyautogui
import platform
import pynput
import time
import directkeys
right = 0xCd
linux = False
class Controller:
	def __init__(self):
		global linux
		self.os = platform.system()
		print(self.os)
		self.screen = pyautogui.size()

		# Region of interest
		self.roi = [-1, -1, -1, -1]

		if self.os == 'Windows':
			linux = False
			# import fails while using Linux
			import pygetwindow as gw

			window = gw.getAllTitles()
			for title in window:
				if "Super" in title or "Dolphin" in title:
					window = title

			window = gw.getWindowsWithTitle(window)[0]
			window.moveTo(5, 5)
			window.resizeTo(600, 500)

			self.roi[0], self.roi[1] = window.topleft
			self.roi[2], self.roi[3] = window.bottomright

		elif self.os == 'Linux':
			linux = True
			print("Linux OS requires game window calibration")
			self.calibrate_screen()
			print("Calibration complete")
			print()

	def click(self):
		pyautogui.click()

	def moveTo(self, x, y):
		pyautogui.moveTo(x,y)

	def calibrate_screen(self):
		print("Move mouse to top left of game window and click")

		# capture mouse location when clicked
		with pynput.mouse.Listener(on_click=self.on_click) as listener:
			listener.join()
		print(self.roi)
		print("Move mouse to bottom of game window and click")

		with pynput.mouse.Listener(on_click=self.on_click) as listener:
			listener.join()

		print("Screen calibrated to ", self.roi)


	def on_click(self, x, y, button, pressed):
		if pressed:
			# set the values of roi
			if self.roi[0] ==  -1:
				self.roi[0] = x
			elif self.roi[2] == -1:
				self.roi[2] = x

			if self.roi[1] == -1:
				self.roi[1] = y
			elif self.roi[3] == -1:
				self.roi[3] = y

			# Release listener
			return False

	def win_press(self, x):
		directkeys.PressKey(x)

	def win_release(self, x):
		directkeys.ReleaseKey(x)

	def press(self, key):
		pyautogui.press(key)

	def keyDown(self, key):
		press_time = 0.5
		pyautogui.keyDown(key)
		time.sleep(press_time)
		pyautogui.keyUp(key)

	def keyUp(self, key):
		pyautogui.keyUp(key)


	def center(self):
		centerx = ((self.roi[2] - self.roi[0]) / 2) + self.roi[0]
		centery = ((self.roi[3] - self.roi[1]) / 2) + self.roi[1]
		pyautogui.moveTo(centerx, centery)

def main():
	controller = Controller()
	controller.center()
	controller.click()

	for i in range(5):
		if linux == True:
			# double jump
			controller.keyDown('right')
			time.sleep(0.1)
			controller.keyDown('right')
			time.sleep(1)
		else:
			controller.win_press(right)
			time.sleep(0.1)
			controller.win_release(right)
			time.sleep(1)

if __name__=="__main__":
	main()