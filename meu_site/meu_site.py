# -*- coding:utf-8 -*-
from settings import settings
from f5.config import F5_Application


def main():
    application = F5_Application(settings)
    # start server
    application.run()

if __name__ == '__main__':
    main()
