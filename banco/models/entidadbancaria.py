from odoo import models, fields, api, _


class EntidadBanco(models.Model):
    _name = 'banco.entidad'
    cod = fields.Char('Cod Entidad', required=True)
    nombre = fields.Char('Nombre', required=True)
    sede = fields.Char('Sede', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
