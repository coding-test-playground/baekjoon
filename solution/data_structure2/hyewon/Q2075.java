import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Q2075 {

    void solve(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] nums = new int[n*n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n*n; i++) {
            if(i != 0 && i % n == 0) st = new StringTokenizer(br.readLine());

            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);

        System.out.println(nums[nums.length-n]);

    }
}
