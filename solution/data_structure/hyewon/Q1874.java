import java.io.*;
import java.util.Stack;

public class Q1874 {

    /*
    * BufferedWriter는 긴 문자열을 임시 저장했다가 출력하는 데에 용이하지 않으므로
    * 긴 문자열을 대상으로 빠르게 출력할 때에는 StringBuffer 나 String Builder를 사용한다.
    */
    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Stack<Integer> stack = new Stack<>();

        int n = Integer.parseInt(br.readLine());

        int stack_size = 0;
        for(int j = 0; j < n; j++) {
            int m = Integer.parseInt(br.readLine().strip());

            if(stack.empty()) {
                for (int i = stack_size+1; i <= m; i++) {
                    stack.push(i);
                    //bw.write("+\n");
                    sb.append("+\n");
                }

                stack_size = m;
                stack.pop();
                //bw.write("-\n");
                sb.append("-\n");
            } else {
                if(stack.peek() > m) {
                    System.out.println("NO");
                    return;
                } else if(stack.peek() < m) {
                    if(stack_size > m) {
                        System.out.println("NO");
                        return;
                    }
                    for(int i = stack_size+1; i <= m; i++) {
                        stack.push(i);
                        //bw.write("+\n");
                        sb.append("+\n");
                    }

                    stack_size = m;
                    stack.pop();
                    //bw.write("-\n");
                    sb.append("-\n");
                } else {
                    stack.pop();
                    //bw.write("-\n");
                    sb.append("-\n");
                }
            }
        }

        System.out.println(sb.toString());
        //br.close();
        //bw.flush();
        //bw.close();
    }
}
