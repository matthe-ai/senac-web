class AnimalDAO:
    def criar_tabela(self):
        self.cursor.execute('''
                CREATE TABLE animais ( #primeiro erro é que ele sempre vai criar uma tabela chamada animais (mesmo já existindo uma com esse nome)
                            nome TEXT, #segundo erro é deixar que esses campos fiquem vazios
                            especie TEXT
                            )
                        ''')