from openerp import api, exceptions, fields, models
from openerp import _
from openerp.exceptions import Warning

class ConfirmationWizard(models.TransientModel):
    _name = 'confirmation.wizard'
    
    @api.multi
    def action_yes(self):
        raise Warning(_('It can not be deleted'))
    
    
    
