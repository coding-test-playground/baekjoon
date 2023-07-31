import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.*;

public class Q10828 {

    // Scanner를 BufferedReader로 교체해야 함...
    void solve() throws IOException {
        int n = 0;
        Stack<Integer> stack = new Stack<>();

        //Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //n = sc.nextInt();
        n = Integer.parseInt(br.readLine());


        for (int i = 0; i < n; i++) {
            //String command = sc.next();
            String s = br.readLine();
            String[] command = s.split(" ");

            switch (command[0]) {
                case "push":
                    //stack.push(sc.nextInt());
                    stack.push(Integer.parseInt(command[1]));
                    break;

                case "pop":
                    if (stack.empty()) System.out.println(-1);
                    else {
                        System.out.println(stack.pop());
                    }
                    break;

                case "size":
                    System.out.println(stack.size());
                    break;

                case "empty":
                    if (stack.empty()) System.out.println(1);
                    else System.out.println(0);
                    break;

                case "top":
                    if (stack.empty()) System.out.println(-1);
                    else System.out.println(stack.peek());
                    break;
            }
        }

        //sc.close();
        br.close();
    }
}
