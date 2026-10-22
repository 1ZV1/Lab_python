import requests


class WeatherAPIClient:
    BASE_URL = "https://api.open-meteo.com/v1"

    def __init__(self, timeout: int = 5):
        self.timeout = timeout
        self.session = requests.Session()

    def get_current_weather(self, latitude: float, longitude: float) -> dict:
        params = {"latitude": latitude, "longitude": longitude, "current_weather": "true"}
        res = self.session.get(f"{self.BASE_URL}/forecast", params=params, timeout=self.timeout)
        res.raise_for_status()
        return res.json().get("current_weather", {})


PRESETS = {
    "Москва": "55.7558, 37.6173",
    "Лондон": "51.5074, -0.1278",
    "Минск": "53.9006, 27.5590",
    "Бобруйск": "53.1384, 29.2214",
    "Молодечно": "54.3167, 26.8500",
}

print("Формат: <широта>, <долгота> (через точку: 55.75, 37.61)")
for city, coords in PRESETS.items():
    print(f"  {city}: {coords}")

raw = input("\nВведите координаты: ").strip().replace(",", " ").split()

try:
    if len(raw) != 2:
        raise ValueError("Требуется два числа.")
    lat, lon = float(raw[0]), float(raw[1])
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError("Широта [-90; 90], долгота [-180; 180].")

    weather = WeatherAPIClient().get_current_weather(lat, lon)
    print(f"\nТемпература: {weather.get('temperature')} °C")
    print(f"Ветер: {weather.get('windspeed')} км/ч")
except (ValueError, requests.RequestException) as err:
    print(f"Ошибка: {err}")