import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class Q2164 {
    void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Integer> deque = new ArrayDeque<>();

        int n = Integer.parseInt(br.readLine());

        for(int i = 1; i <= n; i++) {
            deque.offer(i);
        }

        int count = 1;
        while(deque.size() > 1){
            if(count % 2 == 1) deque.pop();
            else deque.offer(deque.pop());

            count++;
        }

        System.out.println(deque.pop());

    }
}
