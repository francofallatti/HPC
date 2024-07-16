public class Centroid {
    private double X = 0.0;
    private double Y = 0.0;

    public Centroid() {
    }

    public Centroid(double x, double y) {
        this.X = x;
        this.Y = y;
    }

    public void setY(double y) {
        this.Y = y;
    }

    public void setX(double x) {
        this.X = x;
    }

    public double getX() {
        return X;
    }

    public double getY() {
        return Y;
    }
}
