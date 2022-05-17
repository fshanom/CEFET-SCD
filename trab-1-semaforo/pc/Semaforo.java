package pc;

public class Semaforo {
	private int contador = 0;

	public Semaforo(int valorInicial) {
		contador = valorInicial;
	}

	public synchronized void P() {
		if (contador <= 0)
			try { /* esperar até que count > 0 */
				wait();
			} catch (InterruptedException e) {
			}
		contador--;
	}

	public synchronized void V() {
		contador++;
		notify(); /* acordar quem estiver em espera */
	}
}
