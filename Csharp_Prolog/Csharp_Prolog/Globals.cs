using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Csharp_Prolog
{
    class Globals
    {
        static int selectedLevel = 0;
        static int ships = 0;
        

        public void setShips(int count)
        {
            ships = count;
        }
        public int getShips()
        {
            return ships;
        }

        public void setLevel(int level)
        {
            selectedLevel = level;
        }
        public int getLevel()
        {
            return selectedLevel;
        }
    }
}
