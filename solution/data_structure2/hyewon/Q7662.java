import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
import java.util.TreeMap;

public class Q7662 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while(t > 0) {
            TreeMap<Integer, Integer> q = new TreeMap<>();

            int k = Integer.parseInt(br.readLine());

            for(int i = 0; i < k; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String operator = st.nextToken();
                int n = Integer.parseInt(st.nextToken());

                if(operator.equals("D")) {
                    if(q.isEmpty()) continue;

                    if(n == 1) {
                        if(q.get(q.lastKey()) == 1) q.remove(q.lastKey());
                        else {
                            q.put(q.lastKey(), q.get(q.lastKey())-1);
                        }
                    } else {
                        if(q.get(q.firstKey()) == 1) q.remove(q.firstKey());
                        else {
                            q.put(q.firstKey(), q.get(q.firstKey())-1);
                        }
                    }

                } else {
                    if(q.containsKey(n)) q.put(n, q.get(n)+1);
                    else q.put(n, 1);
                }
            }
            if(q.isEmpty()) System.out.println("EMPTY");
            else {
                int min = q.firstKey();
                int max = q.lastKey();

                System.out.println(max + " " + min);
            }

            t--;
        }
    }
}
