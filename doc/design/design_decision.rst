################
Design Decisions
################

********
Language
********

The language chosen to implement this tool comes with some history. There is a very similar tool that is already in use
and which has been used already for several projects. However complaints have been made that the language of choice is
Ruby. IMHO this does not make a big difference but it seems that many people know their way around python and are less
hesitant to write some python code to extend the functionality of existing code. Personally I'm no big fan of ducktyping
languages, so I will be doing my best to use typehints. Performance wise the bottle neck is in the I/O writing files
therefore the language choice will most likely not have major performance implications.

Python provides a vast number of libraries which can be used to develop plugins such as PyLaTeX and python-docx to
create documentation or mako template for arbitrary output.

***************************
Data Serialisation Language
***************************

.. note::
   This section might belong to the input plugin

Many formats have been studied to find a good match for the input format for this tool. Python provides libraries to
parse most of these languages. The tool will provide a input plugin which reads YAML. YAML seems the best fit for human
readability and has a python similar syntax. In the first tool XML was used. This also provides the capabilities that
are required. But XML gets very bloated and is harder to scan by eye for humans then YAML.

Other languages that were taken into consideration:

TOML
  To simplistic for some of the use cases
JSON
  Not as human readable as YAML
XML
  Not as human readable as YAML
S-Expression
  Would be a good match if LUA were used but also is harder to read then e.g. YAML



