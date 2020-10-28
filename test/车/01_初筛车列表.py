import requests
import pandas as pd


def get_car_infos():
    url = "https://www.dcdapp.com/motor/brand/m/v1/select/series/?city_name=深圳"

    offset = 0
    while True:
        payload = {'offset': offset,
                   'limit': 20,
                   'is_refresh': 0,
                   'series_type': ' 0,1',
                   'price': ' 10,20',
                   'city_name': ' 深圳'}

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38'
        }

        response = requests.post(url, headers=headers, data=payload)
        ret = response.json()
        if not ret["data"]["series"]:
            return
        offset += 1
        yield ret["data"]


def main():
    data = []
    for x in get_car_infos():
        data.extend(x["series"])
    df = pd.DataFrame(data=data)
    df.to_excel("test.xlsx")


if __name__ == '__main__':
    main()
