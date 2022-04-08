// Source: https://usaco.guide/general/io

import java.util.*;
import java.io.*;

class Kattio extends PrintWriter {
	private BufferedReader r;
	private StringTokenizer st = new StringTokenizer("");
	private String token;

	// standard input
	public Kattio() { this(System.in,System.out); }
	public Kattio(InputStream i, OutputStream o) {
		super(o);
		r = new BufferedReader(new InputStreamReader(i));
	}
	// USACO-style file input
	public Kattio(String problemName) throws IOException { 
		super(new FileWriter(problemName+".out"));
		r = new BufferedReader(new FileReader(problemName+".in"));
	}

	private String peek() {
		if (token == null)
			try {
				while (!st.hasMoreTokens()) {
					String line = r.readLine();
					if (line == null) return null;
					st = new StringTokenizer(line);
				}
				token = st.nextToken();
			} catch (IOException e) { }
		return token;
	}
	public boolean hasMoreTokens() { return peek() != null; }
	public String next() {
		String ans = peek(); 
		token = null;
		return ans;
	}

	public String nextLine() {
		try {
			if (token == null) return r.readLine();
			else throw new IllegalStateException("Not done reading previous line");
		} catch (IOException e) { }
		return null;
	}
	
	public int nextInt() { return Integer.parseInt(next()); }
	public double nextDouble() { return Double.parseDouble(next()); }
	public long nextLong() { return Long.parseLong(next()); }
}

public class Template {
    
	static Kattio io;
	public static void main(String[] args) throws IOException {
		io = new Kattio();

		int n = io.nextInt();

		io.println(n * n);
		io.close(); // make sure to include this line -- closes io and flushes the output
	}
}
