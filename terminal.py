import webbrowser
import sys
import questionary
from questionary.prompts.common import Choice

nazv=[]
sites=[]
def n(user):
    if user.lower() == 'stop' or user.lower()=='стоп':
        print('\nостановка программы')
        sys.exit()

while True:
    user = input('\nвведите ссылку сайта: ')
    user2=input('\nвведи название: ')
    n(user)
    sites.append(user)
    nazv.append(user2)
    break
while True:
    choice = questionary.select(
        'выбери категорию, остановка \'stop\'',
        choices=[
            Choice(
                title='ваши сохранненые сайты: ',
                value='sites'

            ),
            Choice(
                title='написать сайт',
                value='write'
            ),
            Choice(
                title='выход из программы',
                value='close'
            ),
        ]

    ).ask()

    if choice == 'sites':
        knopki=[]
        for x in range(len(sites)):
            knopki.append(Choice(title=f'сайт: {nazv[x]} ({sites[x]})', value=sites[x]))
        knopki.append(Choice(title='вернуться в предыдущую категорию', value='back'))
        podmenu = questionary.select(
            'выберите сайт из сохраненных',
            choices = knopki
        ).ask()
        if podmenu=='back':
            continue
        else:
            webbrowser.open(podmenu)
    elif choice== 'close':
        sys.exit()
    elif choice=='write':
        user = input('введите ссылку сайт: ')
        user2 = input('введи назву: ')
        n(user)
        nazv.append(user2)
        sites.append(user)
        print('сайт сохранен')
