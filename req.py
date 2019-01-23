import requests


def get_weather(url):
    result = requests.get(url)
    if result.status_code == 200:
        return result.json()
    else:
        print('Something goes wrong!!!')


if __name__ == '__main__':
    data = get_weather("http://api.openweathermap.org/data/2.5/weather?id=706369&appid=300dd55367b503694f6bfa3ca8bfe0ec&units=metric")
    print(data)


    # "http://api.openweathermap.org/data/2.5/weather?q=khmelnytskyy,UA&appid=300dd55367b503694f6bfa3ca8bfe0ec"