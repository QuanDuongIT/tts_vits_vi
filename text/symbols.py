# """ from https://github.com/keithito/tacotron """

# """
# Defines the set of symbols used in text input to the model.
# """
# _pad = "_"
# _punctuation = ';:,.!?¡¿—…"«»“” '
# _letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# _letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"


# # Export all symbols:
# symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

# # Special symbol ids
# SPACE_ID = symbols.index(" ")
from viphoneme import syms


# Lọc những symbol KHÔNG nằm trong tập bị loại
filtered_syms = [s for s in syms]

_letters_ipa = ''.join(filtered_syms)

# Export all symbols:
symbols = list(_letters_ipa)

# Special symbol ids
SPACE_ID = symbols.index(" ")
