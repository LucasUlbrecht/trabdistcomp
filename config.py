import logging
from flask import Flask
import os
import json

class Config:
    CONFIG_FILE = 'cfg/app.cfg'
    
    @classmethod
    def load_config(cls, app: Flask):
        if os.path.exists(cls.CONFIG_FILE):
            with open(cls.CONFIG_FILE) as config_file:
                for line in config_file:
                    if line.strip() and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        key = key.strip()
                        value = value.strip().strip("'")  # Remove as aspas simples

                        if key == 'ADMINISTRATORS':
                            value = json.loads(value.replace("'", "\""))

                        if isinstance(value, str) and value.lower() in ['true', 'false']:
                            value = value.lower() == 'true'
                    
                        # Adiciona a lógica para mapear DATABASE para SQLALCHEMY_DATABASE_URI
                        if key == 'DATABASE':
                            app.config['SQLALCHEMY_DATABASE_URI'] = value
                    
                        app.config[key] = value


    @classmethod
    def log_configure(cls):
        logging.basicConfig(format='%(asctime)s - %(message)s', filename='application.log', level=logging.INFO)
        log = logging.getLogger()
