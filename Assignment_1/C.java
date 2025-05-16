import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class C {

    public static void main(String []args) throws IOException{
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        String inp_1 = br.readLine();
        int k = Integer.parseInt(inp_1.split(" ")[1]);

        String inp_2 = br.readLine();
        String[] array = inp_2.split(" ");

        StringBuilder result = new StringBuilder("");

        for(int i = k-1; i >= 0; i --){
            result.append(array[i] + " ");
        }
        System.out.println(result);


    }
 }