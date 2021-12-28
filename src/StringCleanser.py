import Constants as c
import re


class StringCleanser:
    
    # Strip whitespace, numbers and special characters
    @staticmethod
    def cleanse(s:str):
        s = s.replace(' ', '')
        s = re.sub(c.REGEX_PATTERN, '', s)
        return s
    
    

