import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
    #
    # def __eq__(self, other):
    #     return self.nickname == other.nickname and self.password == other.password
    #
    # def __hash__(self):
    #     return hash(self.password)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = password
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Вы вошли как {nickname}")
                return
        print("Неверный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                self.log_in(nickname, password)
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        print(f"Пользователь {nickname} успешно зарегистрирован и вошел")
        self.current_user = new_user

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, query):
        results = [video.title for video in self.videos if query.lower() in video.title.lower()]
        return results or "Ничего не найдено"

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title.lower() == title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Воспроизведение видео: {video.title}")
                while video.time_now < video.duration:
                    time.sleep(1)  # Симуляция времени
                    video.time_now += 1
                    print(f"Секунда {video.time_now}/{video.duration}")

                video.time_now = 0
                print("Конец видео")
                return

        print("Видео не найдено")


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')