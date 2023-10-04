import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.Scanner;
public class html{
    public static void main(String[] args) {
        try{
        System.out.println("Enter the URL:");
        Scanner sc = new Scanner(System.in);
        String url = sc.nextLine();
        URL objURL = new URL(url);
        URLConnection objConnection=objURL.openConnection();
        InputStream stream = objConnection.getInputStream();
        System.out.println("HTML code of the URL:\n" );
        int i;
        while((i=stream.read())!=-1){
            
            System.out.print((char)i);
        }
        sc.close();
        }

        catch(IOException e){
            System.out.println(e);
        }
    }
}