# CAT Reloaded CTF

<figure><img src="../.gitbook/assets/image (6).png" alt="" width="563"><figcaption></figcaption></figure>

### Index the Secrets

<figure><img src="../.gitbook/assets/image (4).png" alt="" width="550"><figcaption></figcaption></figure>

{% embed url="https://drive.google.com/file/d/1LHf5IlJXJ5lweKiEz5hOrriHwZj80dAm/view?usp=sharing" %}



in challenge description it refer to windows search indexes that mean `windows.edb` , so let's extrect it and anaysis.



After download `Index of Secret.rar` and extrect it will find `C` folder, could find `windows.edb` under `C\ProgramData\Microsoft\search\data\applications\windows`



<figure><img src="../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Now let's used `WinSearchDBAnalyzer` to anaysis `Windows.edb` , on

<figure><img src="../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>



After a little of seach in side `windows.edb` Ifound the Flag



<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>



```
CATF{ESE_DB_F0r3ns1cs}
```

