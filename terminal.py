import questionary
from questionary import Choice
import webbrowser

rickrolls = 0


while True:
    choice = questionary.select(
        f'выбери девушку для просмотра прайвт контента (рикроллов: {rickrolls})',
        choices=[
            Choice(
                title='мавильская',
                value='ww'
            ),
            Choice(
                title='щербакова',
                value='ss'
            ),
            Choice(
                title='выход',
                value=None
            ),
        ]
    ).ask()

    podmenu = None

    if choice == 'ww':
        podmenu = questionary.select(
            'выбери категорию',
            choices=[
                Choice(
                    title='видосы с хаты + кружочек',
                    value='https://cutt.ly/myEzEFJw'
                ),
                Choice(
                    title='фотки с моря',
                    value='https://cutt.ly/myEzEFJw'
                ),
            ]
        ).ask()

    elif choice == 'ss':
        podmenu = questionary.select(
            'выбери категорию',
            choices=[
                Choice(
                    title='кружочек + 2 видоска с днюшки',
                    value='https://cutt.ly/myEzEFJw'
                ),
                Choice(
                    title='фотки не знаю откуда))',
                    value='https://cutt.ly/myEzEFJw'
                ),
            ]
        ).ask()

    else:
        print('выход из программы')
        break

    if podmenu:
        webbrowser.open(podmenu)
        rickrolls += 1
        print(f"ты выбрал: rickroll (всего раз: {rickrolls})")
