package ABB;

public class MainAntecesorComun {

	public static void main(String[] args) {
		System.out.println("Antecesor comun");
		BinarySearchTree abb = new BinarySearchTree();
		abb.insert(25);
		abb.insert(15);
		abb.insert(10);
		abb.insert(22);
		abb.insert(4);
		abb.insert(12);
		abb.insert(18);
		abb.insert(50);
		abb.insert(70);
		abb.insert(90);
		abb.insert(66);
		abb.insert(35);
		abb.insert(44);
		//el arbol se ve de la siguiente forma
		/*		
		 * 						   25
		 * 					   /        \
		 * 				      15		 50	
		 * 				     / \	   /    \ 
		 * 				   10   22	  35     70
		 * 				  / \    /     \     / \
		 * 			  	 4  12  18     44   66  90    
		 */
		
		Node n1 , n2, res;
		
		n1 = new Node(4);
		n2 = new Node(12);
		res = lowestCommonAncestor(abb, n1, n2); //10
		System.out.println("el antecesor comun entre " + n1.key + " y " + n2.key + " es: " + res.key);
		
		n1 = new Node(12);
		n2 = new Node(35);
		res = lowestCommonAncestor(abb, n1, n2); //25
		System.out.println("el antecesor comun entre " + n1.key + " y " + n2.key + " es: " + res.key);
		
		n1 = new Node(44);
		n2 = new Node(66);
		res = lowestCommonAncestor(abb, n1, n2); //50
		System.out.println("el antecesor comun entre " + n1.key + " y " + n2.key + " es: " + res.key);
		
		n1 = new Node(18);
		n2 = new Node(10);
		res =lowestCommonAncestor(abb, n1, n2); //15
		System.out.println("el antecesor comun entre " + n1.key + " y " + n2.key + " es: " + res.key);
	}
	
	public static Node lowestCommonAncestor(BinarySearchTree abb, Node n1, Node n2){
		// asumimos que los dos nodos provistos estan dentro del arbol
		Node raiz=abb.root;
		while (raiz != null) 
	    { 
	        if (raiz.key > n1.key && raiz.key > n2.key) {// si n1 y n2 son mas chicos que la raiz del subarbol actual entonces vamos a la izquierda 
	        	raiz = raiz.left; 
	        }else if (raiz.key < n1.key && raiz.key < n2.key) {// Si n1 y n2 son mas grandes que la raiz del subarbol actual entonces vamos a la derecha 
	        	raiz = raiz.right; 
	        }else {
	        	break; 
	        }  
	    } 
		return raiz;
	}
}
