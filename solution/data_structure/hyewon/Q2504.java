import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Q2504 {

    void solve(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Stack<Character> stack = new Stack<>();
        String s = br.readLine();
        int answer = 0;


        int count2 = 0;
        int count3 = 0;
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if(c == '(') {
                count2 += 2;
                if((i+1) != s.length() && s.charAt(i+1) == ']') {
                    System.out.println(0);
                    return;
                }
            } else if(c == '[') {
                count3 += 3;
                if((i+1) != s.length() && s.charAt(i+1) == ')') {
                    System.out.println(0);
                    return;
                }
            } else if(c == ')') count2 -= 2;
            else if(c == ']') count3 -= 3;
            else {
                System.out.println(0);
                return;
            }

            if(count2 < 0 || count3 < 0) {
                System.out.println(0);
                return;
            }

            stack.push(c);
        }

        if(count2 != 0 || count3 != 0){
            System.out.println(0);
            return;
        }

        while(!stack.empty()) {
            char c = stack.pop();
            int c_num = c == ']' || c == '[' ? 3 : 2;

            answer += caculate(stack, c);
        }

        System.out.println(answer);
    }

    public static int caculate(Stack<Character> stack, char c) {

        int count = 0;
        boolean notEnd = false;
        if(c == ')') {
            while(notEnd == true || stack.peek() != '(') {
                char c2 = stack.pop();
                if(c2 == ')' && stack.peek() == '(') notEnd = true;
                if(c2 == '(') notEnd = false;
                if(c2 == ']' || c2 == ')') {
                    if(stack.peek() == ']' || stack.peek() ==')') {
                        count += caculate(stack, c2) * 2;
                    }
                    else {
                        if(c2 >= 90) count +=3;
                        else count +=2;
                    }
                } else {
                    if(c2 >= 90) count +=3;
                    else {
                        count += 2;
                        notEnd = false;
                    }
                }
            }

            if(count == 0) count = 2;

        } else if(c == ']') {
            while(notEnd == true || stack.peek() != '[') {
                char c2 = stack.pop();
                if(c2 == ']' && stack.peek() == '[') notEnd = true;
                if(c2 == '[') notEnd = false;
                if(c2 == ']' || c2 == ')') {
                    if(stack.peek() == ']' || stack.peek() ==')') {
                        count += caculate(stack, c2) * 2;
                    }
                    else {
                        if(c2 >= 90) count +=3;
                        else count +=2;
                    }
                } else {
                    if(c2 >= 90) {
                        count += 3;
                        notEnd = false;
                    }
                    else count +=2;
                }
            }

            count = count * 3 / 2;

            if(count == 0) count = 3;
        }

        stack.pop();
        return count;
    }
}
