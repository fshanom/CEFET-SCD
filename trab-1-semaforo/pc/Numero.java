package pc;

public class Numero {
	private int numero;
	private Semaforo mutex, cheio, vazio;

	public Numero(int numero, Semaforo mutex, Semaforo cheio, Semaforo vazio) {
		this.numero = numero;
		this.mutex = mutex;
		this.cheio = cheio;
		this.vazio = vazio;
	}

	public int consumir(String idThread) {
		cheio.P();
		mutex.P();
		System.out.println("  Consumidor " + idThread + "\t consumiu: \t" + this.numero);
		mutex.V();
		vazio.V();
		return this.numero;
	}

	public void produzir(String idThread, int valor) {
		vazio.P();
		mutex.P();
		this.numero = valor;
		System.out.println("Produtor " + idThread + "\t produziu: \t" + valor);
		mutex.V();
		cheio.V();
	}
}