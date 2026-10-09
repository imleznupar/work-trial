When I want to insert a data sheet local link into a Symbol properties dialog, KiCad 9.0.8 converts it to

kicad-embed://Name\_data\_sheet.pdf

instead of using the already given directory entry $HOME/$PATH/Name\_data\_sheet.pdf, where I have my Data sheets stored since the invention of Linux.

I want to suppress this cryptic behaviour and have KiCad use the given directory link

$HOME/$PATH/Name\_data\_sheet.pdf as entry.

It is possible to copy it directly, but this is 2 unnecessary steps fro me.

Is there a setting to automate my desired proceeding?

            
          
          
            
            
              I have not tried this myself, I only read the KiCad docs (Schematic Editor chapter, Datasheet field of the symbol properties).

The docs say you can pick a local datasheet with the file browser button next to the Datasheet field. There is an “Embed File” checkbox in that file browser, and if it is enabled the datasheet is embedded in the schematic instead of being referenced as an external file. That could explain the kicad-embed:// entry. My guess, not confirmed: the checkbox is on when you pick the file. The docs do not mention a setting that changes this default, so I can’t say if one exists.

Question: does the kicad-embed:// entry appear only when you pick the file with the browser button, or also when you paste the path into the field?

            
          
          
            
            
              maybe you have set the small checkbox “Embed file” in the “Open Datasheet File” dialog.

            
          
          
            
            
              Yes the checkbox is there, and I must turn it off each time before I select the data sheet.

Now I must make this checkbox being unchecked as a default.

            
          
          
            
            
              Now I must make this checkbox being unchecked as a default


So now you have a reason to update from v9 to v10. Kicad v10 saves and restores the last used state of this checkbox.

            
          
          
            
            
              I prefer to have this set in a config file . Is that possible?

I am with devuan oldstable and use kicad from Backports. So I must settle with 9.0.8

debian/devuan testing currently has 10.0.2.

I will try this in a virtual machine first.