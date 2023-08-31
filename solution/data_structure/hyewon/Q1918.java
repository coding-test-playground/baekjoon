import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.Stack;

public class Q1918 {

    /*public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        String answer = returnPostfix(s);

        System.out.println(answer);
    }*/

    /*static String returnPostfix(String s) {

        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) == '('){

                int closeIndex = 0;
                boolean correctClose = true;

                for(int j = i+1; ; j++) {
                    if(s.charAt(j) == '('){
                        correctClose = false;
                    } else if(s.charAt(j) == ')'){
                        if(correctClose) {
                            closeIndex = j;
                            break;
                        } else {
                            correctClose = true;
                        }
                    }
                }

                s = returnPostfix(s.substring(i + 1, closeIndex)) + s.substring(closeIndex+1, s.length());

                i = closeIndex+1;

                continue;
            }

            String front = "";
            String back = "";

            if(s.charAt(i) < 48) {
                if(i != s.length()-1 && s.charAt(i + 1) < 48) continue;

                int closeIndex = s.length();
                for(int j = i+2; j < s.length(); j++) {
                    if(s.charAt(j) < 48) {
                        closeIndex = j;
                        break;
                    }
                }

                front = s.substring(0, i);
                back = s.substring(i + 1, closeIndex);
                if(back.charAt(0) == '(') back = returnPostfix(back.substring(1, back.length()-1));

                s = new String(front + back + s.charAt(i)) + s.substring(closeIndex, s.length());
                i = closeIndex - 1;
            }
        }

        return s;
    }*/

    static class Operator {
        char type;
        int priority;

        public Operator(char type) {
            this.type = type;
            setPriority();
        }

        void setPriority() {
            if(type == '*' || type == '/') {
                this.priority = 2;
            } else if(type == '(' || type == ')') {
                this.priority = 0;
            } else {
                this.priority = 1;
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Stack<Operator> stack = new Stack<>();

        String s = br.readLine();
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < s.length(); i++ ){
            if(s.charAt(i) >= 'A') {
                sb.append(s.charAt(i));
            } else if(s.charAt(i) == ')') {
              while(!stack.isEmpty() && stack.peek().type != '(') {
                  sb.append(stack.pop().type);
              }

              stack.pop();

            } else if(s.charAt(i) == '('){

                stack.push(new Operator('('));

            } else {
                Operator o = new Operator(s.charAt(i));

                if(o.type != '(') {
                    while(true) {
                        if(!stack.isEmpty() && stack.peek().priority >= o.priority) {
                            sb.append(stack.pop().type);
                        } else {
                            break;
                        }
                    }
                }

                stack.push(o);
            }
        }

        while(!stack.isEmpty()) {
            sb.append(stack.pop().type);
        }

        System.out.println(sb);
    }
}
