

from operator import length_hint
from turtle import position
import discord
import os
from dotenv import load_dotenv
load_dotenv()
import requests
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('$ayuda'):
        await message.channel.send('''Para saber los datos de un jugador ingrese con Nombre y Apellido el siguiente comando:
Ejemplo -> $mlb miguel cabrera
Para saber los detalles de un Jugador copie el ID del jugador e ingrese el siguiente comando: 
Ejemplo -> $detalles 'XXXXXX' <- pegar el ID
Para saber las Estadisticas de un jugador por año ingrese el siguiente comando:
$estadisticas 'ID' 'AÑO' 
Para saber las Estadisticas de por vida de u jugador ingrese el siguiente comando:
$carrera 'ID' ''')
    if message.content.startswith('$mlb'):
        name_player = message.content.split(' ')[1]
        last_name_player = message.content.split(' ')[2]
        search_player = requests.get(f"http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?sport_code='mlb'&active_sw='Y'&name_part='{name_player} {last_name_player}%25'")
        response = search_player.json()
        player_filter_name = response['search_player_all']['queryResults']['row']['name_display_first_last']
        position = response['search_player_all']['queryResults']['row']['position']
        pais_natal = response['search_player_all']['queryResults']['row']['birth_country']
        bateo = response['search_player_all']['queryResults']['row']['bats']
        lanza = response['search_player_all']['queryResults']['row']['throws']
        team_full = response['search_player_all']['queryResults']['row']['team_full']
        team_abrev = response['search_player_all']['queryResults']['row']['team_abbrev']
        player_id = response['search_player_all']['queryResults']['row']['player_id']
        liga = response['search_player_all']['queryResults']['row']['league']
        await message.channel.send(f'''{player_filter_name}. 
Posicion: {position}.
Pais Natal: {pais_natal}.
Bateo/Lanz. : {bateo}, {lanza}.
Equipo Actual: {team_full}, {team_abrev}.
Liga: {liga}.
-------------
Copie el ID -> {player_id}
Si quiere saber los detalles de un jugador:
ingrese el siguiente comando: $detalles 'ID'
Si quiere saber las estadisticas del jugador por año:
ingrese el siguiente comando: $estadisticas 'AQUI ID' 'AQUI AÑO'.
Si quiere saber la estadisticas del jugador de por vida:
ingrese l siguiente comando: $carrera 'AQUI ID'
  ''')
        print(player_filter_name, position, pais_natal,bateo,lanza,team_full,team_abrev)




    if message.content.startswith('$estadisticas'):
             id_jugador = message.content.split(' ')[1]
             year_season = message.content.split(' ')[2]
             #search_id = requests.get(f"http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='{id_jugador}'")
             search_id = requests.get(f" http://lookup-service-prod.mlb.com/json/named.sport_hitting_tm.bam?league_list_id='mlb'&game_type='R'&season='{year_season}'&player_id='{id_jugador}'")
             datos_id = search_id.json()
             avg = datos_id['sport_hitting_tm']['queryResults']['row']['avg']
             hits = datos_id['sport_hitting_tm']['queryResults']['row']['h']
             hr = datos_id['sport_hitting_tm']['queryResults']['row']['hr']
             rbi = datos_id['sport_hitting_tm']['queryResults']['row']['rbi']
             xbh = datos_id['sport_hitting_tm']['queryResults']['row']['xbh']
             bb = datos_id['sport_hitting_tm']['queryResults']['row']['bb']
             sb = datos_id['sport_hitting_tm']['queryResults']['row']['sb']
             ab = datos_id['sport_hitting_tm']['queryResults']['row']['ab']
             jugador_id = datos_id['sport_hitting_tm']['queryResults']['row']['player_id']
             obp = datos_id['sport_hitting_tm']['queryResults']['row']['obp']
             print(avg,hits,hr,rbi,xbh,bb,sb,ab)
             await message.channel.send(f'''Average: {avg}
Hits: {hits}.
Home Runs: {hr}.
Promedio para enbasarse: {obp}
Carreras Impulsadas: {rbi}.
Extras Bases: {xbh}.
Base Por Bolas: {bb}.
Bases Robadas: {sb}.
Turnos Al Bate: {ab}.
-------------
Copie el ID -> {jugador_id}
Si quiere saber los detalles de un jugador:
ingrese el siguiente comando: $detalles 'ID'
Si quiere saber las estadisticas del jugador por año:
ingrese el siguiente comando: $estadisticas 'AQUI ID' 'AQUI AÑO'.
Si quiere saber la estadisticas del jugador de por vida:
ingrese el siguiente comando: $carrera 'AQUI ID'. ''')

        
    if message.content.startswith('$carrera'):
             id_jugador = message.content.split(' ')[1]
             #search_id = requests.get(f"http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='{id_jugador}'")
             vida_id = requests.get(f"http://lookup-service-prod.mlb.com/json/named.sport_career_hitting.bam?league_list_id='mlb'&game_type='R'&player_id='{id_jugador}'")
             datos_id = vida_id.json()
             avg = datos_id['sport_career_hitting']['queryResults']['row']['avg']
             hr = datos_id['sport_career_hitting']['queryResults']['row']['hr']
             hits = datos_id['sport_career_hitting']['queryResults']['row']['h']
             carreras_a = datos_id['sport_career_hitting']['queryResults']['row']['r']
             rbi = datos_id['sport_career_hitting']['queryResults']['row']['rbi']
             xbh = datos_id['sport_career_hitting']['queryResults']['row']['xbh']
             juegos_j = datos_id['sport_career_hitting']['queryResults']['row']['g']
             sb = datos_id['sport_career_hitting']['queryResults']['row']['sb']
             al_bate = datos_id['sport_career_hitting']['queryResults']['row']['ab']
             bb = datos_id['sport_career_hitting']['queryResults']['row']['bb']
             ponches = datos_id['sport_career_hitting']['queryResults']['row']['so']
             obp = datos_id['sport_career_hitting']['queryResults']['row']['obp']
             player_id = datos_id['sport_career_hitting']['queryResults']['row']['player_id']
             print()
             await message.channel.send(f'''Average: {avg}
Hits: {hits}
Extras Bases: {xbh}
Home Runs: {hr}
Promedio para enbasarse: {obp}
Carreras Anotadas: {carreras_a}
Carreras Impulsadas: {rbi}
Juegos Jugados: {juegos_j}
Bases Robadas: {sb}
Turnos al bate: {al_bate}
Base por Bolas: {bb}
Ponches: {ponches}
-------------
Copie el ID -> {player_id}
Si quiere saber los detalles de un jugador:
ingrese el siguiente comando: $detalles 'ID'
Si quiere saber las estadisticas del jugador por año:
ingrese el siguiente comando: $estadisticas 'AQUI ID' 'AQUI AÑO'.
Si quiere saber la estadisticas del jugador de por vida:
ingrese l siguiente comando: $carrera 'AQUI ID'
''')   
    if message.content.startswith('$detalles'):
        id_jugador = message.content.split(' ')[1]
        filter_id = requests.get(f"http://lookup-service-prod.mlb.com/json/named.player_info.bam?sport_code='mlb'&player_id='{id_jugador}'")
        details_id = filter_id.json()
        fecha_naci = details_id['player_info']['queryResults']['row']['birth_date']
        edad = details_id['player_info']['queryResults']['row']['age']
        apodo = details_id['player_info']['queryResults']['row']['name_nick']
        jersey = details_id['player_info']['queryResults']['row']['jersey_number']
        id_player = details_id['player_info']['queryResults']['row']['player_id']
        await message.channel.send(f''' Fecha de Nacimiento: {fecha_naci}
Edad: {edad}
Apodo: {apodo}
Num.Dorsal: {jersey}
-------------
Copie el ID -> {id_player}
Si quiere saber los detalles de un jugador:
ingrese el siguiente comando: $detalles 'ID'
Si quiere saber las estadisticas del jugador por año:
ingrese el siguiente comando: $estadisticas 'AQUI ID' 'AQUI AÑO'.
Si quiere saber la estadisticas del jugador de por vida:
ingrese l siguiente comando: $carrera 'AQUI ID'
''')

client.run(os.environ['TOKEN'])