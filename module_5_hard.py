import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, video):
        for i in self.videos:
            if video.title not in i.title:
                self.videos.append(video)

    def get_videos(self, search_word):
        for i in self.videos:
            if i.lower() == search_word:
                return self.videos

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if self.current_user.age < 18 and video.adult_mode:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                return
            while video.time_now < video.duration:
                video.time_now += 1
                print(video.time_now)
                time.sleep(1)
            print('Конец видео')
            video.time_now = 0












