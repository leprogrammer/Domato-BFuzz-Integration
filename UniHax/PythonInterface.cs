using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace UniHax
{
    class PythonInterface
    {
        private Mappings xmlData;

        public string GetBestFit(char character)
        {
            UniChar unicode = new UniChar();
            unicode.ConvertCharacterToCodePoint(character);

            List<String> bestFitData = xmlData.GetBestfitMappings(character);

            Random rand = new Random();
            int size = rand.Next(bestFitData.Count());

            return bestFitData.ElementAtOrDefault(size);
        }

        public string GetNormalized(char character)
        {
            UniChar unicode = new UniChar();
            unicode.ConvertCharacterToCodePoint(character);

            List<String> normalizedData = xmlData.GetNormalizationMappings(character);

            Random rand = new Random();
            int size = rand.Next(normalizedData.Count());

            return normalizedData.ElementAtOrDefault(size);
        }

        public string GetUnicode(char character)
        {
            UniChar unicode = new UniChar();
            unicode.ConvertCharacterToCodePoint(character);

            return xmlData.GetExpandedUnicodeCharacter(character);
        }
    }
}
