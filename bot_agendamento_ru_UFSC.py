# -*- coding: utf-8 -*-
"""
Created on Thu May 26 08:51:49 2022

@author: micao
"""

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://sistemas.ufsc.br/login?service=https%3A%2F%2Fsgpru.sistemas.ufsc.br%2Fagendamento%2Fj_spring_cas_security_check")   

userUFSC        ='SeuLogin'
senhaUFSC       ='SuaSenha'

userUFSC = str(userUFSC)
senhaUFSC = str(senhaUFSC)
user = driver.find_element_by_xpath('//*[@id="username"]')
user.send_keys(userUFSC)
pas = driver.find_element_by_xpath('//*[@id="password"]')
pas.send_keys(senhaUFSC)
driver.find_element_by_xpath('//*[@id="fm1"]/div/input').click()

driver.find_element_by_xpath('//*[@id="menuForm:j_idt54"]/ul/li[2]/a/span').click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="agendamentoForm:refeicao"]/option[2]').click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="agendamentoForm:dtRefeicao"]/option[2]').click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="agendamentoForm:hrRefeicao"]/option[2]').click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="agendamentoForm:j_idt93"]/span[2]').click()




