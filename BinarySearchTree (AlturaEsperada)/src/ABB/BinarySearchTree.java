package ABB;

public class BinarySearchTree {
	Node root;

	BinarySearchTree() {
		root = null;
	}

	void insert(double key) {
		root = insertRec(root, key);
	}

	Node insertRec(Node root, double key) {

		if (root == null) {
			root = new Node(key);
			return root;
		}
		if (key < root.key)
			root.left = insertRec(root.left, key);
		else if (key > root.key)
			root.right = insertRec(root.right, key);

		return root;
	}

	public Node search(Node root, double key) {
		if (root == null || root.key == key)
			return root;

		if (root.key < key)
			return search(root.right, key);

		return search(root.left, key);
	}

	void inorder() {
		inorderRec(root);
	}

	void inorderRec(Node root) {
		if (root != null) {
			inorderRec(root.left);
			System.out.println(root.key);
			inorderRec(root.right);
		}
	}

	void deleteKey(double key) {
		root = deleteRec(root, key);
	}

	Node deleteRec(Node root, double key) {
		if (root == null)
			return root;

		if (key < root.key)
			root.left = deleteRec(root.left, key);
		else if (key > root.key)
			root.right = deleteRec(root.right, key);

		else {
			if (root.left == null)
				return root.right;
			else if (root.right == null)
				return root.left;

			root.key = minValue(root.right);

			root.right = deleteRec(root.right, root.key);
		}

		return root;
	}

	double minValue(Node root) {
		double minv = root.key;
		while (root.left != null) {
			minv = root.left.key;
			root = root.left;
		}
		return minv;
	}
	
	int height() {
		return heightRec(root);
	}
	
	int heightRec(Node root) {
		int leftHeight, rightHeight; 
		if(root== null) {
			return 0;
		}
		leftHeight = heightRec(root.left);
		rightHeight = heightRec(root.right);
		return Math.max(leftHeight, rightHeight) + 1;
	}
}
