from openerp import api, fields, models

class Course(models.Model):
    _name='openacademy.course'
    _order='id desc'
    
    name=fields.Char(string="Course Name", required=True , readonly=True, states={'draft': [('readonly', False)]})
    description=fields.Text(readonly=True, states={'draft': [('readonly', False)]})
    responsible_id=fields.Many2one("res.users",string="Responsible Users", readonly=True, states={'draft': [('readonly', False)]})
    session_ids=fields.One2many("openacademy.session","course_id",string="Sessions", readonly=True, states={'draft': [('readonly', False)]})
    selection=fields.Selection([('a','A+'),('b','A-')], readonly=True, states={'draft': [('readonly', False)]})
    state=fields.Selection([('draft',"Draft"),('confirm',"Confirm"),('done',"Done"),('cancel',"Cancel")], default="draft")
    
    
    
    @api.one                      # when returns single value----- then @api.one
    def action_confirm(self):
        self.state="confirm"
        
    @api.multi
    def action_done(self):
        self.state="done"
    
    @api.multi                 # when returns multiple value----- then @api.multi
    def action_cancel(self):
        self.state="cancel"
    
        
    @api.multi    
    def action_wizard(self, context=None):
        return {
           'name': ('Confirmation'),
           'view_type': 'form',
           'view_mode': 'form',
           'src_model': 'openacademy.course',
           'res_model': 'confirmation.wizard',          # reference model
           'view_id': False,
           'type': 'ir.actions.act_window',
           'target':'new',
        }
    
    
    
    