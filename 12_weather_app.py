# Programa de Clima

import sys
import requests

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel('Ingresa el nombre de la Ciudad: ', self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton('Obtener Clima', self)
        self.temperature_label = QLabel('', self)
        self.emoji_label = QLabel('', self)
        self.description_label = QLabel('', self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle('Programa del Clima')

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName('city_label')
        self.city_input.setObjectName('city_input')
        self.get_weather_button.setObjectName('get_weather_button')
        self.temperature_label.setObjectName('temperature_label')
        self.emoji_label.setObjectName('emoji_label')
        self.description_label.setObjectName('description_label')

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: Arial;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-familt: Segoe UI emoji;
            }
            QLabel#description_label {
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = 'e22a3b257750a981a6aad1c68b4530ab'
        city = self.city_input.text()
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data['cod'] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error('Solicitud Incorrecta: \nIngresa la ciudad correctamente')
                case 401:
                    self.display_error('Sin Autorizacion: \nLlave de API no valida')
                case 403:
                    self.display_error('Prohibido: \nAcceso denegado')
                case 404:
                    self.display_error('No encontrado: \nCiudad no encontrada')
                case 500:
                    self.display_error('Error de Server Interno: \nIntentalo otra vez en un momento')
                case 502:
                    self.display_error('Mala puerta de entrada: \nRespuesta no validad por parte del servidor')
                case 503:
                    self.display_error('Servicio no disponible: \nServidor esta caido')
                case 504:
                    self.display_error('Servidor agoto el tiempo: \nNo hubo respuesta por parte del servidor')
                case _:
                    self.display_error(f'Error HTTP: \n{http_error}')

        except requests.exceptions.ConnectionError:
            self.display_error('Error de Conexion: \nRevisa tu conexion de internet')

        except requests.exceptions.Timeout:
            self.display_error('Error de tiempo de espera: \nLa solicitu expiro')

        except requests.exceptions.TooManyRedirects:
            self.display_error('Demasiadas redirecciones: \nRevisa el enlace')

        except requests.exceptions.RequestException as req_error:
            self.display_error(f'Error de Solicitud: \n{req_error}')

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        temperature_k = data['main']['feels_like']
        temperature_c = round(temperature_k - 273.15, 0)
        weather_description = data['weather'][0]['description']
        weather_id = data['weather'][0]['id']

        self.temperature_label.setText(f'{temperature_c:.0f}°C')
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):

        if weather_id >= 200 and weather_id <= 232:
            return '⛈️'
        elif weather_id >= 300 and weather_id <= 321:
            return '🌦️'
        elif weather_id >= 500 and weather_id <= 531:
            return '🌧️'
        elif weather_id >= 600 and weather_id <= 622:
            return '❄️'
        elif weather_id >= 701 and weather_id <= 781:
            return '⚠️'
        elif weather_id == 800:
            return '☀️'
        elif weather_id >= 801 and weather_id <= 804:
            return '☁️'
        else:
            return ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())