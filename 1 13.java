import java.util.Random;
import java.util.Scanner;

public class Main {
    static String[] inventory = new String[10]; // Inventory can hold up to 10 items

    public static void main(String[] args) {
        boolean monsterDied = true;
        Scanner scanner = new Scanner(System.in); // Used for user input
        int room = 1; // Starting room
        String direction;
        //add player health here
        int health = 0;
        for(int i = 0; i<10; i++) {
            inventory[i] = " "; //initialize each inventory slot to 0
        }
        inventory[3] = "potato"; //give user a potato!
        boolean running = true;
        while (true) { // Game loop change to check player health
            System.out.println("Your inventory:");
            for (int i = 0; i < 10; i++) {
                System.out.print(inventory[i]);
                System.out.print(" ");
            }
            System.out.println(" ");
            switch (room) {
                case 1: // Room 1
                    inventory[3]=itemDropper();
                    System.out.println("You are in room 1, you can go east.");
                    if (!inventory[0].equals("sword")) {
                        inventory[0] = "sword";
                        System.out.println("You got a sword!");
                    }
                    direction = scanner.nextLine().trim().toLowerCase();
                    if ("east".equals(direction)) {
                        room = 2;
                    } else {
                        System.out.println("Invalid direction. Staying in room " + room);
                    }
                    break;

                case 2: // Room 2
                    if(monsterDied) {
                        String monster = generateMonster();
                        fightMonster(monster);
                        monsterDied = false;
                    }
                    System.out.println("You are in room 2, you can go west or south.");
                    direction = scanner.nextLine().trim().toLowerCase();
                    if ("west".equals(direction)) {
                        room = 1;
                    } else if ("south".equals(direction)) {
                        room = 3;
                    } else {
                        System.out.println("Invalid direction. Staying in room " + room);
                    }
                    break;
                case 3: // Room 2
                    itemDropper();
                    System.out.println("You are in room 3, you can go north or south.");
                    direction = scanner.nextLine().trim().toLowerCase();
                    if ("north".equals(direction)) {
                        room = 2;
                    } else if ("south".equals(direction)) {
                        room = 4;
                    } else {
                        System.out.println("Invalid direction. Staying in room " + room);
                    }
                    break;
                case 4: // Room 2
                    System.out.println("You are in room 4, you can go north or west.");
                    direction = scanner.nextLine().trim().toLowerCase();
                    if ("north".equals(direction)) {
                        room = 3;
                    } else if ("west".equals(direction)) {
                        room = 5;
                    } else {
                        System.out.println("Invalid direction. Staying in room " + room);
                    }
                    break;
                case 5: // Room 1
                    //END THE GAME HERE!
                   System.out.println("you made it! game over :)");
                   running = false;
                    break;
            } // End of switch
        } // End of game loop
    } // End of main

    // Monster generator function
    public static String generateMonster() {
        Random rand = new Random();
        String[] names = {"Goblin", "Skeleton", "Orc"};
        int index = rand.nextInt(names.length);

        return names[index];
    }
    public static String itemDropper() {
        Random rand = new Random();
        String[] names = {"pooto", "bread", "eggs"};
        int index = rand.nextInt(names.length);
        System.out.println("you found a "+names[index]);
        return names[index];
    }

    // Battle system function
    public static void fightMonster(String monster) {

        Random rand = new Random();
        int damage = rand.nextInt(10) + 5; // Simulates damage dealt
        //check if slot 0 has a sword
        //if yes, add 10 to damage and print that they hit with the sword
        System.out.println("A wild " + monster + " appears!");
        System.out.println("You deal " + damage + " damage and defeat the " + monster + "!");

        System.out.println("the monster dropped an item!");
        inventory[4]= itemDropper();
    }
}
