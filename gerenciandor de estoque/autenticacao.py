import abc

class Autenticavel(abc.ABC):
    """
    Interface responsável pela autenticação no sistema...
    """

    @abc.abstractmethod
    def autenticacao(self,usuario,senha):
        """
        Método responsável pela autenticação
        :param usuario: nome de usuário
        :param senha: senha de entrada
        :return: booleano, True para permitir login e False para não permitir
        """
        pass
