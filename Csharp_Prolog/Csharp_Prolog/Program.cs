using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

/*
            Lenguajes de programación 
            Project: Battleship with C# and Prolog
            Students: Gabriel Pérez Barquero
                      Cristian Alvarado Gomez

*/
namespace Csharp_Prolog
{
    static class Program
    {
        /// <summary>
        /// Punto de entrada principal para la aplicación.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }
    }
}
