/*
Author: Louis Falk Knudsen
Date: 25/05/2022

A Random Quick-Sort implementation based on the short description from the introduction of
Randomized Algorithms by Motwani and Raghavan.

I still find recursive functions quite difficult to "visualise" in my head. I tend to prefer
nested loops, when given the option.
*/

using System;

namespace Sorting
{
    class RandQS
    {
        // Helper function for printing the final output array.
        static void PrintArray(Node[] input)
        {
            for (int i = 0; i < input.Length; i++)
            {
                Console.Write(input[i].value + " ");
            }
            Console.WriteLine();
        }

        // The individual entry. On the left are elements that have smaller values,
        // on the right are the remaining. At the end, each array will have only
        // one element.
        class Node
        {
            public int value;
            public Node parent = null;
            public Node[] left = null;
            public Node[] right = null;
        }

        // Adds a new Node element to the end of a Node array.
        static Node[] Append(Node[] input, Node new_node)
        {
            var output = new Node[input.Length + 1];
            for (int i = 0; i < input.Length; i++)
            {
                output[i] = input[i];
            }
            output[input.Length] = new_node;
            return output;
        }

        // The heart of the algorithm. Recursively splits the array into two parts
        // until arrays have only one element, after which it returns up,
        // assembling a final sorted array.
        static Node[] Assemble_Tree(Node[] input)
        {
            if (input.Length == 0)
            {
                return input;
            }
            var rand = new Random();

            var left = Array.Empty<Node>();
            var right = Array.Empty<Node>();
            var pivot = rand.Next(0, input.Length);

            for (int i = 0; i < input.Length; i++)
            {
                if (i == pivot)
                {
                    continue;
                }
                else if (input[i].value < input[pivot].value)
                {
                    left = Append(left, input[i]);
                }
                else
                {
                    right = Append(right, input[i]);
                }
                input[i].parent = input[pivot];
            }
            var subtree_left = Assemble_Tree(left);
            var subtree_right = Assemble_Tree(right);
            var return_array = new Node[subtree_left.Length + 1 + subtree_right.Length];
            subtree_left.CopyTo(return_array, 0);
            return_array[subtree_left.Length] = input[pivot];
            subtree_right.CopyTo(return_array, subtree_left.Length + 1);

            return return_array;
        }

        // The entry point for the algorithm, it converts the input array of
        // integers into the Nodes that the algorithm needs.
        static Node[] Rand_Quick_Sort(int[] input)
        {
            var initial_list = new Node[input.Length];
            for (int i = 0; i < input.Length; i++)
            {
                initial_list[i] = new Node() {value = input[i]};
            }

            return Assemble_Tree(initial_list);
        }

        static void Main(string[] args)
        {
            var inp = new int[] { 30, 4, 111, 4, 9, 20, 8, 17, 5, 22 };
            PrintArray(Rand_Quick_Sort(inp));
        }
    }
}
