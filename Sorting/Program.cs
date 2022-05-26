/*
Author: Louis Falk Knudsen
Date: 26/05/2022

The entry point for the sorting algorithms, testing all of them at once.
*/

using System;

namespace Sorting
{
    public class Program
    {
        public static void PrintArray(int[] input)
        {
            for (int i = 0; i < input.Length; i++)
            {
                Console.Write(input[i] + " ");
            }
            Console.WriteLine();
        }

        static void Main(string[] args)
        {
            RandQS.Test();
            Quicksort.Test();
            Random_Quicksort.Test();
        }
    }
}
