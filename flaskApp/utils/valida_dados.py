import re

class ValidaDados:

    @staticmethod
    def eh_telefone(str_numero):
        flag = False
        try:
            pattern = r"\(\d{2}\)\d{4,5}-\d{4}"
            flag = bool(re.fullmatch(pattern, str_numero))
        except Exception as e:
            print(e)
        return flag