import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Q1620 {
    void solve(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<String, Integer> pokemons = new Hashtable<>();
        String[] pokemons_arr = new String[n];

        for(int i = 1; i <= n; i++){
            String s = br.readLine();
            pokemons.put(s, i);
            pokemons_arr[i-1] = s;
        }

        for(int i = 0; i < m; i++) {
            String s = br.readLine();

            if(pokemons.get(s) == null) {
                System.out.println(pokemons_arr[Integer.parseInt(s)-1]);
            } else {
                System.out.println(pokemons.get(s));
            }
        }
    }
}
