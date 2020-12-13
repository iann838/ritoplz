
TROLL_MODE = False

async def get_riot_account_v1_by_puuid(region, puuid):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"

async def get_riot_account_v1_by_riot_id(region, name, tag):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}"

async def get_riot_account_v1_active_shard(region, game, puuid):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}"

async def get_lol_champion_v3_rotation(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/platform/v3/champion-rotations"

async def get_lol_champion_mastery_v4_by_champion_id(region, summoner_id, champion_id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}/by-champion/{champion_id}"

async def get_lol_champion_mastery_v4_all_mastery(region, summoner_id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summoner_id}"

async def get_lol_clash_v1_players(region, summoner_id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/clash/v1/players/by-summoner/{summoner_id}"

async def get_lol_clash_v1_teams(region, id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/clash/v1/teams/{id}"

async def get_lol_clash_v1_tournaments_by_team_id(region, team_id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/clash/v1/tournaments/by-team/{team_id}"

async def get_lol_clash_v1_toutnaments_by_tournament_id(region, id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/clash/v1/tournaments/{id}"

async def get_lol_clash_v1_tournaments_all(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/clash/v1/tournaments"

async def get_lol_league_v4_summoner_entries(region, summoner_id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"

async def get_lol_league_v4_challenger_league(region, queue):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/{queue}"

async def get_lol_league_v4_grandmaster_league(region, queue):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/{queue}"

async def get_lol_league_v4_master_league(region, queue):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/league/v4/masterleagues/by-queue/{queue}"

async def get_lol_league_v4_entries_by_division(region, queue, tier, division):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/league/v4/entries/{queue}/{tier}/{division}"

async def get_lol_league_v4_league_by_league_id(region, id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/league/v4/leagues/{id}"

async def get_lol_status_v4_platform_data(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/status/v4/platform-data"

async def get_lol_match_v4_match(region, id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/match/v4/matches/{id}"

async def get_lol_match_v4_timeline(region, id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/match/v4/timelines/by-match/{id}"

async def get_lol_match_v4_matchlist(region, account_id, query):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}"

async def get_lol_match_v4_tournament_match(region, id, tournament_code):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/match/v4/matches/{id}/by-tournament-code/{tournament_code}"

async def get_lol_match_v4_tournament_matches(region, tournament_code):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/match/v4/matches/by-tournament-code/{tournament_code}/ids",

async def get_lol_spectator_v4_current_game(region, summoner_id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}"

async def get_lol_spectator_v4_featured_games(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/spectator/v4/featured-games"

async def get_lol_summoner_v4_by_name(region, name):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}"

async def get_lol_summoner_v4_by_id(region, id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/{id}"

async def get_lol_summoner_v4_by_account_id(region, account_id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{account_id}"

async def get_lol_summoner_v4_by_puuid(region, puuid):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"

async def get_lol_third_party_code_v4_code(region, summoner_id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/platform/v4/third-party-code/by-summoner/{summoner_id}"

async def post_lol_tournament_v4_codes(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/tournament/v4/codes"

async def get_lol_tournament_v4_codes_by_code(region, code):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/tournament/v4/codes/{code}"

async def put_lol_tournament_v4_codes_by_code(region, code):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/tournament/v4/codes/{code}"

async def get_lol_tournament_v4_lobby_events(region, code):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/tournament/v4/lobby-events/by-code/{code}"

async def post_lol_tournament_v4_providers(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/tournament/v4/providers"

async def post_lol_tournament_v4_tournaments(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/tournament/v4/tournaments"

async def post_lol_tournament_stub_v4_codes(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/tournament-stub/v4/codes"

async def get_lol_tournament_stub_v4_lobby_events(region, code):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/tournament-stub/v4/lobby-events/by-code/{code}"

async def post_lol_tournament_stub_v4_providers(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/tournament-stub/v4/providers"

async def post_lol_tournament_stub_v4_tournaments(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lol/tournament-stub/v4/tournaments"

async def get_tft_league_v1_summoner_entries(region, summoner_id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/tft/league/v1/entries/by-summoner/{summoner_id}"

async def get_tft_league_v1_challenger_league(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/tft/league/v1/challenger"

async def get_tft_league_v1_grandmaster_league(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/tft/league/v1/grandmaster"

async def get_tft_league_v1_master_league(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/tft/league/v1/master"

async def get_tft_league_v1_entries_by_division(region, tier, division):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/tft/league/v1/entries/{tier}/{division}"

async def get_tft_league_v1_league_by_league_id(region, id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/tft/league/v1/leagues/{id}"

async def get_tft_match_v1_matchlist(region, puuid):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids"

async def get_tft_match_v1_match(region, id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/tft/match/v1/matches/{id}"

async def get_tft_summoner_v1_by_name(region, name):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/tft/summoner/v1/summoners/by-name/{name}"

async def get_tft_summoner_v1_by_id(region, id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/tft/summoner/v1/summoners/{id}"

async def get_tft_summoner_v1_by_account_id(region, account_id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/tft/summoner/v1/summoners/by-account/{account_id}"

async def get_tft_summoner_v1_by_puuid(region, puuid):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/{puuid}"

async def get_lor_ranked_v1_leaderboards(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lor/ranked/v1/leaderboards"

async def get_lor_match_v1_matchlist(region, puuid):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lor/match/v1/matches/by-puuid/{puuid}/ids"

async def get_lor_match_v1_match(region, id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lor/match/v1/matches/{id}"

async def get_lor_status_v1_platform_data(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/lor/status/v1/platform-data"

async def get_val_match_v1_match(region, id):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/val/match/v1/matches/{id}"

async def get_val_match_v1_matchlist(region, puuid):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/val/match/v1/matchlists/by-puuid/{puuid}"

async def get_val_match_v1_recent(region, queue):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/val/match/v1/recent-matches/by-queue/{queue}"

async def get_val_content_v1_contents(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/val/content/v1/contents"

async def get_val_status_v1_platform_data(region):
    kwargs = locals()
    endpoint = "https://{region}.api.riotgames.com/val/status/v1/platform-data"
