import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Q2346 {

    static class Balloon {
        int number;
        int paper;

        public Balloon(int number, int paper) {
            this.number = number;
            this.paper = paper;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Deque<Balloon> queue = new ArrayDeque<>();

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++) {
            queue.offer(new Balloon(i+1, Integer.parseInt(st.nextToken())));
        }

        int k = 0;
        while(!queue.isEmpty()) {
            Balloon b;
            if(k >= 0) b = queue.pollFirst();
            else b = queue.pollLast();
            //bw.write((b.number) + "");
            System.out.print(b.number + "");

            if(!queue.isEmpty()) {
                //bw.write(" ");
                System.out.print(" ");

                k = b.paper;

                for (int i = 0; i < (k > 0 ? k : k*(-1))-1; i++) {
                    if(b.paper > 0) queue.offerLast(queue.pollFirst());
                    else queue.offerFirst(queue.pollLast());
                }
            }
        }

        br.close();
        bw.flush();
        bw.close();
    }
}
