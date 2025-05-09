self.cursor.execute("INSERT INTO alunos (nome,idade) VALUES (?,?)","Carlos",18)
# O erro está nos itens fornecidos que deveriam estar entre parenteses ficando:
self.cursor.execute("INSERT INTO alunos (nome,idade) VALUES (?,?)",("Carlos",18))