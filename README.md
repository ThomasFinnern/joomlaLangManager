# joomlaLangManager
Bits and pieces to handle joomla language translation files (coollect IDs, merge fron exisitng ...)

Uses python to find component language ids, merge with old translations and so time allows more translations done
The project origins in the needs when i recreated rsgallery2 for joomla 4

## Differences and matches between two translation files

1) Destination translation missing
2) Destination translation exists and is obsolete/surplus
3) Comments exist on translated file
4) Order of appearance is wrong

## How to handle

1) Missing: (Options)

   1) Prepare translation line with empty translations
      - Good for translation preparation -> use config / calling argument for yes/no
   2) Comment line so it is not used
      * May be interesting for auto translation when the translation is found somewhere else
   3) ignore empty translations in target file

2) Obsolete/surplus (Options)
   1) Move to end of file. Comment line before section
   2) Move to end of file. Comment each behind translation
   3) Remove these translations

3) Comments exist on translated file
   * Target comments will be kept and written with the following translation

4) Order of appearance is wrong
   * On writing order by sourc appearances and add obsolates behind

What can not be handled actually
* Comment moved with surplus translation
* New comments in source files
* Changed translation in source file

# german tranlations

de-AT	German (Austria)
de-CH	German (Switzerland)
de-DE	German (Germany)
de-LI	German (Liechtenstein)
de-LU	German (Luxembourg)
