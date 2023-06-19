public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
    }

   private void RunSynaptic_Click(object sender, RoutedEventArgs e)
   {
       Process.Start("synaptic");
   }

   private void InstallSynpatic_Click(object sender, RoutedEventArgs e)
   {
       string output = "";
       using (Process process = new Process())
       {

           process.StartInfo.FileName = "sudo";
           process.StartInfo.Arguments = "apt-get install synaptic -y";
           process.StartInfo.UseShellExecute = false;
           process.StartInfo.RedirectStandardOutput = true;
           process.OutputDataReceived += new DataReceivedEventHandler((s, e) =>
               output += e.Data + "\n"
            );
           
          // Start the installation and wait for it to finish.
          process.Start();
          while (!process.StandardOutput.EndOfStream)
              output += $"{process.StandardOutput.ReadLine()}\n";

          MessageBox.Show(output);
      }
  }