import java.io.*;
import java.util.*;

public class Q18258 {

    void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Integer> queue = new ArrayDeque<>();

        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++) {
            StringTokenizer command = new StringTokenizer(br.readLine());

            switch (command.nextToken()){
                case "push":
                    queue.offer(Integer.parseInt(command.nextToken()));
                    break;
                case "pop":
                    if(queue.isEmpty()) bw.write("-1\n");
                    else {
                        bw.write(queue.poll() + "\n");
                    }
                    break;
                case "size":
                    bw.write(queue.size() + "\n");
                    break;
                case "empty":
                    if(queue.isEmpty()) bw.write("1\n");
                    else bw.write("0\n");
                    break;
                case "front":
                    if(queue.isEmpty()) bw.write("-1\n");
                    else bw.write(queue.peekFirst() + "\n");
                    break;
                case "back":
                    if(queue.isEmpty()) bw.write("-1\n");
                    else bw.write(queue.peekLast() + "\n");
                    break;
            }
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
