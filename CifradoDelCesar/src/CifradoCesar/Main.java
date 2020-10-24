package CifradoCesar;

public class Main {

	public static void main(String[] args) {
		int[] llave = {17, 6, 25, -13, -8, 4};
		String mensajeCifradoProfe= "DK FHKXRT KNK IJZQHUXLXZF VI UGSBK"; 
		String ITAM ="ITAM";
		System.out.println(cifrar(ITAM,llave)); // vemos que cifra correctamente ITAM
		
		System.out.println(descifrar(mensajeCifradoProfe, llave)); // vemos que descifra correctamente el mensaje del profe
		
		String mensajeOriginal="ME GUSTAN LAS ESTRUCTURAS DE DATOS";
		System.out.println(cifrar(mensajeOriginal, llave)); // ciframos el mensaje original del profe y corroboramos que sea el mismo
		System.out.println(corrimiento('Z',0));

		
	}	
	
	private static String cifrar(String mensajeOriginal, int[] llave){
		if(mensajeOriginal==null){
			return "No hay mensaje original";
		}
		if(llave==null){
			return "No hay llave";
		}
		char[] arr=mensajeOriginal.toCharArray();
		StringBuilder mensajeCifrado = new StringBuilder();
		int j=0;
		for(int i=0 ; i < arr.length ; i++){
			if(Character.isUpperCase(arr[i])){
				mensajeCifrado.append(corrimiento(arr[i],llave[j%llave.length]));
				j++; // este contador externo al for es necesario porque si uso el del for sigue avanzando el indice de la llave incluso con espacios
			}else if((int)arr[i]==32){
				mensajeCifrado.append(arr[i]);
			}else{
				return "Hay algun caracter que no es un espacio o una letra mayuscula en el mensaje";	
			}
		}
		return mensajeCifrado.toString();
	}

	private static String descifrar(String mensajeCifrado, int[] llave){
		char[] arr = mensajeCifrado.toCharArray();
		StringBuilder mensajeDescifrado = new StringBuilder();
		if(mensajeCifrado==null){
			return "No hay mensaje cifrado";
		}
		if(llave==null){
			return "No hay una llave";
		}
		int[] llaveInvertida = llaveInversa(llave);
		int j=0;
		for(int i=0 ; i < arr.length ; i ++){
			if(Character.isUpperCase(arr[i])){
				mensajeDescifrado.append(corrimiento(arr[i],llaveInvertida[j%(llave.length)]));	
				j++; // este contador externo al for es necesario porque si uso el del for sigue avanzando el indice de la llave incluso con espacios
			}else if((int)arr[i]==32){
				mensajeDescifrado.append(arr[i]);
			}else{
				return "Hay algun caracter que no es un espacio o una letra mayuscula en el mensaje";	
			}
				
		}
		return mensajeDescifrado.toString();
	}

	private static char corrimiento(char a, int corrimientos){ // funcion que hace el corrimiento de un character apoyandose en su casting a ASCII
		int ascii = (int)a;
		int orden = ascii-64;
		int corr = corrimientos%26;
		if(corr<0){
			if(orden+corr<1){
				return (char)(90+orden+corr);
			}else{
				return (char)(ascii+corr);
			}	
		}else{ 
			if(orden+corr<27){
				return (char)(ascii+corr);
			}else{
				return (char)(64+(orden+corr)%26);	
			}
		}
	}
	
	private static int[] llaveInversa(int[] llave){ // funcion que cambia de signo a todos los elementos de un arreglo de ints (la llave inversa)
		int[] aux =  new int[llave.length];
		for(int i=0 ; i < llave.length ; i++ ){
			aux[i]=llave[i]*-1;
		}
		return aux;
	}
	
}
