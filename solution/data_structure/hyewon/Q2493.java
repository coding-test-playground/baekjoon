import java.io.*;
import java.util.Iterator;
import java.util.Stack;
import java.util.StringTokenizer;

public class Q2493 {

    static class Laser {
        int index;
        int height;

        public Laser(int index, int height) {
            this.index = index;
            this.height = height;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int[] tops = new int[n];

        Stack<Laser> stack = new Stack<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            tops[i] = Integer.parseInt(st.nextToken());
            stack.push(new Laser(i, tops[i]));

            if(i == 0) {
                bw.write("0");
            } else {
                Laser l = stack.pop();

                while(!stack.empty()) {
                    Laser l2 = stack.pop();

                    if(l2.height >= l.height) {
                        stack.push(l2);
                        bw.write(" " + (l2.index+1));
                        break;
                    }
                }

                if(stack.empty()) {
                    bw.write(" 0");
                }

                stack.push(l);
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
