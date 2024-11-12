# Objetivo Geral:
Desenvolver e automatizar testes para verificar a funcionalidade de diversas APIs (Pokémon, Spotify,
TMDB, The Dog e Edamam) utilizando pytest, garantindo a validade das respostas e a 
robustez das integrações.

# Descrição das APIs

#  1. Pokémon API (PokeAPI)
A PokeAPI fornece acesso a informações sobre Pokémon. Neste projeto, o teste verifica se é
 possível acessar dados sobre um Pokémon específico, como o nome "Ditto".

- Endpoint: (https://pokeapi.co/api/v2/pokemon/)
- Teste: Verifica se o nome do Pokémon retornado é "ditto".

# 2. Spotify API
A API do Spotify fornece acesso a informações sobre músicas e artistas. Este teste busca as
 faixas mais populares de Anitta.

- Endpoint:(https://api.spotify.com/v1/artists/{artist_id}/top-tracks)
- Teste: Verifica se é possível obter as principais faixas de Anitta.

# 3. **TMDB API**
O TMDB (The Movie Database) fornece informações sobre filmes e séries. O teste busca séries de
 suspense utilizando o gênero de ID 80.

- Endpoint: (https://api.themoviedb.org/3/discover/tv)
- Teste: Verifica se é possível listar séries de suspense.

# 4. The Dog API
A The Dog API fornece informações sobre raças de cães. O teste verifica se é possível 
obter uma lista de raças de cães.

- Endpoint: (https://api.thedogapi.com/v1/breeds)
- **Teste:** Verifica se há pelo menos uma raça de cão na resposta.

# 5. Edamam API
A Edamam API oferece dados sobre receitas de alimentos. O teste verifica se é possível
 buscar receitas que utilizem "frango" como ingrediente principal.

- Endpoint: (https://api.edamam.com/api/recipes/v2)
- Teste: Verifica se há receitas com o ingrediente "frango".

## Requisitos

Este projeto foi desenvolvido utilizando Python 3.x. As dependências necessárias estão
 listadas no arquivo (requirements.txt).

# Instalei as dependências

- pip install -r requirements.txt

# Para rodar os testes, execute:

- pytest

# Estrutura do Projeto
- api_test.py: Arquivo contendo os testes para as APIs.
- requirements.txt: Arquivo contendo as dependências necessárias.
- README.md: Este arquivo de instruções.


# requirements.txt:

Este arquivo lista as dependências do projeto, que são as bibliotecas
 necessárias para rodar os testes:

- requests==2.28.1
- pytest==7.2.2

