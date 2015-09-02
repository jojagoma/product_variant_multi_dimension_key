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

from openerp.osv import fields, orm
import logging
#from tools.translate import _
from openerp.tools.safe_eval import safe_eval

_logger = logging.getLogger(__name__)

class product_variant_dimension_type(orm.Model):    
    _inherit = "product.variant.dimension.type"
    _description = "Dimension Type"

    _columns = {
        'sales_key': fields.char('Sales key', size=24, translate=True),
        }
