# -*- encoding: utf-8 -*-
##############################################################################
#
#    Product Variant Multi Key module for OpenERP
#    Copyright (C) 2015 José Javier Goyos
#    
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Product Variant Multi Dimension Key',
    'version': '0.1',
    'category': 'Sales Management',
    'license': 'AGPL-3',
    'complexity': 'expert',
    'description': ("This module extend the capacity of product_variant_multi "
                    "giving the posibility of add an aditional field 'key'"
                    "to the dimension for being used in the variant name" 
                    ),
    'author': "José Javier Goyos",
    'website': '',
    'depends': ['product_variant_multi'],
    'init_xml': [],
    'update_xml': ['dimension_view.xml'],
    'demo_xml': [],
    'data': ['data/stock_demo.xml'],
    'installable': True,
    'active': False,
}
