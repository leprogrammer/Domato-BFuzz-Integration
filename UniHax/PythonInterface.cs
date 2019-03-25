using RGiesecke.DllExport;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;

namespace UniHax
{
    public class PythonInterface
    {
        public static string results;
        public static Mappings xmlData = new Mappings();
        
        public static void FindBestFit(string asciiValue)
        {
            char ascii = asciiValue.ElementAtOrDefault(0);

            List<String> bestFitData = xmlData.GetBestfitMappings(ascii);

            Random rand = new Random();
            int randIndex = rand.Next(0, bestFitData.Count());

            results = bestFitData.ElementAtOrDefault(randIndex);
        }

        public static string GetBestFit()
        {
            return results;
        }

        //[DllExport("normal", CallingConvention = CallingConvention.Cdecl)]
        //public static void GetNormalized(char character, ref object returnedValue)
        //{
        //    Mappings xmlData = new Mappings();
        //    UniChar unicode = new UniChar();
        //    unicode.ConvertCharacterToCodePoint(character);

        //    List<String> normalizedData = xmlData.GetNormalizationMappings(character);

        //    Random rand = new Random();
        //    int size = rand.Next(normalizedData.Count());

        //    returnedValue = new string[] { normalizedData.ElementAtOrDefault(size) };
        //}

        //[DllExport("unicode", CallingConvention = CallingConvention.Cdecl)]
        //public static void GetUnicode(ref object returnedValue)
        //{
        //    Mappings xmlData = new Mappings();

        //    returnedValue = new string[] { xmlData.GetExpandedUnicodeCharacter() };
        //}
    }
}
