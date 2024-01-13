import configparser
import logging
import sys
import os
import openai
import streamlit as st

class Config:
    CONFIG_FILE_PATH = "config.ini"
    OPENAI_API_KEY_ENV_VAR = "OPENAI_API_KEY"

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(self.CONFIG_FILE_PATH)

        # OpenAI API key
        self.openai_key = st.secrets["API_KEY"]
        self.__set_env_openai_key()

        # Logging level
        self.log_level = config['LOGGING']['LEVEL'].casefold()
        self.__set_log_level()

        # The best file reader will be automatically selected (from the given file extensions).
        self.simple_data_dir = config['DATA']['SIMPLE_DIR']
        # Wikipedia pages will be downloaded from the web with WikipediaReader.
        self.wiki_pages_file_path = config['DATA']['WIKIPEDIA_PAGES']

        self.storage_dir = config['INDEX']['STORAGE']
        self.engine = config['INDEX']['ENGINE'].casefold()

    def __set_env_openai_key(self):
        os.environ[self.OPENAI_API_KEY_ENV_VAR] = self.openai_key
        openai.api_key = os.environ[self.OPENAI_API_KEY_ENV_VAR]

    def __set_log_level(self):
        level = logging.INFO
        if self.log_level == "debug":
            level = logging.DEBUG

        logging.basicConfig(stream=sys.stdout, level=level)

    def is_engine_chat(self):
        return self.engine == "chat"

    def is_engine_query(self):
        return self.engine == "query"
