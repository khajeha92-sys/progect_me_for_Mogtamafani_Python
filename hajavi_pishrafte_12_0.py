#IN THE NAME OF GOD
#MADE IN AMIRABAS KHAJEH FOR MR HAJAVI
# CLASS 12

import urllib.request
import urllib.parse


class WebExercises:

    def exercise1(self):
        url = "https://api.example.com/v1/weather?city=Tabriz&days=5&units=metric"

        parsed = urllib.parse.urlparse(url)

        print("\n--- Exercise 1 ---")
        print("Protocol:", parsed.scheme + "://")
        print("Host:", parsed.netloc)
        print("Path:", parsed.path)
        print("Query:", "?" + parsed.query)

        params = urllib.parse.parse_qs(parsed.query)

        print("city =", params["city"][0])
        print("days =", params["days"][0])
        print("units =", params["units"][0])

    def exercise2(self):
        items = {
            "Chrome Browser": "Client",
            "Python Program": "Client",
            "Bank Server": "Server",
            "Weather Server": "Server",
            "Mobile App": "Client",
            "Database Server": "Server"
        }

        print("\n--- Exercise 2 ---")

        for item, type_ in items.items():
            print(item, "->", type_)

    def exercise3(self):
        print("\n--- Exercise 3 ---")
        print("Website is made for humans.")
        print("Web Service is made for programs.")
        print("Website -> Humans")
        print("Web Service -> Programs")

    def exercise4(self):
        params = {
            "city": "New York",
            "country": "USA",
            "days": 7
        }

        query_string = urllib.parse.urlencode(params)

        print("\n--- Exercise 4 ---")
        print(query_string)
        print("Space in New York is converted to +")

    def exercise5(self):
        url = "https://jsonplaceholder.typicode.com/posts/1"

        print("\n--- Exercise 5 ---")

        response = urllib.request.urlopen(url)

        data = response.read()
        data_str = data.decode()

        print(data_str)

        response.close()

    def exercise6(self):
        base_url = "https://geocoding-api.open-meteo.com/v1/search"

        print("\n--- Exercise 6 ---")

        city = input("Enter city name: ")

        params = {
            "name": city
        }

        query_string = urllib.parse.urlencode(params)

        full_url = base_url + "?" + query_string

        print("Sending request to:", full_url)

        response = urllib.request.urlopen(full_url)

        data = response.read()
        data_str = data.decode()

        print("Response received!")
        print(data_str)

        response.close()

###deriver code###
def main():
    program = WebExercises()

    program.exercise1()
    program.exercise2()
    program.exercise3()
    program.exercise4()
    program.exercise5()    
    program.exercise6()
    print('THE END')

main()
print('\n MADE IN AMIRABAS KHAJEH')

