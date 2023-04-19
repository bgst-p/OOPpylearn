class Player:  # encapsulation
    name = 'joni'
    _salary = 5000  # protected
    __salary = 3000  # private

    def get_salary(self):
        return self._salary, self.__salary


player = Player()
player.name = "jarwo"
player.__salary = 40000  # private baru diluar class

print(player.name)
print(player.get_salary())
print(player.__salary)
