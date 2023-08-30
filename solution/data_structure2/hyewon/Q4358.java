import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

// 8 : 50
public class Q4358 {
    void solve(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Comparator<String> comparator = Comparator.naturalOrder();
        Map<String, Integer> trees = new TreeMap<>(comparator);
        int total = 0;

        while(true) {
            String s = br.readLine();

            if(s == null || s.isEmpty()) break;

            if(trees.containsKey(s)) {
                int count = trees.get(s);
                trees.put(s, count+1);
            } else {
                trees.put(s, 1);
            }

            total++;
        }

        for(String key: trees.keySet()){
            System.out.print(key + " ");
            System.out.println(String.format("%.4f", (double)((double)trees.get(key) / total) * 100));
        }

    }
}
