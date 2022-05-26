/*
Author: Louis Falk Knudsen
Date: 26/05/2022

An implementation of a basic Quick-sort algorithm.
*/

using System;

namespace Sorting
{
    public static class Quicksort
    {
        public static int[] Sort(int[] input, int left, int right)
        {
            if (left < right)
            {
                var pivot = Partition(input, left, right);
                Sort(input, left, pivot - 1);
                Sort(input, pivot + 1, right);
            }
            return input;
        }

        static int Partition(int[] input, int left, int right)
        {
            var pivot_value = input[right];
            var i = left - 1;
            for (var j = left; j <= (right - 1); j++)
            {
                if (input[j] <= pivot_value)
                {
                    i++;
                    (input[i], input[j]) = (input[j], input[i]);
                }
            }
            (input[i + 1], input[right]) = (input[right], input[i + 1]);
            return i + 1;
        }

        public static void Test()
        {
            Console.WriteLine("Quicksort:");
            var inp = new int[] { 30, 4, 111, 4, 9, 20, -8, -17, 5, 22 };
            Console.Write("Before: ");
            Program.PrintArray(inp);
            Console.Write("After:  ");
            Program.PrintArray(Sort(inp, 0, inp.Length - 1));
        }
    }
}