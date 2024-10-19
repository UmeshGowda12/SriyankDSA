namespace Student_DSA.DecisionMakingStmts
{
    public class DMS
    {
        //Develop a project 
        // If Client budget is over 10k $ I will take the project, If not I will not do anything

        public static void IsProjectTaken(int budget)
        {
            if(budget > 10000)
            {
                System.Console.WriteLine("Take the project");
            }
            else
            {
                System.Console.WriteLine("Let's Negotiate"); // This gets executed always when if block condition is not satisified
            }
        }

        //1 : Website -> 5000$
        //2 : AI/ML -> 15000$
        //3 : Robotics -> 50000$
        //4 : Any other type : We won't take it
        public static void IsProjectTakenEnhanced(int budget, int projectType)
        {
            if (projectType == 1 && budget >= 5000) //&& checks the first condition, and executes the second if and only if the first one is true where as OR executes all the conditions.
            {
                System.Console.WriteLine("Take the website project");
            }
            else if (projectType == 2 && budget >= 15000)
            {
                System.Console.WriteLine("Take the AI/ML project");
            }
            else if (projectType == 3 && budget >= 50000)
            {
                System.Console.WriteLine("Take the Robotics project");
            }
            else
            {
                System.Console.WriteLine("We will not take it up"); // This gets executed always when if block/ else if block condition is not satisified
            }
        }

        //1 : Website -> 5000$
        //2 : AI/ML -> 15000$
        //3 : Robotics -> 50000$
        //4 : Invalid Category
        public static string IsProjectTakenEnhancedV2(int budget)
        {
            string response = "";

            if (budget >= 5000) 
            {
               response = "This is the website project";
            }
            if (budget >= 15000)
            {
                response="This is the AI/ML project";
            }
            if (budget >= 50000)
            {
                response ="This is the Robotics project";
            }
            else
            {
                response = "Invalid Budget"; 
            }

            return response;
        }

        //Switch along with break
        public static string IsProjectTakenEnhancedV3(int projectType)
        {
            string s = "";
            switch (projectType)
            {
                case 1:
                    s = "Budget of websites is atmost 5000$";
                    break;
                case 2:
                    s = "Budget of AI/ML is atmost 15000$";
                    break;
                default:
                    s = "Invalid Project Type";
                    break;
            }

            return s;
        }
        
        //while
        //do-while
        //for
        //foreach -> Arrays 
        public static void Print1ToN(int num)
        {
            //Syntax :
            //while(condition)
            // {

            // }
            int i = 0;
            while (i <= 100) //This keeps executing till the condition is true
            {
                Console.WriteLine(i);
                i = i + 1;
            }
        }

        public static void Print1ToNV2(int num)
        {
            //Syntax :
            //for(int i = intialize the number ; condition; incrementor/decrementor)
            for(int i = num; i >= 0; i--)
            {
                Console.WriteLine(i);
            }
        }

        public static void Print1ToNV3(int num)
        {
            int i = 0;
            do
            {
                Console.WriteLine(i);
                i = i + 1;
            }
            while(i <= num);
        }
    }
}
