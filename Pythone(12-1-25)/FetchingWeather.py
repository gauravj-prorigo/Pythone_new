import requests

class weatherdetails:
    
    def __init__(self,city):
        self.city = city
        
    def display(self):
        try:  
          response = requests.get(f'https://api.weatherapi.com/v1/current.json?key=556769fc1cee4f978b9175318250712&q=${self.city}&aqi=no')
          data = response.json() 
          print(f"The Temprature of {data['location']['name']} city is {data['current']['temp_c']}")
          
        except Exception as e: 
            print("Something went wrong ",e)  
            
    def validation(self):
         if(len(self.city) == 0):
             print("Enter valid city name")
             return
         else:
             self.display() 
             
          
cityname = input("Enter city name : ")          
W = weatherdetails(cityname)  
W.validation()     