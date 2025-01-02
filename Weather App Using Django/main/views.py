from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        
        try:
            # source contain JSON data from API
            source = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=a5bd156fe0c39483983642105476075d'
            ).read()

            # converting JSON data to a dictionary
            list_of_data = json.loads(source)

            # data for variable list_of_data
            data = {
                "country_code": str(list_of_data['sys']['country']),
                "city": str(list_of_data['name']),
                "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + 'k',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            }
        except urllib.error.HTTPError as e:
            if e.code == 404:
                data = {
                    "error": "City not found"
                }
            else:
                data = {
                    "error": "An error occurred"
                }
        except Exception as e:
            data = {
                "error": "An error occurred"
            }
    else:
        data = {}
    return render(request, "main/index.html", data)
