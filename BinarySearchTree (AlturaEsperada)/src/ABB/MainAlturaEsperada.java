package ABB;

import java.util.*;

public class MainAlturaEsperada {
	public static void main(String[] args) {
		System.out.println("# elementos : altura esperada"); 
		int aux = 0;
		for (int i = 0; i <= 10000; i += 100) {
			int alt=promedioAltura(i);
			if(aux!=alt) {
				System.out.println(i + " : " + alt);
			}
			aux=alt;
		}
	}

	public static int promedioAltura(int n) {
		ArrayList<Integer> alturas = new ArrayList<Integer>();
		for (int i = 0; i < 1000; i++) {
			alturas.add(Llenado_Altura(n));
		}
		return promedioDeLista(alturas);
	}

	public static int Llenado_Altura(int n) {
		BinarySearchTree abb = new BinarySearchTree();
		double random;
		for (int i = 0; i < n; i++) {
			random = Math.random();
			abb.insert(random);
		}
		return abb.height();
	}

	public static int promedioDeLista(ArrayList<Integer> lista) {
		int res = 0;
		for (Integer i : lista) {
			res += i;
		}
		return res / lista.size();
	}
}
