
package ex0009;

import java.time.LocalDateTime;

public class Messwert
{
  private final double wert;
  private final LocalDateTime zeit;
  private final String kommentar;

  public Messwert(double wert, LocalDateTime zeit, String kommentar)
  {
    this.wert = wert;
    this.zeit = zeit;
    this.kommentar = kommentar;
  }

  public double getWert()
  {
    return wert;
  }

  public LocalDateTime getZeit()
  {
    return zeit;
  }

  public String getKommentar()
  {
    return kommentar;
  }

  @Override
  public String toString()
  {
    return wert + " " + zeit + " " + kommentar;
  }
  
  public static void main(String[] args)
  {
    Messwert m1 = new Messwert(22,LocalDateTime.now(),"Arnfels KU Saal");
    System.out.println(m1.getWert()+" "+m1.getZeit()+" "+m1.getKommentar());
    System.out.println(""+m1);
  }
}
