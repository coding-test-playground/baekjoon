import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Q14425 {

    void solve(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int answer = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        ArrayList<String> s = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            s.add(br.readLine());
        }

        for(int i = 0; i < m; i++) {
            if(s.contains(br.readLine())) {
                answer++;
            }
        }

        System.out.println(answer);
    }
}
