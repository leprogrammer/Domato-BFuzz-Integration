#

uBOM = '\uFEFF'

uRLO = '\u202E'

uMVS = "\u180E"

uWordJoiner = "\u2060"

uReservedCodePoint = "\uFEFE"

uNotACharacter = "\uFFFF"

uUnassigned = "\u0FED"

uDEAD = "\uDEAD"

uDAAD = "\uDAAD"

uPrivate = "\uF8FF"

uFullwidthSolidus = "\uFF0F"

uIdnaSs = "\u00DF"

uFDFA = "\uFDFA"

u0390 = "\u0390"

u1F82 = "\u1F82"

uFB2C = "\uFB2C"

def getUnicodeArray():
    x = [u0390, u1F82, uBOM, uDAAD, uDEAD, uFB2C, uFDFA, uFullwidthSolidus, uIdnaSs, uMVS, uNotACharacter, uPrivate, uReservedCodePoint, uRLO, uUnassigned, uWordJoiner]
    return x


def getMalformBytes(character):
    characterBytes = bytearray(character, 'utf-8')

    if len(characterBytes) > 1:
        sliceSize = slice(0, len(characterBytes) - 1)
        result = characterBytes[sliceSize]

        return result.decode("utf-8")
    return characterBytes.decode("utf-8")