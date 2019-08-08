#!/usr/bin/env python 
#-*-coding:utf-8-*-

import  unittest
# from page.login import *
from selenium import  webdriver
from common.logger import Log
from business.login_business import LoginBusiness


import time


class LoginTest(unittest.TestCase):
	def setUp(self,value='https://www.baidu.com'):
		self.driver=webdriver.Chrome()
		self.driver.get(value)
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.log = Log()
		self.login_business = LoginBusiness()
	def tearDown(self):
		self.driver.quit()

	def test_01(self):
		time.sleep(5)
		self.log.info("------登录失败用例：start!---------")
		# self.login_business.login_pass()
		# self.login_business.go_paizhao()
		self.login_business.go_baidu()


		#self.assertNotEqual(1,2)
		#self.assertTrue(flag)
		#self.assertFalse(flag)
	#@unittest.skip("CaseTest")
	# def test_02(self):
	# 	self.login_business.login_user_error()
	# 	print ("this is case02\n")	def tearDown(self):
	# 		self.driver.quit()
	# 	self.assertTrue(True)

if __name__ == '__main__':
    unittest.main(verbosity=2)


