
Beiruti Open-Source Variable Font

See: 
     ./Source/1-drawings/Beiruti-Black.glyphs
     ./Source/1-drawings/Beiruti-Regular.glyphs
     ./Source/1-drawings/Beiruti-ExtraLight.glyphs

Glyphs data are used as source file format. 
UFO data are used as production file format. 


See: 
     /source/2-production/Beiruti-Black.ufo
     /source/2-production/Beiruti-Regular.ufo
     /source/2-production/Beiruti-ExtraLight.ufo

     /source/2-production/BeirutiVF.designspace

Production:

     The production of the variable ttf font is done with fontmake and a designspacefilei
     the production of the variable cff2 font is done with buildcff2vf (from the Adobe SDK)

     buildcff2vf -d BeirutiVF.designspace
     fontmake -m BeirutiVF.designspace -o variable

After production of the variable font use for example program OTM to correct the STAT table and add the  missing entres weight axis.



