import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    html = '''
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Главная</title>
        </head>
        <body>
        <header>
            <ul>
                <li><a href="/">Главная</a></li>
                <li><a href="/about">О себе</a></li>
            </ul>
        </header>
        <main>
            <h1>Мой первый сайт на Django!</h1>
        </main>
        <footer>
            <p><em>© Copyright 2023</em></p>
        </footer>
        </body>
        </html>'''

    logger.info(f'Открыта Главная страница')
    return HttpResponse(html)


def about(request):
    html = '''
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>О себе</title>
        </head>
        <body>
        <header>
            <ul>
                <li><a href="/">Главная</a></li>
                <li><a href="/about">О себе</a></li>
            </ul>
        </header>
        <main>
            <h1>Немного обо мне</h1>
            <p>
                Неужели писать верстку HTML - задача бекенд-разработчика?<br>
                Вот и я так не считаю. Конец.
            </p>
        </main>
        <footer>
            <p><em>© Copyright 2023</em></p>
        </footer>
        </body>
        </html>'''

    logger.info(f'Открыта страница О себе')
    return HttpResponse(html)
