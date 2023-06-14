import pygame

class MusicPlayer:
    def __init__(self, playlist):
        self.playlist = playlist

    def play_music(self):
        try:
            pygame.mixer.init()
            pygame.mixer.music.load(self.playlist)
            pygame.mixer.music.play()

            print("Music is playing. Press Ctrl+C to stop.")

            while True:
                continue

        except KeyboardInterrupt:
            pygame.mixer.music.stop()
            print("Music stopped.")

def main():
    playlist = "playlist.mp3"

    player = MusicPlayer(playlist)
    player.play_music()

if __name__ == "__main__":
    main()
