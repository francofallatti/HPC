public class Data {
    private double X = 0;
    private double Y = 0;
    private int cluster = 0;

    public Data() {
    }

    public Data(double x, double y) {
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

    public void setCluster(int clusterNumber) {
        this.cluster = clusterNumber;
    }

    public int getCluster() {
        return this.cluster;
    }
}
