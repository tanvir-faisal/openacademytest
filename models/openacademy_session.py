from openerp import api, fields, models

class Session(models.Model):
    _name='openacademy.session'
    
    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today())
    duration = fields.Float(digits=(6,2))   # number 6, after ., 2 digits 
    seats = fields.Integer(string="Number of seats")
    course_id=fields.Many2one("openacademy.course",string="Courses",domain=[('state', '=', 'confirm')])
    attendee_ids=fields.Many2many(comodel_name="res.partner",relation="session_partner_rel",column1="session_id",column2="partner_id",string="Attendees")
    color = fields.Integer()
    state=fields.Selection([('draft',"Draft"),('confirm',"Confirm"),('done',"Done"),('cancel',"Cancel")], default="draft")
    
    
    @api.multi                     # when returns single value----- then @api.one
    def action_confirm(self):
        self.state="confirm"
        
    @api.multi
    def action_done(self):
        self.state="done"
    
    @api.multi                 # when returns multiple value----- then @api.multi
    def action_cancel(self):
        self.state="cancel"
        
    