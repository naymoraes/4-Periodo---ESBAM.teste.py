import requests
import pytest

# API URLs e tokens
BASE_URL_POKEMON = "https://pokeapi.co/api/v2/pokemon"
BASE_URL_SPOTIFY = "https://api.spotify.com/v1/artists/3fMbdgQpXoY4w3v1t3lWlS/top-tracks"
BASE_URL_TMDB = "https://api.themoviedb.org/3/discover/tv"
BASE_URL_DOG = "https://api.thedogapi.com/v1/breeds"
BASE_URL_EDAMAM = "https://api.edamam.com/api/recipes/v2"

# API Tokens e Chaves
AUTH_TOKEN_SPOTIFY = "YOUR_SPOTIFY_AUTH_TOKEN"  # Meu token de acesso do Spotify (substituir pelo meu token)
API_KEY_TMDB = "YOUR_TMDB_API_KEY"  # Minha chave de API do TMDB (substituir pela minha chave)
API_KEY_DOG = "YOUR_DOG_API_KEY"  # Minha chave de API para o The Dog (substituir pela minha chave)
APP_ID_EDAMAM = "YOUR_APP_ID"  # Meu App ID para a API Edamam (substituir pelo meu ID)
APP_KEY_EDAMAM = "YOUR_APP_KEY"  # Minha App Key para a API Edamam (substituir pela minha key)


# Funções para testes

# TESTE 1 - API Pokémon
def test_pokemon_success():
    
# Testa se é possível acessar dados de um Pokémon específico usando a PokeAPI.
# Verifica se a resposta contém o nome do Pokémon "ditto" e se o status da resposta é 200 (sucesso).

    response = requests.get(f"{BASE_URL_POKEMON}/ditto")
    if response.status_code == 200:
        data = response.json()
        print("Pokémon:", data["name"])
        assert "name" in data and data["name"] == "ditto"
    else:
        print("Erro ao acessar a PokeAPI:", response.status_code)

# TESTE 2 - Spotify: Anitta A MAIOR :)
def test_spotify_top_tracks():
    
    # Testa se é possível recuperar as principais faixas de um artista (Anitta) usando a API do Spotify.
    # O teste verifica se a resposta contém uma lista  de faixas e se o status da resposta é 200 (sucesso).
    
    headers = {"Authorization": f"Bearer {AUTH_TOKEN_SPOTIFY}"}
    response = requests.get(f"{BASE_URL_SPOTIFY}?market=US", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("Top Tracks de Anitta:", [track["name"] for track in data["tracks"]])
        assert "tracks" in data and len(data["tracks"]) > 0
    else:
        print("Erro ao acessar a API do Spotify:", response.status_code)

# TESTE 3 - TMDB: Séries de Suspense
def test_series_success():
    
    # Testa se é possível recuperar séries de suspense usando a API TMDB.
    # Verifica se a resposta contém uma lista de resultados com pelo menos uma série 
    # e se o status da resposta é 200 (sucesso).
    
    response = requests.get(f"{BASE_URL_TMDB}?api_key={API_KEY_TMDB}&with_genres=80")
    if response.status_code == 200:
        data = response.json()
        print("Séries de Suspense:", [series["name"] for series in data["results"]])
        assert "results" in data and len(data["results"]) > 0
    else:
        print("Erro ao acessar a API TMDB:", response.status_code)

# TESTE 4 - The Dog API: Raças de Cães
def test_dogs_success():

    # Testa se é possível recuperar uma lista de raças de cães usando a The Dog API. 
    # Verifica se a resposta contém uma lista com pelo menos uma raça e se o status  da resposta é 200 (sucesso).
    
    headers = {"x-api-key": API_KEY_DOG}
    response = requests.get(f"{BASE_URL_DOG}", headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("Raças de Cães:", [breed["name"] for breed in data])
        assert len(data) > 0
    else:
        print("Erro ao acessar a API do Dog:", response.status_code)

# TESTE 5 - Edamam: Receitas
def test_recipes_success():
    
    # Testa se é possível buscar receitas com o ingrediente 'frango' usando a API Edamam. 
    # Verifica se a resposta contém uma lista de receitas com pelo menos um item e se o  status da resposta é 200 (sucesso).
    
    params = {
        "q": "chicken",
        "app_id": APP_ID_EDAMAM,
        "app_key": APP_KEY_EDAMAM
    }
    response = requests.get(f"{BASE_URL_EDAMAM}", params=params)
    if response.status_code == 200:
        data = response.json()
        print("Receitas com Frango:", [recipe["label"] for recipe in data["hits"]])
        assert "hits" in data and len(data["hits"]) > 0
    else:
        print("Erro ao acessar a API Edamam:", response.status_code)

# Execução dos testes
def run_tests():
    print("\nTestando a API Pokémon...")
    test_pokemon_success()
    
    print("\nTestando a API Spotify (Anitta)...")
    test_spotify_top_tracks()

    print("\nTestando a API TMDB (Séries de Suspense)...")
    test_series_success()

    print("\nTestando a API The Dog (Raças de Cães)...")
    test_dogs_success()

    print("\nTestando a API Edamam (Receitas)...")
    test_recipes_success()

if __name__ == "__main__":
    run_tests()
