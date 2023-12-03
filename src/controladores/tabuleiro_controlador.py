from modelos.tabuleiro import Tabuleiro
from controladores.embarcacao_controlador import EmbarcacoesControlador

class TabuleiroControlador():

    @classmethod
    def pegar_tabuleiro_por_parte(self, tabuleiro: Tabuleiro, parte_tabuleiro: str):
        tabuleiro_parte = tabuleiro.devolver_tabuleiro_por_parte(parte_tabuleiro)
        representacao = []
        for linha in tabuleiro_parte:
           representacao.append(''.join(linha)) 
        return representacao
    
    #Criando embarcacoes pro tabuleiro
    @classmethod
    def definir_embarcacoes_para_colocar(cls, tabuleiro: Tabuleiro):
        lista : list = EmbarcacoesControlador.criar_embarcacoes()
        tabuleiro.definir_embarcacoes_tabuleiro(lista)
    
    @classmethod
    def listar_embarcacoes_para_colocar(cls, tabuleiro: Tabuleiro, parte_tabuleiro: str):
        return tabuleiro.delvover_embarcacoes_por_parte(parte_tabuleiro)
    
    @classmethod
    def pegar_embarcacao_para_colocar_por_nome(cls, tabuleiro: Tabuleiro, parte_tabuleiro: str, nome_embarcacao: str):
        embarcacoes_para_colocar = cls.listar_embarcacoes_para_colocar(tabuleiro, parte_tabuleiro)
        embarcacao = None

        for e in embarcacoes_para_colocar:
            if e['nome'] == nome_embarcacao:
                embarcacao = e

        if (embarcacao != None):
            return embarcacao
        return False
    
    @classmethod
    def definir_embarcacao_viva_na_parte(cls, tabuleiro: Tabuleiro, parte_tabuleiro: str, embarcacao: object):
        tabuleiro.definir_embarcacao_viva_na_parte(embarcacao, parte_tabuleiro)
        
    # Colocando embarcacoes no tabuleiro             
    # @classmethod
    # def colocar_embarcacoes_no_tabuleiro(cls, tabuleiro: Tabuleiro, parte_tabuleiro: str, nome_embarcacao: str, coord_x: int, coord_y: int, orientacao: str):
        
    #     if not(0 <= coord_x < 10 and 0 <= coord_y < 10):
    #         raise ValueError('Coordenadas invalidas')
        
    #     embarcacao = cls.pegar_embarcacao_para_colocar_por_nome(tabuleiro, parte_tabuleiro, nome_embarcacao)
        
    #     for i in range(tabuleiro.definir_embarcacao_viva_na_parte[embarcacao]):
    #         if orientacao == 'horizontal':
    #             if coord_y + i >= 10 or tabuleiro.devolver_tabuleiro_por_parte(parte_tabuleiro)[coord_x][coord_y + i] != 'X':
    #                 raise ValueError('Outra embarcação aqui irmão')
    #             tabuleiro.devolver_tabuleiro_por_parte(parte_tabuleiro)[coord_x][coord_y + i] = embarcacao
    #         elif orientacao == 'vertical':
    #             if coord_x + i >= 10 or tabuleiro.devolver_tabuleiro_por_parte(parte_tabuleiro)[coord_x + i][coord_y] != 'X':
    #                 raise ValueError('Outra embarcação aqui irmão')
    #             tabuleiro.devolver_tabuleiro_por_parte(parte_tabuleiro)[coord_x + i][coord_y] = embarcacao
    #         else:
    #             raise ValueError('Orientação errada')
        
        
    # @classmethod
    # def checar_espaco(cls, linha, coluna):
    #     return linha + coluna

    # @classmethod
    # def sobreposicao_embarcacao(cls, linha, coluna):
    #     try:
    #         if not cls.get_instance().checar_espaco(linha, coluna):
    #             return True  
    # # Embarcação não cabe no tabuleiro
    #         for i in range(10):
    #             coord_x = chr(ord('A') + linha)
    #             coord_y = coluna + i
    # # Coordenadas fora dos limites
    #             if coord_x not in cls.get_instance()._tabuleiro._parte_a._dict_alphanum or coord_y >= len(cls.get_instance()._tabuleiro._parte_a._matrix[0]):
    #                 return True 
    # # Navio sobrepondo navio
    #             if cls.get_instance()._tabuleiro._parte_a.get_quadrante(coord_x, coord_y) != 'X':
    #                 return True 
    # # Índicie fora dos limites do tabuleiro
    #     except IndexError:
    #         return True
    #     return False