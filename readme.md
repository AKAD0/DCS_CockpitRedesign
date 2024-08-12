From AlbaMelody with love <3

# Installation
1. Copy '/DCS World' into the game directory '../Eagle Dynamics/';
2. Enjoy!

# Usage
Custom colors work only for unprotected servers!
1. Run 'hud.bat' as administrator to change the HUD color (You won't be able to spawn on protected servers!);
2. Run 'hud-reset' as administrator to reset game files (You'll get back the access to protected servers);
3. Restart the game to apply new settings.

# Custom color
The file 'materials-new.lua' contains 4 arrays:

line 23) MDG_materials[MDG_SELF_IDS.HUD] = {&lt;values&gt;}

line 29) MDG_materials[MDG_SELF_IDS.LMDI] = {&lt;values&gt;}

line 81) materials["RWR_STROKE"] = {&lt;values&gt;}

line 84) materials["HMD_SYMBOLOGY_MATERIAL"] = {&lt;values&gt;}

Change their &lt;values&gt; in RGB-ish manner to set a new color.