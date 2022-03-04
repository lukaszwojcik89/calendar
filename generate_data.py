from random import randint, choice
from pprint import pprint as pp
import json
from app import Event


class GenerateData:
    def __init__(self):
        self.title = ['piwo', 'wino', 'wodka']
        self.location = ['amsterdam', 'berlin', 'warszawa']
        self.users = ['ala', 'ola', 'ela', 'ula', 'roman']

    @staticmethod
    def _start_time_generator():
        return f'{randint(1, 28)}-{randint(2, 12)}-{randint(2022, 2050)} {randint(0, 23)}:{randint(0, 59)}'

    def generate(self, amount, path):
        temp = []

        for i in range(amount):
            temp.append({
                "title": choice(self.title),
                "location": choice(self.location),
                "start_time": str(self._start_time_generator()),
                "duration": randint(15, 599),
                "owner": choice(self.users),
                "participants": [choice(self.users) for _ in range(randint(1, len(self.users) - 1))]
            })

            # 	choice(self.title),
            # 	choice(self.location),
            # 	str(self._start_time_generator()),
            # 	str(randint(15, 599)),
            # 	choice(self.users),
            # 	', '.join([choice(self.users) for _ in range(randint(1, len(self.users) - 1))])
        # pp(temp) - pretty print
        with open(path, 'w', encoding='UTF-8') as file:
            # file.writelines([', '.join(x) + '\n' for x in temp]) - to jest bez jsona
            json.dump(temp, file)

    @staticmethod
    def load(path):
        with open (path, 'r') as file:
            pp(json.load(file))

    def __repr__(self):
        attrs = ', '.join(f'{k if k[0] != "_" else k[1:]}={v}' for k, v in self.__dict__.items())
        return f"{type(self).__name__}({attrs})"




# # g = GenerateData()
# # g.generate(30)

# GenerateData.load()

