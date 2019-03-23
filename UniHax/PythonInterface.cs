using RGiesecke.DllExport;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;

namespace UniHax
{
    class PythonInterface
    {
        private Mappings xmlData;

        [DllExport("add", CallingConvention = CallingConvention.StdCall)]
        public string GetBestFit(char character)
        {
            UniChar unicode = new UniChar();
            unicode.ConvertCharacterToCodePoint(character);

            List<String> bestFitData = xmlData.GetBestfitMappings(character);

            Random rand = new Random();
            int size = rand.Next(bestFitData.Count());

            return bestFitData.ElementAtOrDefault(size);
        }

        [DllExport("add", CallingConvention = CallingConvention.StdCall)]
        public string GetNormalized(char character)
        {
            UniChar unicode = new UniChar();
            unicode.ConvertCharacterToCodePoint(character);

            List<String> normalizedData = xmlData.GetNormalizationMappings(character);

            Random rand = new Random();
            int size = rand.Next(normalizedData.Count());

            return normalizedData.ElementAtOrDefault(size);
        }

        [DllExport("add", CallingConvention = CallingConvention.StdCall)]
        public string GetUnicode(char character)
        {
            UniChar unicode = new UniChar();
            unicode.ConvertCharacterToCodePoint(character);

            return xmlData.GetExpandedUnicodeCharacter(character);
        }
    }
}
