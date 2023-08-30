import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Q11286 {

    // 9: 43 ~ 9:58
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Comparator<Integer> comparator = (o1, o2) -> {
            int abs1 = Math.abs(o1);
            int abs2 = Math.abs(o2);
            if(abs1 - abs2 == 0) return o1 - o2;
            else return abs1 - abs2;
        };

        PriorityQueue<Integer> queue = new PriorityQueue<>(comparator);

        int n = Integer.parseInt(br.readLine());

        for(int i = 0; i < n; i++){
            int x = Integer.parseInt(br.readLine());

            if(x == 0) {
                if(queue.isEmpty()) System.out.println("0");
                else System.out.println(queue.poll());
            } else {
                queue.add(x);
            }
        }
    }
}
