import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class Q10866 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Integer> deque = new ArrayDeque<>();

        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            switch (st.nextToken()){
                case "push_front":
                    deque.offerFirst(Integer.parseInt(st.nextToken()));
                    break;
                case "push_back":
                    deque.offerLast(Integer.parseInt(st.nextToken()));
                    break;
                case "pop_front":
                    if (deque.isEmpty()) bw.write("-1\n");
                    else bw.write(deque.pollFirst() + "\n");
                    break;
                case "pop_back":
                    if (deque.isEmpty()) bw.write("-1\n");
                    else bw.write(deque.pollLast() + "\n");
                    break;
                case "size":
                    bw.write(deque.size() + "\n");
                    break;
                case "empty":
                    if (deque.isEmpty()) bw.write("1\n");
                    else bw.write("0\n");
                    break;
                case "front":
                    if (deque.isEmpty()) bw.write("-1\n");
                    else bw.write(deque.peekFirst() + "\n");
                    break;
                case "back":
                    if (deque.isEmpty()) bw.write("-1\n");
                    else bw.write(deque.peekLast() + "\n");
                    break;

            }
        }

        br.close();
        bw.flush();
        bw.close();
    }
}
