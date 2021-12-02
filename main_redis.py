import redis



def connection():
    """
    Function to connect to server
    """
    connect = redis.Redis(host='localhost', port=6379)

    return connect


def disconnection(connect):
    """
    Function to disconnect from server
    """
    connect.connection_pool.disconnect()


def show_country_details(country):
    """
    Function to list products
    """
    connect = connection()

    try:
        data = connect.keys(pattern=f'{country}')

        if len(data) > 0:
            print('Getting Country...')
            print('-------------------')
            for key in data:
                fetched = connect.hgetall(key)
                print(f"ID: {str(key, 'utf-8', 'ignore')}")
                print(f"Country: {str(fetched[b'Country'], 'utf-8', 'ignore')}")
                print(f"Value: {str(fetched[b'Value'], 'utf-8', 'ignore')}")
                print(f"Year: {str(fetched[b'Year'], 'utf-8', 'ignore')}")
                print('-------------------')
        else:
            print('There are no products registred')
    except redis.exceptions.ConnectionError as e:
        print(f'It was not possible to list the products: {e}')

        disconnection(connect)


def menu():
    """
    Function to generate main menu
    """
    while True:
        print('\nMENU\n')
        print('1) Get country by short code')
        print('5) Exit')
        print('\n')

        try:
            option = int(input('Choose an option: '))

            if option == 1:
                show_country_details(input("Enter Country short code:"))
            elif option == 5:
                print('Exiting...')
                break
            else:
                print('Option not found, try again')
        except ValueError:
            print('Option not found, try again')

if __name__ == '__main__':
    menu()