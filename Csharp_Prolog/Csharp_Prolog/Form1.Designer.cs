namespace Csharp_Prolog
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
            
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.levelComboBox = new System.Windows.Forms.ComboBox();
            this.nextFromButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.BackColor = System.Drawing.Color.Transparent;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.DarkRed;
            this.label1.Location = new System.Drawing.Point(24, 428);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(76, 29);
            this.label1.TabIndex = 0;
            this.label1.Text = "Level";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.BackColor = System.Drawing.Color.Transparent;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 27.75F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.ForeColor = System.Drawing.Color.DarkRed;
            this.label2.Location = new System.Drawing.Point(214, 19);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(192, 42);
            this.label2.TabIndex = 1;
            this.label2.Text = "Battleship";
            // 
            // levelComboBox
            // 
            this.levelComboBox.BackColor = System.Drawing.Color.BurlyWood;
            this.levelComboBox.Cursor = System.Windows.Forms.Cursors.Hand;
            this.levelComboBox.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.levelComboBox.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.levelComboBox.ForeColor = System.Drawing.Color.DarkRed;
            this.levelComboBox.FormattingEnabled = true;
            this.levelComboBox.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.levelComboBox.Items.AddRange(new object[] {
            "Easy",
            "Medium",
            "Hard"});
            this.levelComboBox.Location = new System.Drawing.Point(106, 429);
            this.levelComboBox.Name = "levelComboBox";
            this.levelComboBox.Size = new System.Drawing.Size(119, 28);
            this.levelComboBox.TabIndex = 2;
            // 
            // nextFromButton
            // 
            this.nextFromButton.BackColor = System.Drawing.Color.Transparent;
            this.nextFromButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.nextFromButton.ForeColor = System.Drawing.Color.DarkRed;
            this.nextFromButton.Location = new System.Drawing.Point(529, 427);
            this.nextFromButton.Name = "nextFromButton";
            this.nextFromButton.Size = new System.Drawing.Size(94, 35);
            this.nextFromButton.TabIndex = 3;
            this.nextFromButton.Text = "Create ";
            this.nextFromButton.UseVisualStyleBackColor = false;
            this.nextFromButton.Click += new System.EventHandler(this.nextFromButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::Csharp_Prolog.Properties.Resources.BATLLESHIP;
            this.ClientSize = new System.Drawing.Size(640, 481);
            this.Controls.Add(this.nextFromButton);
            this.Controls.Add(this.levelComboBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Name = "Form1";
            this.Text = "Player1                                             Blattleship by Gabriel and Cr" +
    "istian";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ComboBox levelComboBox;
        private System.Windows.Forms.Button nextFromButton;
    }
}

