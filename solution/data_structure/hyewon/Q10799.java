import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Q10799 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Stack<Integer> stack = new Stack<>();
        int answer = 0;

        String s = br.readLine();

        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '(') {
                stack.push(i);
                answer++;
            } else if(s.charAt(i) == ')') {
                stack.pop();
                if(i != 0 && s.charAt(i-1) == '(') {
                    answer--;
                    answer += stack.size();
                }
            }
        }

        System.out.println(answer);
    }
}
