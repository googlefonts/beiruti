fontmake -m Source/2-Production/BeirutiVF.designspace -o variable --output-path fonts/Beiruti[wght].ttf

# custom fixers
python Scripts/fix.py fonts/Beiruti\[wght\].ttf

# gftools fixers
gftools fix-nonhinting fonts/Beiruti\[wght\].ttf fonts/Beiruti\[wght\]-nonhinted.ttf
mv fonts/Beiruti\[wght\]-nonhinted.ttf fonts/Beiruti\[wght\].ttf
rm fonts/*gasp*

# Add STAT table
statmake --designspace Source/2-Production/BeirutiVF.designspace fonts/Beiruti\[wght\].ttf