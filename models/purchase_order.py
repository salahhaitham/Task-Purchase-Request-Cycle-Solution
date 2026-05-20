from odoo import fields, models



class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    purchase_request_id = fields.Many2one(
        'purchase.request',
    )
    purchase_request_count = fields.Integer(
        compute='_compute_purchase_request_count'
    )

    def _compute_purchase_request_count(self):
        for rec in self:
            rec.purchase_request_count = len(rec.purchase_request_id)

    def action_view_requests(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Requests',
            'res_model': 'purchase.request',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.purchase_request_id.id)],
        }