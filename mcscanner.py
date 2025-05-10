import requests


def java():
    url = 'https://api.mcsrvstat.us/3/'
    platform = 'java'

    try:
        server = input(f'Server Address: \n > ').strip() or 'Please enter a server'
        print(server)
        if server == str('Please enter a server'):
            exit()
    except KeyboardInterrupt:
        exit()

    try:
        r = requests.get(f'{url}{server}')

        if r.status_code == 200 and r.json()['online']:
            data = r.json()

            hostname = data.get('hostname')
            ip = data.get('ip')
            port = data.get('port')
            version = data.get('protocol', {}).get('name')
            protocol = data.get('protocol', {}).get('version')
            online = data.get('players', {}).get('online')
            svr_max = data.get('players', {}).get('max')
            pl = data.get('players', {}).get('list')

            print(f'PLATFORM: {platform}')
            print(f'HOSTNAME: {hostname}')
            print(f'IP:PORT: {ip}:{port}')
            print(f'VERSION: {version}')
            print(f'PROTOCOL: {protocol}')
            print(f'ONLINE PLAYERS: {online}/{svr_max}')
            print(f'PLAYER LIST:')
            if pl is not None:
                for player in pl:
                    name = player['name']
                    uuid = player['uuid']
                    print(f'{name:16} UUID: {uuid}')
                print(f'')
            else:
                print(f'no players found\n')
        else:
            print(f'java server not found\n')
    except KeyboardInterrupt:
        exit()

def banner():
    print(f'                                                            ')
    print(f'⠀⠀⡰⠉⠉⣷⡄⣀⣎⠉⢹⡎⠉⢉⡞⠉⠉⣧⡎⠉⠉⡞⠉⠉⠉⠉⠉⣿⠉⠉⠉⠉⠉⢹⡏⠋⠉⠉⠉⠙⡏⠉⣉⠉⣉⠉⢿⠉⠉⠉⢉⠉⢱⡏⠉⠉⠉⢉⠉⡄')
    print(f'⠀⢀⠃⠀⠀⠘⠛⠁⠀⠀⣼⠀⠀⣸⠃⠀⠀⠘⠃⠀⢰⡇⠀⠀⠛⠛⠛⣿⠀⠀⢸⣿⣿⣿⡇⠀⠈⠃⠀⣠⣿⠀⠉⣶⣍⠀⢸⡆⠀⠘⠛⠛⠛⣿⣿⡆⠀⠈⡟⠁')
    print(f'⠀⡜⣀⢀⣶⣀⣰⠆⠀⢀⡏⠀⠀⣿⠀⠀⣸⣄⠤⠄⢸⠃⠀⢰⣶⣶⣶⣿⠀⠀⢸⣉⣉⣉⡇⡀⠀⣶⠀⠀⢹⠀⠀⢀⡀⢀⠀⣇⠀⠀⢶⣶⣶⢾⣿⣿⡀⠀⢱⠀')
    print(f'⢰⠀⠀⢸⣿⣦⠈⠀⠀⢼⠁⠀⢰⡇⠀⠀⣿⣿⠀⠀⢼⠀⡄⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⢸⡇⠂⠀⣿⠀⠀⢸⡆⠀⢘⡧⠀⠀⣿⠀⠀⢸⠛⠃⠘⣿⣿⡇⠀⠀⡆')
    print(f' ⠑⢤⣀⣙⡿⠉⠱⣄⣠⣷⣄⣀⣹⣄⣀⣘⡏⢆⣀⣘⣧⣀⣀⣀⣀⣀⣿⣀⣀⣀⣀⣀⣸⣇⣀⣰⣏⣀⣠⣿⣀⣀⣾⣁⣀⣴⣋⣀⡠⠃⠀⠀⠀⢿⣋⣀⡤⠋⠀')
    print(f'                                            (server)scanner)')
    print(f'                    Github[xorsirenz]                       ')


def main():
    banner()
    java()


if __name__ == '__main__':
    main()
