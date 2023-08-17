import java.io.*;
import java.util.*;

public class Q2800 {

    static class Parenthesis {
        int start;
        int end;

        public Parenthesis(int start, int end) {
            this.start = start;
            this.end = end;
        }

        public Parenthesis(int start) {
            this.start = start;
            this.end = -1;
        }

        public void setEnd(int end) {
            this.end = end;
        }
    }

    void solve(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        ArrayList<Parenthesis> arrayList = new ArrayList<>();
        Set<String> answer = new HashSet<>();

        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if(c == '(') {
                arrayList.add(new Parenthesis(i));
            } else if(c == ')') {
                if(arrayList.get(arrayList.size()-1).end == -1) {
                    arrayList.get(arrayList.size()-1).setEnd(i);
                } else {
                    for(int j = arrayList.size()-1; j >= 0; j--){
                        if(arrayList.get(j).end == -1) {
                            arrayList.get(j).setEnd(i);
                            break;
                        }
                    }
                }
            }
        }

        recursion(s, arrayList, 0, answer);

        ArrayList<String> answer2 = new ArrayList<>(answer);

        Collections.sort(answer2);

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for(String string : answer2) {
            bw.write(string + "\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }

    static void recursion(String s, ArrayList<Parenthesis> arrayList, int index, Set<String> answer) {
        char[] s2 = s.toCharArray();

        if(index >= arrayList.size()) return;

        s2[arrayList.get(index).start] = ' ';
        s2[arrayList.get(index).end] = ' ';

        String s3 = new String(s2);
        if(!s3.equals(s)) {
            answer.add(s3.replaceAll(" ", ""));
        }

        recursion(s3, arrayList, index+1, answer);
        recursion(s, arrayList, index+1, answer);
    }
}
