__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_update_user_information(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()
        time.sleep(5)
        username = self.browser.find_element_by_id('usrname')
        username.send_keys('feruiz')
        password = self.browser.find_element_by_id('passwd')
        password.send_keys('clave123')
        botonGrabar = self.browser.find_element_by_id('id_aceptar')
        botonGrabar.click()
        time.sleep(3)
        editar = self.browser.find_element_by_id('id_editar')
        editar.click()
        time.sleep(5)
        nombre = self.browser.find_element_by_id("editar-form").find_element_by_id("id_nombre")
        nombre.clear()
        nombre.send_keys('Fernando')

        apellidos = self.browser.find_element_by_id("editar-form").find_element_by_id('id_apellidos')
        apellidos.clear()
        apellidos.send_keys('Ortiz')

        botonGrabar = self.browser.find_element_by_id("editar-form").find_element_by_id('id_grabar')
        botonGrabar.click()

        botonCancelar = self.browser.find_element_by_id("editar-form").find_element_by_id('id_cancelar')
        botonCancelar.click()
        time.sleep(5)
        link = self.browser.find_element_by_id('id_logout')
        link.click()
        time.sleep(5)

        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Fernando Ortiz"]')

        self.assertIn('Fernando Ortiz', span.text)


    def test_registro(self):
            self.browser.get('http://localhost:8000')
            link = self.browser.find_element_by_id('id_register')
            link.click()
            time.sleep(3)
            nombre = self.browser.find_element_by_id('id_nombre')
            nombre.send_keys('Juan Daniel')

            apellidos = self.browser.find_element_by_id('id_apellidos')
            apellidos.send_keys('Arevalo')

            experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
            experiencia.send_keys('5')

            self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='DESARROLLO WEB']").click()
            telefono = self.browser.find_element_by_id('id_telefono')
            telefono.send_keys('3173024578')

            correo = self.browser.find_element_by_id('id_correo')
            correo.send_keys('jd.patino1@uniandes.edu.co')

            nombreUsuario = self.browser.find_element_by_id('id_username')
            nombreUsuario.send_keys('juan645')

            clave = self.browser.find_element_by_id('id_password')
            clave.send_keys('clave123')

            botonGrabar = self.browser.find_element_by_id('id_grabar')
            botonGrabar.click()
            self.browser.implicitly_wait(3)
            span=self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

            self.assertIn('Juan Daniel Arevalo', span.text)

    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span=self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()
        time.sleep(5)
        h2=self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_hacerLogin(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()
        time.sleep(1)
        username = self.browser.find_element_by_id('usrname')
        username.send_keys('feruiz')
        password = self.browser.find_element_by_id('passwd')
        password.send_keys('clave123')
        botonGrabar = self.browser.find_element_by_id('id_aceptar')
        botonGrabar.click()
        btnEditar = self.browser.find_element_by_id('id_editar')
        self.assertIsNotNone(btnEditar, "Fallo prueba login")

    def test_crear_comentario(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()
        time.sleep(3)
        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')
        self.assertIn('Juan Daniel Arevalo', h2.text)
        time.sleep(1)
        correo = self.browser.find_element_by_id('correo')
        correo.send_keys('juam@gmail.com')
        comentario = self.browser.find_element_by_id('comentario')
        comentario.send_keys('Este es un comentariooo ')
        time.sleep(1)
        botonGrabar = self.browser.find_element_by_id('id_guarda_comentario')
        botonGrabar.click()


