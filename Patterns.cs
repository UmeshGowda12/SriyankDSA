namespace Student_DSA.Patterns
{
    public class Pattern
    {
        public static void Pattern1(int N)
        {
            char alpha = 'A';
            for(int rows = 1; rows <= N; rows++)
            {
                for(int col = 1; col <= rows; col++)
                {
                    Console.Write(alpha);
                    alpha++;
                }
                Console.WriteLine();
            }
        }

        public static void Pattern2(int N)
        {
            for (int rows = 1; rows <= N; rows++)
            {
                int beginDigit = rows % 2 == 0 ? 0 : 1;
                for (int col = 1; col <= rows; col++)
                {
                    Console.Write(beginDigit);
                    beginDigit = 1 - beginDigit;
                }
                Console.WriteLine();
            }
        }

        public static void Pattern3(int N)
        {
            for (int rows = 1; rows <= N; rows++)
            {
                for (int spaces = 1; spaces <= N - rows; spaces++)
                {
                    Console.Write(" ");
                }
                for (int col = 1; col <= rows; col++)
                {
                    Console.Write("* ");
                }
                Console.WriteLine();
            }
        }


        public static char ConvertToUpper(char input)
        {
            return (char)(input - 32); //97-32 = 65  //8 bit //int 32 bit
        }
    }
}
