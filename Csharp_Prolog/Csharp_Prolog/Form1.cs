using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Csharp_Prolog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            levelComboBox.SelectedIndex = 0;
            levelComboBox.DropDownStyle = ComboBoxStyle.DropDownList;
        }

        private void nextFromButton_Click(object sender, EventArgs e)
        {
            int level = levelComboBox.SelectedIndex;
            Globals globals = new Globals();
            globals.setLevel(level);

            Form2 window = new Form2();
            window.Show();
            this.Hide();
        }
    }
}
