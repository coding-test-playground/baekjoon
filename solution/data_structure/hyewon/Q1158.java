import java.io.*;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Q1158 {

    void solve() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        LinkedList<Integer> roundPeople = new LinkedList<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        for(int i = 1; i <= n; i++) {
            roundPeople.offer(i);
        }

        int count = 0;
        bw.write("<");
        while(!roundPeople.isEmpty()) {
            count = (count + k - 1) % roundPeople.size();

            bw.write(roundPeople.get(count)+ "");
            if(roundPeople.size() != 1) bw.write(", ");

            roundPeople.remove(count);

        }
        bw.write(">");

        br.close();
        bw.flush();
        bw.close();
    }
}
