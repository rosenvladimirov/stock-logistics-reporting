#  Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, _


class StockMove(models.Model):
    _inherit = 'stock.move'


def _get_aggregated_values(self, name, description, qty_done, qty_ordered, uom):
    return {
        'name': name,
        'description': description,
        'qty_done': qty_done,
        'qty_ordered': qty_ordered or qty_done,
        'product_uom': uom,
        'product': self.product_id,
        'move_line': self,
    }
