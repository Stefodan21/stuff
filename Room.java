public class Room {
    private final String name;
    private String color;
    private final double width;
    private final double length;
    private double temperature;

    public Room(String name, String color, double width, double length, double temperature) {
        this.name = name;
        this.color = color;
        this.width = width;
        this.length = length;
        this.temperature = temperature;
    }

    public double area() {
        return width * length;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getColor() {
        return color;
    }

    public void setTemperature(double temperature) {
        this.temperature = temperature;
    }

    public double getTemperature() {
        return temperature;
    }

    public static void main(String[] args) {
        Room kitchen = new Room("kitchen", "white", 10.5, 12.0, 77.0);

        double area = kitchen.area();

        kitchen.setColor("blue");        this.color = color;

        double newTemp = kitchen.getTemperature() + 3.0;
        kitchen.setTemperature(newTemp);

        System.out.printf(
                "Color: %s  Area: %.2f  Temp: %.2f%n",
                kitchen.getColor(), area, kitchen.getTemperature()
        );
    }
}
