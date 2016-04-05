import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Iterator;


public class PrimeIterable implements Iterable<Long> {
	
	private String fileName;
	
	public PrimeIterable(String fileName) {
		this.fileName = fileName;
	}
	
	public class PrimeIterator implements Iterator<Long> {
		private DataInputStream input;
		private long nbElement;
		private long currentElement = 0;
		
		public PrimeIterator(String fileName) throws FileNotFoundException {
			input = new DataInputStream(new BufferedInputStream(new FileInputStream(fileName)));
			nbElement = new File(fileName).length() / 8;
		}
		
		public boolean hasNext() {
			return (currentElement < nbElement);
		}
		
		public Long next() {
			currentElement++;
			try {
				return input.readLong();
			} catch (IOException e) {
				return -1l;
			}
		}
		public void remove() { }
	}

	@Override
	public Iterator<Long> iterator() {
		try {
			return new PrimeIterator(fileName);
		} catch (FileNotFoundException e) {
			e.printStackTrace();
			return null;
		}
	}
}