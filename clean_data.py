import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

def clean_and_geocode_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df.dropna(subset=["adresse"], inplace=True)

    geolocator = Nominatim(user_agent="coworking_map_app")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

    latitudes = []
    longitudes = []

    for addr in df["adresse"]:
        try:
            location = geocode(addr)
            if location:
                latitudes.append(location.latitude)
                longitudes.append(location.longitude)
                print(f"✅ {addr} → {location.latitude}, {location.longitude}")
            else:
                latitudes.append(None)
                longitudes.append(None)
                print(f"⚠️ Adresse non trouvée : {addr}")
        except Exception as e:
            latitudes.append(None)
            longitudes.append(None)
            print(f"❌ Erreur pour {addr} : {e}")

    df["latitude"] = latitudes
    df["longitude"] = longitudes

    df.dropna(subset=["latitude", "longitude"], inplace=True)
    df.to_csv(output_file, index=False)
    print(f"\n✅ Fichier enrichi avec géocodage : {output_file}")

if __name__ == "__main__":
    clean_and_geocode_data("coworking_data_pandas.csv", "coworking_data.csv")
