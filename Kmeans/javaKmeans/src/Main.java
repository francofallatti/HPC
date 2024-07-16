import java.util.ArrayList;
import java.util.Random;

public class Main {
    private static final int NUM_CLUSTERS = 2; // Total clusters.
    private static final ArrayList<Data> dataSet = new ArrayList<Data>();
    private static final ArrayList<Centroid> centroids = new ArrayList<Centroid>();

    private static void initialize(int totalDataPoints, double maxX, double maxY) {
        System.out.println("Centroids initialized at:");
        centroids.add(new Centroid(1.0, 1.0)); // lowest set.
        centroids.add(new Centroid(5.0, 7.0)); // highest set.
        System.out.println("     (" + centroids.get(0).getX() + ", " + centroids.get(0).getY() + ")");
        System.out.println("     (" + centroids.get(1).getX() + ", " + centroids.get(1).getY() + ")");
        System.out.print("\n");

        Random rand = new Random();
        for (int i = 0; i < totalDataPoints; i++) {
            double x = maxX * rand.nextDouble();
            double y = maxY * rand.nextDouble();
            dataSet.add(new Data(x, y));
        }
    }

    private static int kMeanCluster() {
        final double bigNumber = Math.pow(10, 10); // some big number that's sure to be larger than our data range.
        double minimum = bigNumber; // The minimum value to beat.
        double distance = 0.0; // The current minimum value.
        int cluster = 0;
        boolean isStillMoving = true;
        int iterations = 0; // Count iterations

        // Add in new data, one at a time, recalculating centroids with each new one.
        for (Data data : dataSet) {
            minimum = bigNumber;
            for (int i = 0; i < NUM_CLUSTERS; i++) {
                distance = euclideanDistance(data, centroids.get(i));
                if (distance < minimum) {
                    minimum = distance;
                    cluster = i;
                }
            }
            data.setCluster(cluster);
        }

        // Now, keep shifting centroids until equilibrium occurs.
        while (isStillMoving) {
            iterations++;
            // calculate new centroids.
            for (int i = 0; i < NUM_CLUSTERS; i++) {
                double totalX = 0;
                double totalY = 0;
                int totalInCluster = 0;
                for (Data data : dataSet) {
                    if (data.getCluster() == i) {
                        totalX += data.getX();
                        totalY += data.getY();
                        totalInCluster++;
                    }
                }
                if (totalInCluster > 0) {
                    centroids.get(i).setX(totalX / totalInCluster);
                    centroids.get(i).setY(totalY / totalInCluster);
                }
            }

            // Assign all data to the new centroids
            isStillMoving = false;

            for (Data tempData : dataSet) {
                minimum = bigNumber;
                for (int j = 0; j < NUM_CLUSTERS; j++) {
                    distance = euclideanDistance(tempData, centroids.get(j));
                    if (distance < minimum) {
                        minimum = distance;
                        cluster = j;
                    }
                }
                if (tempData.getCluster() != cluster) {
                    tempData.setCluster(cluster);
                    isStillMoving = true;
                }
            }
        }
        return iterations;
    }

    /**
     * // Calculate Euclidean distance.
     * @param d - Data object.
     * @param c - Centroid object.
     * @return - double value.
     */
    private static double euclideanDistance(Data d, Centroid c) {
        return Math.sqrt(Math.pow((c.getY() - d.getY()), 2) + Math.pow((c.getX() - d.getX()), 2));
    }

    // Main method
    public static void main(String[] args) {
        int totalDataPoints = 100;
        double maxX = 10.0; // Maximum value for x-coordinate.
        double maxY = 10.0; // Maximum value for y-coordinate.

        initialize(totalDataPoints, maxX, maxY);
        int iterations = kMeanCluster();

        // Print out clustering results.
        for (int i = 0; i < NUM_CLUSTERS; i++) {
            System.out.println("Cluster " + i + " includes:");
            for (Data data : dataSet) {
                if (data.getCluster() == i) {
                    System.out.println("     (" + data.getX() + ", " + data.getY() + ")");
                }
            }
            System.out.println();
        }

        // Print out centroid results.
        System.out.println("Centroids finalized at:");
        for (int i = 0; i < NUM_CLUSTERS; i++) {
            System.out.println("     (" + centroids.get(i).getX() + ", " + centroids.get(i).getY()+")");
        }
        System.out.print("\n");

        System.out.println("Total iterations: " + iterations); // Print the total iterations
    }
}