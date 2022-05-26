/*
Author: Louis Falk Knudsen
Date: 25/05/2022

A Random Quick-Sort implementation based on the short description from the introduction of
Randomized Algorithms by Motwani and Raghavan.

I still find recursive functions quite difficult to "visualise" in my head. I tend to prefer
nested loops, when given the option.
*/

using System;

namespace personal_projects.Sorting
{
    class RandQS
    {
        static void PrintArray(Node[] input)
        {
            for (int i = 0; i < input.Length; i++)
            {
                Console.Write(input[i].value + " ");
            }
            Console.WriteLine();
        }

        // The individual entries.
        class Node
        {
            public int value;
            public Node parent = null;
            public Node[] left = null;
            public Node[] right = null;
        }

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
            var l2 = Assemble_Tree(left);
            var r2 = Assemble_Tree(right);
            var return_array = new Node[l2.Length + 1 + r2.Length];
            l2.CopyTo(return_array, 0);
            return_array[l2.Length] = input[pivot];
            r2.CopyTo(return_array, l2.Length + 1);

            return return_array;
        }

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
