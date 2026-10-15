import questionary
from questionary import Choice
import webbrowser

while True:
    a=input('введите свое имя: ')
    print(f'\nпривяу  {a}')

    choice = questionary.select(
        'выбери девушку для просмотра прайвт контента',
        choices=[
            Choice(
                title='настюха чеченина',
                value='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            ),
            Choice(
                title='сашка мороз',
                value='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
            ),
            Choice(
                title='выход',
                value=None
            )
        ]
    ).ask()
    if choice:
        webbrowser.open(choice)

        print(f"Ты выбрал: {choice}")
        break
    else:
        print('выход из программы')
        break
