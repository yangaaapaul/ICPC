import java.util.*; 
public class alphabetanimals{
     public static ArrayList<String> helper(
        String animal,
        ArrayList<String> list) {
        ArrayList<String> result = new ArrayList<>();
        for (String x : list) {
            if (x.charAt(0) == animal.charAt(animal.length() - 1)) {
                result.add(x);
            }
        }
        return result;
    }

     public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String animal = sc.nextLine();
        int n = Integer.parseInt(sc.nextLine());
        ArrayList<String> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(sc.nextLine());
        }
        ArrayList<String> bruh = helper(animal, list);
        if (bruh.size() == 0) {
            System.out.println("?");
        }
        else {
            int flag = 1;
            for (String x : bruh) {
                ArrayList<String> copy = new ArrayList<>(list);
                copy.remove(x);
                if (helper(x, copy).size() == 0) {
                    System.out.println(x + "!");
                    flag = 0;
                    break;
                }
            }
            if (flag == 1) {
                System.out.println(bruh.get(0));
            }
        }

    }
}