## A Python script to help deobfuscate PowerShell scripts (.ps1) that use the value reordering based on an index list obfuscation technique.
### Prompt 1
```
Enter number orders to arrange values: {2}{0}{3}{4}{5}{1}
```
### Prompt 2
```
Enter values: WebRequest,Invoke,http,:,//bad.site,-
```
### Result
```
Reordered:  http WebRequest : //bad.site - Invoke
```
