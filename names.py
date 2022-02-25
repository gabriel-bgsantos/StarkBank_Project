from random import randint

names = ["Oliver Khan", "Otavio Neto", "CLaudete Edivânia", "Ammarante Douglas", "Rodrigo o Abençoado", "Matheus Cardoso", "Terrance Reker",
"Gabriel Lobato", "Floyd Meio Tempo", "Robert Batman", "Ellie Fernandes", "Peter Park", "MC Rodolfinho Dessa Vez Não Estou Sozinho",
"Kindred Green Poison", "Agnes Evangelista", "Catherine Eduarda", "Mary Namoradeira", "Dorothy Junior", "Helen Santos", "Anna Silva", 
"Maria Eduarda", "Stephanie Rodrigues", "Gloria Miranda", "Randy Skies", "Savarino Santos", "Walter Gonçalves", "Amanda Cavalcante",
"Evelyn Senna", "Susan Boyle", "Harry Potter", "Marjorie Amaral", "Lev Saloio", "Samaritana Neto Quinteiro", "Davy Robalinho Barreira",
"Pietra Dantas", "Davide Varanda", "Amir Lima", "Stephen Malta", "Jennifer Cartaxo", "Nicolae Valcanaia", "Dinarte Trigueiro",
"Maimuna Madruga", "Andriy Neto", "Haniel Toscano", "Liany Póvoas"]

def random_names():
    return names[randint(0, len(names))]
