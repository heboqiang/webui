# #!/usr/bin/env python
# #-*-coding:utf-8-*-
#
# import  unittest
# from selenium import  webdriver
# from page.shopHu import *
# from page.login import *
#
# from ui3333.page.login import Login
# from ui3333.page.shopHu import ShopHu
#
# import time
#
# class LoginTest(unittest.TestCase,ShopHu,Login):
# 	def setUp(self,value='url'):
# 		self.driver=webdriver.Firefox()
# 		self.driver.maximize_window()
# 		self.driver.implicitly_wait(30)
# 		self.driver.get(self.getXmlData(value))
#
# 	def tearDown(self):
# 		self.driver.quit()
#
# 	def test_01(self):
# 		time.sleep(5)
# 		# self.login_business.login_pass()
# 		# self.login_business.go_paizhao()
# 		self.login_business.go_tianqi ()
#
#
# 		#self.assertNotEqual(1,2)
# 		#self.assertTrue(flag)
# 		#self.assertFalse(flag)
# 	#@unittest.skip("CaseTest")
# 	# def test_02(self):
# 	# 	self.login_business.login_user_error()
# 	# 	print ("this is case02\n")
# 	# 	self.assertTrue(True)
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
#
#
