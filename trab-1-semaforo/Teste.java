import pc.Consumidor;
import pc.Numero;
import pc.Produtor;
import pc.Semaforo;

public class Teste {

	public static void main(String[] args) {
		
		int numeroPermissoes = 1;
		Semaforo mutex = new Semaforo(numeroPermissoes);
		Semaforo cheio = new Semaforo(0);
		Semaforo vazio = new Semaforo(1);
		
		Numero n = new Numero(0, mutex, cheio, vazio);
		Produtor p = new Produtor(n);
		Consumidor c = new Consumidor(n);
		Consumidor c1 = new Consumidor(n);
		Consumidor c2 = new Consumidor(n);
		
				
		p.start();
		c.start();
		c1.start();
		c2.start();

	}

}
