import Constants as c
import re


class StringCleanser:
    
    # Strip whitespace, numbers and special characters
    @staticmethod
    def cleanse(s:str):
        """
        @Desc: Strips input string for invalid occurences (whitespace/numbers/specials)
        @Args: s(str): unformatted raw string
        @Returns: s(str): cleansed string

        """

        s = s.replace(' ', '')
        s = re.sub(c.REGEX_PATTERN, '', s)
        return s
    
    

