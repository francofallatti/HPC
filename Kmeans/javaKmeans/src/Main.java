import java.util.ArrayList;

public class Main {
    private static final int NUM_CLUSTERS = 2; // Total clusters.
    private static final int TOTAL_DATA = 7; // Total data points.
    private static final double[][] SAMPLES = new double[][] { { 1.0, 1.0 }, { 1.5, 2.0 }, { 3.0, 4.0 }, { 5.0, 7.0 },
            { 3.5, 5.0 }, { 4.5, 5.0 }, { 3.5, 4.5 } };
    private static final ArrayList<Data> dataSet = new ArrayList<Data>();
    private static final ArrayList<Centroid> centroids = new ArrayList<Centroid>();

    private static void initialize() {
        System.out.println("Centroids initialized at:");
        centroids.add(new Centroid(1.0, 1.0)); // lowest set.
        centroids.add(new Centroid(5.0, 7.0)); // highest set.
        System.out.println("     (" + centroids.get(0).getX() + ", " + centroids.get(0).getY() + ")");
        System.out.println("     (" + centroids.get(1).getX() + ", " + centroids.get(1).getY() + ")");
        System.out.print("\n");
        return;
    }

    private static void kMeanCluster() {
        final double bigNumber = Math.pow(10, 10); // some big number that's sure to be larger than our data range.
        double minimum = bigNumber; // The minimum value to beat.
        double distance = 0.0; // The current minimum value.
        int sampleNumber = 0;
        int cluster = 0;
        boolean isStillMoving = true;
        Data newData = null;

        // Add in new data, one at a time, recalculating centroids with each new one.
        while (dataSet.size() < TOTAL_DATA) {
            newData = new Data(SAMPLES[sampleNumber][0], SAMPLES[sampleNumber][1]);
            dataSet.add(newData);
            minimum = bigNumber;
            for (int i = 0; i < NUM_CLUSTERS; i++) {
                distance = dist(newData, centroids.get(i));
                if (distance < minimum) {
                    minimum = distance;
                    cluster = i;
                }
            }
            newData.setCluster(cluster);

            // calculate new centroids.
            for (int i = 0; i < NUM_CLUSTERS; i++) {
                int totalX = 0;
                int totalY = 0;
                int totalInCluster = 0;
                for (int j = 0; j < dataSet.size(); j++) {
                    if (dataSet.get(j).getCluster() == i) {
                        totalX += (int) dataSet.get(j).getX();
                        totalY += (int) dataSet.get(j).getY();
                        totalInCluster++;
                    }
                }
                if (totalInCluster > 0) {
                    centroids.get(i).setX(totalX / totalInCluster);
                    centroids.get(i).setY(totalY / totalInCluster);
                }
            }
            sampleNumber++;
        }

        // Now, keep shifting centroids until equilibrium occurs.
        while (isStillMoving) {
            // calculate new centroids.
            for (int i = 0; i < NUM_CLUSTERS; i++) {
                int totalX = 0;
                int totalY = 0;
                int totalInCluster = 0;
                for (int j = 0; j < dataSet.size(); j++) {
                    if (dataSet.get(j).getCluster() == i) {
                        totalX += (int) dataSet.get(j).getX();
                        totalY += (int) dataSet.get(j).getY();
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

            for (int i = 0; i < dataSet.size(); i++) {
                Data tempData = dataSet.get(i);
                minimum = bigNumber;
                for (int j = 0; j < NUM_CLUSTERS; j++) {
                    distance = dist(tempData, centroids.get(j));
                    if (distance < minimum) {
                        minimum = distance;
                        cluster = j;
                    }
                }
                tempData.setCluster(cluster);
                if (tempData.getCluster() != cluster) {
                    tempData.setCluster(cluster);
                    isStillMoving = true;
                }
            }
        }
        return;
    }

    /**
     * // Calculate Euclidean distance.
     * @param d - Data object.
     * @param c - Centroid object.
     * @return - double value.
     */
    private static double dist(Data d, Centroid c) {
        return Math.sqrt(Math.pow((c.getY() - d.getY()), 2) + Math.pow((c.getX() - d.getX()), 2));
    }

    // Main method
    public static void main(String[] args) {
        initialize();
        kMeanCluster();

        // Print out clustering results.
        for (int i = 0; i < NUM_CLUSTERS; i++) {
            System.out.println("Cluster " + i + " includes:");
            for (int j = 0; j < TOTAL_DATA; j++) {
                if (dataSet.get(j).getCluster() == i) {
                    System.out.println("     (" + dataSet.get(j).getX() + ", " + dataSet.get(j).getY() + ")");
                }
            } // j
            System.out.println();
        } // i

        // Print out centroid results.
        System.out.println("Centroids finalized at:");
        for (int i = 0; i < NUM_CLUSTERS; i++) {
            System.out.println("     (" + centroids.get(i).getX() + ", " + centroids.get(i).getY()+")");
        }
        System.out.print("\n");
        return;
    }
}