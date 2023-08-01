import java.io.*;
import java.util.*;

public class Q1966 {

    /*static class Paper implements Comparable<Paper>{
        int number;
        int primary;

        public Paper(int number, int primary) {
            this.number = number;
            this.primary = primary;
        }

        @Override
        public String toString() {
            return "Paper{" +
                    "number=" + number +
                    ", primary=" + primary +
                    '}';
        }

        @Override
        public int compareTo(Paper p) {
            return this.primary <= p.primary ? 1 : -1;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int t = Integer.parseInt(br.readLine());

        for(int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            if(!st.hasMoreTokens()) st = new StringTokenizer(br.readLine());

            PriorityQueue<Paper> priorityQueue = new PriorityQueue<>();
            for(int j = 0; j < n; j++) {
                priorityQueue.offer(new Paper(j, Integer.parseInt(st.nextToken())));
            }

            while(!priorityQueue.isEmpty()){
                System.out.println(priorityQueue.poll());
            }
        }

    }*/

    static class Paper{
        int number;
        int primary;

        public Paper(int number, int primary) {
            this.number = number;
            this.primary = primary;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        LinkedList<Paper> printQueue = new LinkedList<>();

        int t = Integer.parseInt(br.readLine());

        for(int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            if(!st.hasMoreTokens()) st = new StringTokenizer(br.readLine());

            for(int j = 0; j < n; j++) {
                printQueue.offer(new Paper(j, Integer.parseInt(st.nextToken())));
            }

            int count = 1;
            while(!printQueue.isEmpty()) {
                Paper comparePaper = printQueue.poll();

                boolean isPrint = false;

                for(int j = 0; j < printQueue.size(); j++) {
                    if(comparePaper.primary < printQueue.get(j).primary) {
                        printQueue.offer(comparePaper);
                        isPrint = false;
                        break;
                    } else {
                        isPrint = true;
                    }
                }

                if(printQueue.isEmpty()) isPrint = true;
                if(isPrint == true) {
                    if(comparePaper.number == m) System.out.println(count);
                    count++;
                }
            }
        }
    }
}
