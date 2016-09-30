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
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
            createMatrix();
            flowLayoutPanel2.Enabled = false;
        }
        public int sizeButton = 0;
        public bool player1Ready = false;
        public bool player2Ready = false;
        public int player1ShipsLeft = 0;
        public int player2ShipsLeft = 0;

        private void createMatrix()
        {
            player1ShipsLeftLabel.Text = "0";
            player2ShipsLeftLabel.Text = "0";
            //flowLayoutPanel1.Controls.Clear();
            Globals globals = new Globals();
            int n = 0;

            if (globals.getLevel() == 0)
            {
                sizeButton = 66;
                n = 35;
                totalShipsLabel.Text = "10";
                
            }
            else if(globals.getLevel() == 1)
            {
                sizeButton = 50;
                n = 63;
                totalShipsLabel.Text = "9";
            }
            else
            {
                sizeButton = 40;
                n = 99;
                totalShipsLabel.Text = "10";
            }

            for (int i = 0; i <= n; i++)
            {
                flowLayoutPanel1.Controls.Add(btn(i));
                flowLayoutPanel2.Controls.Add(btn(i));
            }
        }

        Button btn(int i)
        {
            Button b = new Button();
            b.Name = i.ToString();
            b.Width = sizeButton;
            b.Height = sizeButton;
            b.TabStop = false;
            b.FlatStyle = FlatStyle.Flat;
            b.FlatAppearance.BorderSize = 0;

            b.Margin = new Padding(0);
            b.FlatStyle = FlatStyle.Flat;
            b.BackColor = Color.Transparent;// DeepSkyBlue;//"#00bfff";
            b.Click += b_CLieck;
            return b;
        }

        private void b_CLieck(object sender, EventArgs e)
        {
            Button b = (Button)sender;
            var bmp = new  Bitmap(Csharp_Prolog.Properties.Resources.WaterSplash66, new Size(sizeButton, sizeButton));
            if (!player1Ready)
            {
                if (b.BackgroundImage != null)
                {
                    player1ShipsLeft = player1ShipsLeft - 1;
                    player1ShipsLeftLabel.Text = player1ShipsLeft.ToString();

                    bmp = null;
                    b.BackgroundImage = bmp;
                }
                else if (player1ShipsLeft < Int32.Parse(totalShipsLabel.Text))
                {
                    bmp = new Bitmap(Csharp_Prolog.Properties.Resources.ship, new Size(sizeButton, sizeButton));
                    player1ShipsLeft += 1;
                    player1ShipsLeftLabel.Text = player1ShipsLeft.ToString();
                    b.BackgroundImage = bmp;
                }

                
            }
            

            if (player2Ready)
            {
                flowLayoutPanel2.Enabled = true;
                bmp = new Bitmap(Csharp_Prolog.Properties.Resources.WaterSplash66, new Size(sizeButton, sizeButton));

                b.Enabled = false;
            }

           
            
           
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form1 window = new Form1();
            window.Show();
            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {

            if (Int32.Parse(player1ShipsLeftLabel.Text) < Int32.Parse(totalShipsLabel.Text))
            {
                MessageBox.Show("Please put all the ships");
            }
            else
            {
                label1.ForeColor = Color.Green;
                button2.Enabled = false;
                flowLayoutPanel1.Enabled = false;
                player1Ready = true;
            }
            

        }
    }
}
