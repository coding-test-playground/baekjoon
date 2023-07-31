import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q9012 {
    void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for(int i = 0; i < t; i++) {
            String s = br.readLine();
            int ps = 0;
            String answer = "YES";

            for(int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);

                if(c == '(') ps++;
                else if(c == ')') ps--;

                if(ps < 0) {
                    answer = "NO";
                    break;
                }
            }

            if(ps == 0) answer = "YES";
            else answer = "NO";

            System.out.println(answer);
        }
    }
}
