from traductor.translators.base import BaseTranslator

class ContainerName(BaseTranslator):
    """

    """
    def translate(self, value):
        """
        :param value:
        :return:
        """
        if not value:
            return ""

        return "--name=%s" % value