from pessoa import Pessoa

class Aluno(Pessoa):

    cursos_oficiais = ['ADM', 'ADS', 'ENG', 'CONT']
    
    def __init__(self, nome, nasc, curso=None):
        super().__init__(nome, nasc)

        if curso == None:
            self._curso = curso
        else:
            if curso in self.cursos_oficiais:
                self._curso = curso
            else:
                raise ValueError(f'O curso {curso} não consta na lista!')
    
#   --------------------------- CURSO ------------------------------
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, curso):
        if isinstance(curso, str):
            if curso in self.cursos_oficiais:
                self._curso = curso
            else:
                raise ValueError(f'O curso {curso} não consta na lista!')
        else:
            raise ValueError('Só se aceita valores strings')
#   -----------------------------------------------------------------

    def add_curso(self, curso):
        if isinstance(curso, str):
            curso = curso.upper()
            (self.cursos_oficiais).append(curso)
        else:
            raise ValueError('Só se aceita valores strings')
