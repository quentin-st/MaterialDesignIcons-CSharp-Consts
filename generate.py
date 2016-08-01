#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from upstream_parser import mdi_upstream

icon_prefix = 'mdi-'
output_file = 'content/Helpers/MaterialDesignIcons.cs.pp'
output_prefix = """namespace $rootnamespace$.Helpers
{
    /**
     * MaterialDesignIcons-C#-Consts
     * https://github.com/chteuchteu/MaterialDesignIcons-CSharp-Consts
     *
     * MaterialDesignIcons v#VERSION#
     */
    public abstract class Mdi
    {
"""

output_sufix = """    }
}
"""

# Download & parse input file
meta = mdi_upstream.fetch_meta()

if len(meta['icons']) == 0:
    print('Could not find variables.')
    sys.exit(1)

# Write in generated file
with open(output_file, 'w') as output:
    output.truncate()

    output.writelines(output_prefix.replace('#VERSION#', meta['version']))

    for icon in meta['icons']:
        # Remove dashes, capitalize
        var_name = icon['name'].replace('-', ' ').title().replace(' ', '')

        output.write('        public const string {} = "{}";\n'.format(
            var_name, icon_prefix + icon['name']
        ))

    output.writelines(output_sufix)

    print("Generated {} with {} variables".format(output_file, len(meta['icons'])))
