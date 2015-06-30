#!/bin/bash

# Generate the demo.html file
python demo.py > ../_demo/demo.html

# Minify / Concatenate CSS
rm -f ../cssbis.css
rm -f ../cssbis-min.css
for cssfile in general vcr icons actions browsers couriers countries filetypes os programming_languages severity_levels socmed status
do
	cat ../"$cssfile".css >> ../cssbis.css
	cat ../"$cssfile".css | python cssmin.py > ../"$cssfile"-min.css
	cat ../"$cssfile"-min.css >> ../cssbis-min.css
done

# Clean up cruft
cd ..
find . -name '*.DS_Store' -type f -delete
