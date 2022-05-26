using Sorting;
using System;
using NUnit.Framework;

namespace Sorting_Tests
{
    [TestFixture]
    public class Test_Quicksort
    {

        [Test]
        public void Test_Quicksort_Presorted()
        {
            var input = new int[] { -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            var expected = new int[] { -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            var actual = Quicksort.Sort(input, 0, input.Length - 1);
            Assert.AreEqual(expected, actual);
        }

        [Test]
        public void Test_Quicksort_Oppositely_Sorted()
        {
            var input = new int[] { 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10 };
            var expected = new int[] { -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            var actual = Quicksort.Sort(input, 0, input.Length - 1);
            Assert.AreEqual(expected, actual);
        }

        [Test]
        public void Test_Quicksort_Empty_Input()
        {
            var input = new int[] { };
            var expected = new int[] { };
            var actual = Quicksort.Sort(input, 0, input.Length - 1);
            Assert.AreEqual(expected, actual);
        }

        [Test]
        public void Test_Quicksort_Single_Input()
        {
            var input = new int[] { 1 };
            var expected = new int[] { 1 };
            var actual = Quicksort.Sort(input, 0, input.Length - 1);
            Assert.AreEqual(expected, actual);
        }

        [Test]
        public void Test_Quicksort_Negative_Input_Only()
        {
            var input = new int[] { -1, -80, -10, -3 };
            var expected = new int[] { -80, -10, -3, -1 };
            var actual = Quicksort.Sort(input, 0, input.Length - 1);
            Assert.AreEqual(expected, actual);
        }

        [Test]
        public void Test_Quicksort_Positive_Input_Only()
        {
            var input = new int[] { 1, 80, 10, 3 };
            var expected = new int[] { 1, 3, 10, 80 };
            var actual = Quicksort.Sort(input, 0, input.Length - 1);
            Assert.AreEqual(expected, actual);
        }

        [Test]
        public void Test_Quicksort_All_Equal()
        {
            var input = new int[] { 1, 1, 1, 1, 1, 1 };
            var expected = new int[] { 1, 1, 1, 1, 1, 1 };
            var actual = Quicksort.Sort(input, 0, input.Length - 1);
            Assert.AreEqual(expected, actual);
        }

        [Test]
        public void Test_Quicksort_Large_Input()
        {
            var rand = new Random();

            var input = new int[3000];
            Array.Fill(input, rand.Next(-2000, 2000));

            var expected = new int[3000];
            input.CopyTo(expected,0);
            Array.Sort(expected);
            var actual = Quicksort.Sort(input, 0, input.Length - 1);
            Assert.AreEqual(expected, actual);
        }
    }
}