#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import urllib.request
import re

icon_prefix = 'mdi-'
input_file_uri = 'https://raw.githubusercontent.com/Templarian/MaterialDesign-Webfont/master/scss/_variables.scss'
output_file = 'generated/MaterialDesignIcons.cs.pp'
output_prefix = """namespace $rootnamespace$.Helpers
{
    /**
     * MaterialDesignIcons-C#-Consts
     * https://github.com/chteuchteu/MaterialDesignIcons-CSharp-Consts
     */
    public abstract class Mdi
    {
"""

output_sufix = """    }
}
"""

# Download & parse input file
response = urllib.request.urlopen(input_file_uri)
data = response.read()
input = data.decode('utf-8')

regex = re.compile('    "(.*)": (F[A-F0-9]*),?')
matches = regex.findall(input)

if len(matches) == 0:
    print('Could not find variables.')
    sys.exit(1)

# Write in generated file
with open(output_file, 'w') as output:
    output.truncate()

    output.writelines(output_prefix)

    for match in matches:
        icon_name = match[0]

        # Remove dashes, capitalize
        var_name = icon_name.replace('-', ' ').title().replace(' ', '')

        output.write('        public const string {} = "{}";\n'.format(var_name, icon_prefix + icon_name))

    output.writelines(output_sufix)

    print("Generated {} with {} variables".format(output_file, len(matches)))
