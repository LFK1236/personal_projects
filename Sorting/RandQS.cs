/*
Author: Louis Falk Knudsen
Date: 26/05/2022

A failed? attempt at implementing Random Quick-Sort based on the short description from the
introduction of Randomized Algorithms by Motwani and Raghavan. After implementing the
deterministic version, I see that the description wasn't complete; this one is therefore a WIP.
It works, but is very slow.

I still find recursive functions quite difficult to "visualise" in my head. I tend to prefer
nested loops, when given the option.
*/

using System;

namespace Sorting
{
    public class RandQS
    {
        // The individual entry. On the left are elements that have smaller values,
        // on the right are the remaining. At the end, each array will have only
        // one element.
        class Node
        {
            public int value;
            public Node[] left = null;
            public Node[] right = null;
        }

        // Adds a new Node element to the end of a Node array.
        private static Node[] Append(Node[] input, Node new_node)
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
        private static Node[] Assemble_Tree(Node[] input)
        {
            if (input.Length == 0)
            {
                return input;
            }
            var rand = new Random();
            var pivot = rand.Next(0, input.Length);

            input[pivot].left = Array.Empty<Node>();
            input[pivot].right = Array.Empty<Node>();

            // Compares each element to the pivot, assembling two sub-arrays accordingly.
            for (int i = 0; i < input.Length; i++)
            {
                if (i == pivot)
                {
                    continue;
                }
                else if (input[i].value < input[pivot].value)
                {
                    input[pivot].left = Append(input[pivot].left, input[i]);
                }
                else
                {
                    input[pivot].right = Append(input[pivot].right, input[i]);
                }
            }

            // Recursively call the function on the left and right arrays. These will eventually
            // be returned sorted.
            var subtree_left = Assemble_Tree(input[pivot].left);
            var subtree_right = Assemble_Tree(input[pivot].right);
            var return_array = new Node[subtree_left.Length + 1 + subtree_right.Length];

            // Copy the left and right arrays, as well as the pivot, into the array which
            // this iteration of the function will return.
            subtree_left.CopyTo(return_array, 0);
            return_array[subtree_left.Length] = input[pivot];
            subtree_right.CopyTo(return_array, subtree_left.Length + 1);

            return return_array;
        }

        // The entry point for the algorithm, it converts the input array of
        // integers into the Nodes that the algorithm needs.
        public static int[] Sort(int[] input)
        {
            // Convert the input array into a Node array.
            var initial_list = new Node[input.Length];
            for (int i = 0; i < input.Length; i++)
            {
                initial_list[i] = new Node() {value = input[i]};
            }

            // Begin the recursive algorithm.
            var return_node_list = Assemble_Tree(initial_list);

            // Convert the Node array into an array of integers.
            var return_array = new int[return_node_list.Length];
            for (int i = 0; i < return_node_list.Length; i++)
            {
                return_array[i] = return_node_list[i].value;
            }
            return return_array;
        }

        public static void Test()
        {
            Console.WriteLine("RandQS:");
            var inp = new int[] { 30, 4, 111, 4, 9, 20, -8, -17, 5, 22 };
            Console.Write("Before: ");
            Program.PrintArray(inp);
            Console.Write("After:  ");
            Program.PrintArray(Sort(inp));
        }
    }
}
