import pygame


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((160, 160))
done = False
clock = pygame.time.Clock()
_songs = ['./songs/Jumpsuit.mp3', './songs/Bandito.mp3', './songs/Morph.mp3']
SONG_END = pygame.USEREVENT + 1
_currently_playing_song = None

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
def play_previous_song():
    global _songs
    pygame.mixer.music.load(_songs[-1])
    pygame.mixer.music.play()
pygame.mixer.music.load('./songs/Jumpsuit.mp3')
pygame.mixer.music.play(0, start=1, fade_ms = 0)
pygame.mixer.music.set_volume(0.2)   
pygame.mixer.music.set_endevent(SONG_END)
while not done:
    pressed = pygame.key.get_pressed()
    pause = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == SONG_END:
            print("the song ended!")
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
            elif event.key == pygame.K_k:
                pygame.mixer.music.load('./songs/Jumpsuit.mp3')
                pygame.mixer.music.play(0, start=1, fade_ms = 0)
            elif event.key == pygame.K_l:
                play_next_song()
            elif event.key == pygame.K_j:
                play_previous_song()
    pygame.display.flip()