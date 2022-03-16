package ex0009;

import java.time.LocalDateTime;
import java.util.ArrayList;
import javax.swing.AbstractListModel;

public class Inventory extends AbstractListModel
{
  private ArrayList<Messwert> list;
  
  public Inventory()
  {
    list = new ArrayList();
    // Testdaten
    Messwert m1 = new Messwert(22,LocalDateTime.now(),"Arnfels KU Saal");
    list.add(m1);
    Messwert m2 = new Messwert(23,LocalDateTime.now(),"Kaindorf an der Sulm");
    list.add(m2);
  }
  
  public void add(Messwert m)
  {
    list.add(m);
    this.fireIntervalAdded(this, list.size()-1, list.size()-1);
  }

  @Override
  public int getSize()
  {
    return list.size();
  }

  @Override
  public Object getElementAt(int index)
  {
    return list.get(index);
  }

  public void delete(int index)
  {
    list.remove(index);
    this.fireIntervalRemoved(this, index, index);
  }

  public void removeEntries()
  {
    int i=0;
//    while(i<list.size())
//    {
//      Messwert m = list.get(i);
//      String name = m.getKommentar();
//      if(name.equals("Arnfels KU Saal"))
//      {
//        list.remove(i);
//      }
//      else
//      {
//        i++;
//      }
//    }

    for(i=list.size()-1; i>=0; i--)
    {
      if(list.get(i).getKommentar().equals("Arnfels KU Saal"))
      {
        list.remove(i);
      }      
    }
    this.fireIntervalRemoved(this, 0, list.size()-1);
  }

  public double maxTemperatureValue()
  {
    int i;
    double max = list.get(0).getWert();
    for(i=1; i<=list.size()-1; i++)
    {
      if(list.get(i).getWert()>max)
      {
        max = list.get(i).getWert();
      }
    }
    return max;
  }

  public int countMaxTempValues()
  {
    double max = maxTemperatureValue();
    int i,counter=0;
    for(i=0; i<=list.size()-1; i++)
    {
      if(list.get(i).getWert()==max)
      {
        counter++;
      }
    }
    return counter;
  }

  public String getAllEntriesFrom2021()
  {
    StringBuilder sb = new StringBuilder();
    sb.append("<html><body><table border='1'>");
    for(int i=0; i<list.size()-1; i++)
    {
      if(list.get(i).getZeit().getYear()==2021)
      {
        sb.append("<tr><td>");
        sb.append(list.get(i).getKommentar());
        sb.append("</td><td>");
        sb.append(list.get(i).getWert());
        sb.append("</td></tr>");
      }
    }
    sb.append("</table></body></html>");
    return sb.toString();
  }
}
