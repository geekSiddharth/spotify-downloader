import spotipy
import spotipy.util as util

myusername = '217fyj52gog6a4ljqcydluh6y'


def login():
    scope = 'playlist-read-private  playlist-read-collaborative user-follow-read user-library-read user-read-private user-read-recently-played user-top-read user-read-playback-state'
    token = util.prompt_for_user_token(myusername, scope, client_id='016a812198bb4a94b181f8e6bdf3fe5c',
                                       client_secret='cb01fccca5834ead92bd36e007dd2774',
                                       redirect_uri='http://localhost:9988/callback')
    return spotipy.Spotify(auth=token)
