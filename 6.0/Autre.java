import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.Stack;


public class Autre {

	/////////////////
	// # Matrice # //
	/////////////////
	
	public static double[][] matriceMultiplication(double[][] matrix1, double[][] matrix2) {
		double[][] resultMatrix = new double[matrix1.length][matrix2[0].length];
		
		for (int i=0; i<matrix1.length; i++) {
			for (int j=0; j<matrix2[0].length; j++) {
				
				// i - ligne 1
				// j - col 2
				
				double value = 0;
				
				for (int k=0; k<matrix1[0].length; k++) {
					value += matrix1[i][k] * matrix2[k][j];
				}
				
				resultMatrix[i][j] = value;
			}
		}
		
		return resultMatrix;
	}
	
	/**
	 * 
	 * @param matrix
	 * @param angle En radian
	 * @return
	 */
	public static double[] rotateMatrix(double[] matrix, double angle) {
		double[][] matrixCoeficient = new double[][]{
			new double[] { Math.cos(angle), -Math.sin(angle) },
			new double[] { Math.sin(angle), Math.cos(angle) }
		};
		
		double[][] matrixXY = new double[][]{ 
				new double[] { matrix[0] },
				new double[] { matrix[1] }
		};
		
		double[][] resultMatrix = matriceMultiplication(matrixCoeficient, matrixXY);
		
		return new double[] { resultMatrix[0][0], resultMatrix[1][0] };
	}
	
	public static BigDecimal[][] matriceMultiplication(BigDecimal[][] matrix1, BigDecimal[][] matrix2) {
		BigDecimal[][] resultMatrix = new BigDecimal[matrix1.length][matrix2[0].length];
		
		for (int i=0; i<matrix1.length; i++) {
			for (int j=0; j<matrix2[0].length; j++) {
				
				// i - ligne 1
				// j - col 2
				
				BigDecimal value = BigDecimal.ZERO;
				
				for (int k=0; k<matrix1[0].length; k++) {
					value = value.add(matrix1[i][k].multiply(matrix2[k][j]));
				}
				
				resultMatrix[i][j] = value;
			}
		}
		
		return resultMatrix;
	}
	
	/**
	 * 
	 * @param matrix
	 * @param angle En radian
	 * @return
	 */
	public static BigDecimal[] rotateMatrix(BigDecimal[] matrix, BigDecimal angle) {
		BigDecimal[][] matrixCoeficient = new BigDecimal[][]{
			new BigDecimal[] { new BigDecimal(Math.cos(angle.doubleValue()) + ""), new BigDecimal(-Math.sin(angle.doubleValue())+"") },
			new BigDecimal[] { new BigDecimal(Math.sin(angle.doubleValue())+"")  , new BigDecimal(Math.cos(angle.doubleValue())+"") }
		};
		
		BigDecimal[][] matrixXY = new BigDecimal[][]{ 
				new BigDecimal[] { matrix[0] },
				new BigDecimal[] { matrix[1] }
		};
		
		BigDecimal[][] resultMatrix = matriceMultiplication(matrixCoeficient, matrixXY);
		
		return new BigDecimal[] { resultMatrix[0][0], resultMatrix[1][0] };
	}
	
	////////////////
	// # Modulo # //
	////////////////
	
	public static long euclideInverseMod(long nb, long mod) {
		
		if (nb == 1) {
			return 1;
		}
		
		Stack<long[]> stack = new Stack<long[]>();
		
		long a = mod;
		long b = nb;
		long n = mod / nb;
		long r = mod % nb;
		
		while (r != 0) {
			stack.push(new long[] { a, b, n, r });
			
			a = b;
			b = r;
			n = a / b;
			r = a % b;
		}
		
		long[] values = stack.pop();
		long f1 = 1, f2 = values[2];
		boolean atN2 = true;
		
		while (stack.size() > 0) {
			values = stack.pop();
			
			if (atN2) {
				f1 += f2 * values[2];
			} else {
				f2 += f1 * values[2];
			}
			
			atN2 = !atN2;
		}
		
		long f = (atN2) ? -f2: f1;
		
		return mod(f, mod);
	}

	public static long mod(long nb, long mod) {
		if (nb < 0) {
			nb += mod * (Math.abs(nb / mod) + 1);
		}
		
		return nb % mod;
	}
	
	//////////////////////
	// # Prime number # //
	//////////////////////
	
	public static int PRIME_COUNT = 0;
	public static int[] PRIMES = new int[10000000];
	
	public static int PRIME_RANGE_COUNT = 0;
	public static long[] PRIME_RANGE = null;
	
	/**
	 * 
	 * @param n
	 */
	public static void generatePrime(int n) {
		boolean[] listNumber = new boolean[n + 1];
		
		for (int i=2; i<=n; i++) {
			if (!listNumber[i]) {
				PRIMES[PRIME_COUNT++] = i;
				
				for (int j=i; j<=n; j+=i) {
					listNumber[j] = true;
				}
			}
		}
	}
	
	public static void generatePrimeRange(long min, long max) {
	    
	}
	
	public static Iterable<Long> getPrimes()  {
		return new PrimeIterable("F:\\Documents\\Primes\\Primes_10^11.bin");
	}
	
	public static Long[] getPrimes(long min, long max) {
		ArrayList<Long> lst = new ArrayList<Long>();
		
		for (long p : getPrimes()) {
			if (p < min) continue;
			if (p > max) break;
			lst.add(p);
		}
		
		Long[] r = new Long[lst.size()];
		lst.toArray(r);
		return r;
	}
}
