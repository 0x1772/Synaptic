Add-Type -TypeDefinition @"
using System;
using System.Windows.Forms;

public static class InstallerForm {
    static bool acceptedPrivacyPolicy = false;

    [STAThread]
    public static void Main() {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);
        
        var form = new Form();
        var installButton = new Button();
        
        installButton.Text = "Install";
        installButton.Location = new System.Drawing.Point(50, 50);
        installButton.Click += (sender, e) => {
            if (!acceptedPrivacyPolicy) {
                MessageBox.Show("Please accept the privacy policy before proceeding.", "Privacy Policy", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }
            
            // Kurulum işlemini burada gerçekleştirin
            // ...
            
            MessageBox.Show("Installation completed successfully.", "Installation Complete", MessageBoxButtons.OK, MessageBoxIcon.Information);
            form.Close();
        };
        
        var privacyCheckbox = new CheckBox();
        privacyCheckbox.Text = "I accept the privacy policy";
        privacyCheckbox.Location = new System.Drawing.Point(50, 100);
        privacyCheckbox.CheckedChanged += (sender, e) => {
            acceptedPrivacyPolicy = privacyCheckbox.Checked;
        };
        
        form.Controls.Add(installButton);
        form.Controls.Add(privacyCheckbox);
        form.ShowDialog();
    }
}
"@

[InstallerForm]::Main()
