public class ex25 { 

	public static void main(String args[]) {

        double[] grades = new double[]{7, 9, 10, 8.5, 8, 9.5, 2, 4, 7, 8};

        double[] grades_backup = new double[10];

        System.out.println( "mean value: " + meanValue (grades) );
        System.out.println( "max value: " + maxValue (grades) );
        System.out.println( "min value: " + minValue (grades) );
        myCopy (grades, grades_backup);
        printArray (grades);
        printArray (grades_backup);
    }

    private static double meanValue(double[] array) {
        int sum = 0;
        for (int i=0; i<=array.length; i++){
            sum+=array[i]; }
        return sum/array.length;
    }

    private static double maxValue(double[] array) {
        double max = 0;
        for (int i=0; i<=array.length; i++){
            if(array[i]>=max) max = array[i];
        }
        return max;
    }

    private static double minValue(double[] array) {
        double min = 10000;
        for (int i=0; i<=array.length; i++)
            if(array[i]<=min) 
				min = array[i];
        return min;
    }

    private static void myCopy(double[] grades, double[] grades_backup) {
        for (int i=0; i<=grades.length; i++){
            grades_backup[i] = grades[i];
        }
    }

    private static void printArray(double[] array) {
        for (int i=0; i<=array.length; i++){
            System.out.println(array[i]);
        }
    }
}