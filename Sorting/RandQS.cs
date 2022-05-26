/*
Author: Louis Falk Knudsen
Date: 26/05/2022

A WIP attempt at implementing randomised quick-sort, originally based on the
description in Randomized Algorithms by Motwani and Raghavan, and then
iteratively improved upon to match the slightly better (but frankly still
not great) description in Introduction to Algorithms (CLRS).

It works, but is comparatively slow.
*/

using System;

namespace Sorting
{
    public class RandQS
    {
        private static int[] Append(int[] input, int new_entry)
        {
            var new_arr = new int[input.Length + 1];
            for (int i = 0; i < input.Length; i++)
            {
                new_arr[i] = input[i];
            }
            new_arr[input.Length] = new_entry;
            return new_arr;
        }

        // The heart of the algorithm. Recursively splits the array into two parts
        // until arrays have only one element, after which it returns up,
        // assembling a final sorted array.
        public static int[] Sort(int[] input)
        {
            if (input.Length == 0)
            {
                return input;
            }
            var rand = new Random();
            var pivot = rand.Next(0, input.Length);

            var left_arr = Array.Empty<int>();
            var right_arr = Array.Empty<int>();

            // Compares each element to the pivot, assembling two sub-arrays accordingly.
            for (int i = 0; i < input.Length; i++)
            {
                if (i == pivot)
                {
                    continue;
                }
                else if (input[i] < input[pivot])
                {
                    left_arr = Append(left_arr, input[i]);
                }
                else
                {
                    right_arr = Append(right_arr, input[i]);
                }
            }

            // Recursively call the function on the left and right arrays. These will eventually
            // be returned sorted.
            var subtree_left = Sort(left_arr);
            var subtree_right = Sort(right_arr);

            // Copy the left and right arrays, as well as the pivot, into the array which
            // this iteration of the function will return.
            var return_array = new int[subtree_left.Length + 1 + subtree_right.Length];
            subtree_left.CopyTo(return_array, 0);
            return_array[subtree_left.Length] = input[pivot];
            subtree_right.CopyTo(return_array, subtree_left.Length + 1);

            return return_array;
        }

        public static void Test()
        {
            Console.WriteLine("RandQS:");
            var input = new int[] { 30, 4, 111, 4, 9, 20, -8, -17, 5, 22 };
            Console.Write("Before: ");
            Program.PrintArray(input);
            Console.Write("After:  ");
            Program.PrintArray(Sort(input));
        }
    }
}
