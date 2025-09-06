import configparser

config=configparser.RawConfigParser()
config.read(r"C:\Users\Rahul\PycharmProjects\Ecommerce\Configurations\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationUrl(self):
        url=config.get('common info','baseURl')
        return url

    @staticmethod
    def getUsername(self):
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword(self):
        password = config.get('common info', 'password')
        return password

