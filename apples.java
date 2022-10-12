import java.util.*; 
public class apples{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int c = sc.nextInt();
        char[][] grid = new char[r][c];
        for (int i = 0; i < r; i++) {
            grid[i] = sc.next().toCharArray();
        }

        for (int i = 0; i < c; i++) {
            int space = 0;
            for (int j = r - 1; j >= 0; j--) {
                if (grid[j][i] == '.') {
                    space++;
                }
                else if (grid[j][i] == '#') {
                    space = 0;
                }
                else if (space > 0) {
                    grid[j][i] = '.';
                    grid[j + space][i] = 'a';

                }
            }
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                System.out.print(grid[i][j]);
            }
            System.out.println();
        }

    }
}