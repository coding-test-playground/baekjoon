import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Q11279 {

    void solve(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>((a, b) -> b - a);

        int n = Integer.parseInt(br.readLine());

        while(n > 0) {
            int x = Integer.parseInt(br.readLine());

            if(x == 0) {
                if(heap.isEmpty()) System.out.println(0);
                else System.out.println(heap.poll());
            } else {
                heap.add(x);
            }

            n--;
        }

        br.close();
    }
}
