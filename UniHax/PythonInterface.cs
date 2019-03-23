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

        [DllExport("bestfit", CallingConvention = CallingConvention.StdCall)]
        public static string GetBestFit(char character)
        {
            Mappings xmlData = new Mappings();
            UniChar unicode = new UniChar();
            unicode.ConvertCharacterToCodePoint(character);

            List<String> bestFitData = xmlData.GetBestfitMappings(character);

            Random rand = new Random();
            int size = rand.Next(bestFitData.Count());

            return bestFitData.ElementAtOrDefault(size);
        }

        [DllExport("normal", CallingConvention = CallingConvention.StdCall)]
        public static string GetNormalized(char character)
        {
            Mappings xmlData = new Mappings();
            UniChar unicode = new UniChar();
            unicode.ConvertCharacterToCodePoint(character);

            List<String> normalizedData = xmlData.GetNormalizationMappings(character);

            Random rand = new Random();
            int size = rand.Next(normalizedData.Count());

            return normalizedData.ElementAtOrDefault(size);
        }

        [DllExport("unicode", CallingConvention = CallingConvention.StdCall)]
        public static string GetUnicode(char character)
        {
            Mappings xmlData = new Mappings();
            UniChar unicode = new UniChar();
            unicode.ConvertCharacterToCodePoint(character);

            return xmlData.GetExpandedUnicodeCharacter(character);
        }
    }
}
