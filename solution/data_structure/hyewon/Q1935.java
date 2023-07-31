import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Q1935 {

    void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Double> stack = new Stack<>();

        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();

        int[] nums = new int[n];
        for(int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }

        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if(c > 64 && c < 91) {
                stack.push((double) nums[c - 65]);
            } else {
                double a = stack.pop();
                double b = stack.pop();

                switch (c){
                    case '+':
                        stack.push((double)(b + a));
                        break;
                    case '-':
                        stack.push((double)(b - a));
                        break;
                    case '*':
                        stack.push((double)(b * a));
                        break;
                    case '/':
                        stack.push((double)(b / a));
                        break;
                }
            }

            //System.out.println("stack: " + stack);
        }

        System.out.printf("%.2f\n", stack.pop());
        br.close();
    }
}
