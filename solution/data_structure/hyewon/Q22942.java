import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Q22942 {

    static class Circle {
        int x;
        int r;

        public Circle(int x, int r) {
            this.x = x;
            this.r = r;
        }
    }

    void solve(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Circle> stack = new Stack<>();

        int n = Integer.parseInt(br.readLine());
        String answer = "YES";

        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            if(i == 0) stack.push(new Circle(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
            else {
                Circle c1 = new Circle(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));

                for (Circle c2 : stack) {
                    double d = Math.sqrt(Math.pow((c1.x - c2.x), 2));
                    int raPlusrb = c1.r + c2.r;
                    int raMinusrb = Math.abs(c1.r - c2.r);

                    if(d > raPlusrb || d < raMinusrb) continue;
                    else {
                        answer = "NO";
                        break;
                    }
                }
            }

            if(answer.equals("NO")) break;
        }

        System.out.println(answer);
    }
}
