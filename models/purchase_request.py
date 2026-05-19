from jinja2 import defaults

from odoo import fields, models, api


class PurchaseRequest(models.Model):
    _name = 'purchase.request'


    name=fields.Char(string="Request Name",required=True,default='NEW')
    state=fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm')
    ],default='draft',)
    creation_date=fields.Datetime(default=fields.Datetime.now,readonly=True)
    analytical_account=fields.Many2one('account.analytic.account',)
    created_by = fields.Many2one(
        'res.users',
        string='Created By',
        default=lambda self: self.env.user,
        readonly=True
    )
    requested_by =fields.Many2one(
        'res.users',
        string='Requested By',
        default=lambda self: self.env.user,

    )
    requested_on= fields.Datetime(default=fields.Datetime.now)


    purchase_lines_ids=fields.One2many('purchase.request.line',
                                       'purchase_request_id',string='Purchase Lines')
    
    purchase_order_ids = fields.Many2many(
        'purchase.order',
        string='Purchase Orders'
    )
    purchase_order_count = fields.Integer(
        compute='_compute_purchase_order_count'
    )

    def _compute_purchase_order_count(self):
        for rec in self:
            rec.purchase_order_count = len(rec.purchase_order_ids)

    def action_view_orders(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Orders',
            'res_model': 'purchase.order',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.purchase_order_ids.ids)],
        }

    def action_confirm(self):
            print("inside action_confirm")
            vendors={}
            for line in self.purchase_lines_ids:
                vendor=line.vendor_id
                if vendor not in vendors:
                   vendors[vendor]=[]
                vendors[vendor].append(line)

            for vendor,lines in vendors.items()    :
                self.env['purchase.order'].create({
                    'partner_id':vendor.id,
                    'order_line':[(0,0,{
                        'product_id':line.product_id.id ,
                        'product_qty':line.quantity,
                        'uom_id':line.uom_id.id,
                    })]
                })

            self.state = 'confirm'
    @api.model
    def create(self, vals):
        res=super().create(vals)
        if res.name=='NEW':
            res.name=self.env['ir.sequence'].next_by_code('purchase_seq')
        return  res



class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'

    purchase_request_id=fields.Many2one('purchase.request')

    product_id=fields.Many2one('product.product')
    vendor_id=fields.Many2one('res.partner')
    quantity=fields.Float(string='Quantity')
    uom_id=fields.Many2one('uom.uom' )

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            self.uom_id=self.product_id.uom_id
