# Test Strings Cases that should fail automatically
FAIL_TEST_CASES = {
    'EMPTY_STRING': '',
    'NONE_VAL': None,
    'WHITESPACE': '           ',
    'ALL_NUMBERS': '78346029274101149780279646769884535398028238924614',
    'ALL_SPECIALS': '*(^%*(%^#&@()%&#&*@#&%&@#%(*@#^-==-={{_)_!*@#&#@|',
    'SPECIALS_NUMBERS': '*#*35!(@(&$54#18346372435^#!^($61346',
    'ONE_CHAR': 'A',
    'ONE_CHAR_WHITESPACE': '     Z     '
}

# Test String Edited from Assignment to include invalid characters to test StringCleanser
PASS_TEST_CASES = {
    'TEST_MIXED': '   6!*$)@%@$A      BCB  AH5ELL+_(#&@%#)+}{|:"<>>54654O  HOW#@%#%RACECA{><}{:?"RAREYO&#)*%*)UILO3_*$":+($@*VEUE 35335VOL IIA@#%#%MAIDOIN -7-GGOOD@^&$^$ &*# ^36796^ @& $           '
}
